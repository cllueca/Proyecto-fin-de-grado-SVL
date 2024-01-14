import os
from flask import Flask, request, jsonify
from config import config
from flask_cors import CORS
os.environ["PATH"] += os.pathsep + os.environ.get('FFMPEG_PATH')

from dotenv import load_dotenv
from flask_jwt_extended import JWTManager

import userRecognitionService as URS

from flask import session
import bcrypt
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import hashlib
import datetime

# Models
from models.userModel import UserModel

app = Flask(__name__)

load_dotenv()
CORS(app, resources={r"/api/*": {"origins": "*"}})


app.modelo = URS.User_Recognition_Service()
app.activeSessions = {}
app.servicioCore = 'http://localhost:5173'

app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config.from_object(config["development"])

jwt = JWTManager(app)


def obtenerFechaHoy():
    fechaActual = datetime.now()
    fechaHora_string = fechaActual.strftime("%Y-%m-%d %H:%M:%S")
    return fechaHora_string


@app.route("/api/user/verSessions", methods=["GET"])
def verSessions():
    # Funcion provisional, solamente se ven las sesiones activas
    return app.activeSessions

@app.route("/api/user/authenticate/external", methods=["POST"])
def check_active():
    try:
        data = request.json
        
        # Mira que la URL este en los servicios disponibles
        if request.environ['HTTP_REFERER'] in UserModel.obtener_servicios(False):
            # Mira que haya sesiones activas en el servidor
            if len(app.activeSessions) != 0:
                # Obtengo la sesion del usuario en el servicio core
                claveSesionCore = data['correo'] + "-" + app.servicioCore + request.headers.get('User-Agent')
                # Mira que esa sesion core exista
                if hashlib.sha512(bytes(claveSesionCore, encoding='utf-8')).hexdigest() in app.activeSessions:
                    user = UserModel.get_user(data["correo"])
                    # Creo la clave de sesion del nuevo servicio
                    claveSesionNueva = user['correo'] + "-" + request.environ['HTTP_ORIGIN'] + request.headers.get('User-Agent')
                    # Compruebo que esa clave de sesion no exista
                    if hashlib.sha512(bytes(claveSesionNueva, encoding='utf-8')).hexdigest() not in app.activeSessions:
                        # Se ve si se enlaza por primera vez o no
                        UserModel.enlazarServicio(user['correo'], request.environ['HTTP_REFERER'])
                        # Creo el jwt y la sesion
                        access_token = create_access_token(identity=claveSesionNueva)
                        UserModel.createSession(claveSesionNueva)
                        
                        return {"Message": "Este usuario esta activo en el servidor", "nombre": user['nombre'],
                            "apellidos": user['apellidos'], "correo": user['correo'], "Access_token": access_token, "Error": False}
                    else:
                        return {"Message": "Este servicio ya tiene la sesion iniciada", "Error": True}
                else:
                    return {"Message": "Este usuario no esta activo en el servidor", "Error": True}
            else:
                return {"Message": "No hay sesiones activas en el servidor", "Error": True}
        else:
            return {"Message": "Este servicio no dispone de soporte", "Error": True}
        
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route("/api/user/authenticate", methods=["POST"])
def auth_user():
    try:
        # Se obtienen los datos mandados desde el front y se pasan a formato json
        data = request.json

        # Se obtiene el usuario de la base de datos con el correo indicado por el usuario
        user = UserModel.get_user(data["correo"])

        # Por ahora el access token (jwt) no tiene valor
        access_token = None

        # Si el usuario existe
        if user is not None:
            # Si la contraseña es por texto
            if user['normal_password'] != 'None':
                pct = 0
                # Se comparan las contraseñas, a ver si coinciden
                if bcrypt.checkpw(bytes(data["normal_password"], encoding='utf-8'), bytes(user["normal_password"], encoding='utf-8')):
                    message = "Contraseña correcta" 
                    error = False
                else:
                    message = "Contraseña incorrecta" 
                    error = True
            # Contraseña por voz
            else:
                model = app.modelo # Se llama a la clase con la CNN

                # Se transforman los audios de base 64 para que librosa pueda abrirlos
                audioGuardado = UserModel.convertirDeBase64(user["voice_password"], 'audioBBDD.wav')
                audioNuevo = UserModel.convertirDeBase64(data["voice_password"],'audioNuevo.wav')

                # Se realizan predicciones
                pct1 = model.predict(model, audioNuevo, audioGuardado)
                pct2 = model.predict(model, audioGuardado, audioNuevo)
                media = (pct2+pct1)/2

                # Se eliminan los audios del servidor
                try:
                    os.remove(audioNuevo)
                    os.remove(audioGuardado)
                except OSError as e:
                    print(e)
                
                pct = media
                print(f'Porcentaje de similitud obtenido: {pct}%')

                # Si las voces se parecen mas de un 60&, se autentica al usuario
                if media < 60:
                    error = True
                    message = "No coinciden las voces"
                else:
                    error= False
                    message = "Identificado como dueño de la cuenta"

            # Si el usuario ha sido autenticado, se crea un access token y se añade al diccionario de sesiones activas
            if not error:
                # Se obtiene el correo del usuario y se añade identificacion extra para las sesiones

                claveSesion = user['correo'] + "-" + app.servicioCore + request.headers.get('User-Agent')
                access_token = create_access_token(identity=claveSesion)
                UserModel.createSession(claveSesion)

            return {"Message": message, "Error": error, "pct": pct, "nombre": user['nombre'],
                    "apellidos": user['apellidos'], "fecha_registro": user['fecha_registro'], "Access_token": access_token}, 200
        # Si el usuario no existe
        else:
            message = "Este usuario no existe en la base de datos"
            error = True
            return {"Message": message, "Error": error, "pct": 0}, 401
        
    except Exception as e:
        print("EXCEPTION: ", e)
        return jsonify({'message': str(e)}), 500
    
@app.route("/api/user/logout", methods=["GET"])
@jwt_required()
def logout_user():

    # Se obtiene el token jwt de la cabecera de la peticion HTTP
    try:
        # Se obtiene el identificador del usuario a partir del token JWT y se hashea
        user_id = hashlib.sha512(bytes(get_jwt_identity(), encoding='utf-8')).hexdigest()
        
        # Si el hash del id del usuario esta en las sesiones activas, se elimina, cerrando la sesion
        if user_id in app.activeSessions:
            del app.activeSessions[user_id]
            return jsonify({"Message": "Sesion cerrada", "Error": False})
        else:
            return jsonify({"Message": "Este usuario no tiene la sesion iniciada", "Error": True}), 401
    except Exception as e:
        # Si el token es inválido, se lanza una excepción
        return jsonify({"Message": "Token JWT inválido", "Error": True}), 401
    
@app.route("/api/user/add", methods=["POST"])
def register_user():
    # Se obtienen los datos de la peticion POST en formato json
    data = request.json

    # Se añade el usuario a la base de datos
    status = UserModel.add_user(data)

    if not status['Error']:
        # Se añade un identificador al correo para crear el id de usuario, su jwt y su sesion activa
        claveSesion = status['User']['correo'] + "-" + app.servicioCore + request.headers.get('User-Agent')
        access_token = create_access_token(identity=claveSesion)
        UserModel.createSession(claveSesion)
        status['Access_token'] = access_token
    
    # Se manipula lo que se va a devolver al front y se manda
    status['User']['correo'] = '' # Se manda el correo vacio porque con el jwt ya vale
    
    return jsonify(status)

@app.route("/api/user/update", methods=["POST"])
@jwt_required()
def update_user():
    try:
        # Se obtienen los datos de la peticion (puedo quitar el correo de aqui y obtenerlo con get_jwt_identity)
        data = request.json
        # Obtener el identificador del usuario a partir del token JWT
        correo = get_jwt_identity().split("-")[0]
        # Se obtiene el usuario correspondiente al correo
        user = UserModel.get_user(correo)

        # Si el usuario existe, se actualizan sus datos
        if user is not None:
            status = UserModel.update_user(data, correo)
            return jsonify(status)
        else:
            return jsonify({"Message": "Este usuario no se encuentra en la base de datos", "Error": True})
    except Exception as e:
        # Si el token es inválido, se lanza una excepción
        return jsonify({"Message": "Token JWT inválido", "Error": True}), 401
    
@app.route("/api/user/availableServices", methods=["GET"])
@jwt_required()
def get_available_services():

    try:
        # Se obtienen los servicios disponibles para enlazar
        listaDisponibles = UserModel.obtener_servicios(True)

        # Se obtienen los servicios con los que el usuario ya ha enlazado la cuenta
        listaEnlazados = UserModel.obtener_servicios_enlazados(get_jwt_identity().split("-")[0])

        # Si existen servicios disponibles
        if listaDisponibles is not None:
            # Se crea una lista que solamente contendra los servicios disponibles con los que el usuario no haya enlazado su cuenta
            nuevaLista = {}
            for sitio in listaDisponibles:
                if sitio not in listaEnlazados:
                    nuevaLista[sitio] = listaDisponibles[sitio]

            return jsonify({"Error": False, "Message": "Bien", "Sitios": nuevaLista})
        else:
            return {"Error": True, "Message": "No se han encontrado sitios disponibles"}
    except Exception as e:
        # Si el token es inválido, se lanza una excepción
        return jsonify({"Message": "Token JWT inválido", "Error": True}), 401
    
@app.route("/api/user/linkedServices", methods=["GET"])
@jwt_required()
def get_linked_services():

    try:
        # Se obtienen los servicios con los que el usuario ha enlazado la cuenta
        lista = UserModel.obtener_servicios_enlazados(get_jwt_identity().split("-")[0])

        # Si la lista contiene sitios
        if lista is not None:
            return jsonify({"Error": False, "Message": "Bien", "Sitios": lista})
        else:
            return {"Error": True, "Message": "No hay sitios enlazados"}
    except Exception as e:
        # Si el token es inválido, se lanza una excepción
        return jsonify({"Message": "Token JWT inválido", "Error": True}), 401



def page_not_found(error):
    return'<h1>Lo sentimos, esta URL no se encuentra disponible</h1>', 404

if __name__ =='__main__':

    app.modelo.predict(app.modelo, "keras_utils/audioInicio.wav", "keras_utils/audioInicio.wav")
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(debug=False, port=5000)