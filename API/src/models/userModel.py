from database.db import get_connection
from .entities.Usuario import Usuario
from .entities.Sesion import Sesion
import psycopg2
import bcrypt
from datetime import date, datetime
from flask import current_app, request
import os
import base64
import hashlib

class UserModel():

    def obtenerFechaHoy():
        fechaActual = datetime.now()
        fechaHora_string = fechaActual.strftime("%Y-%m-%d %H:%M:%S")
        return fechaHora_string

    @classmethod
    def get_user(self, correo):
        try:
            connection = get_connection()

            cursor = connection.cursor()
            cursor.execute(f'SELECT * from "Usuario" WHERE correo = \'{correo}\'')
            resultset = cursor.fetchone()

            if resultset is None:
                # No se encontró ningún usuario con el correo electrónico proporcionado
                return None

            user = Usuario(resultset[0], resultset[1], resultset[2], resultset[3], resultset[4], resultset[5])
            return user.to_JSON()
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            connection.close()
        
    @classmethod
    def add_user(self, user):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            data = UserModel.get_user(user['correo'])                             

            if data is None:
                fecha = self.obtenerFechaHoy()

                try:
                    if user["voice_password"] is None:
                        cursor.execute(f'INSERT INTO "Usuario" (correo, normal_password, nombre, apellidos, fecha_registro) '+
                                    f'VALUES (\'{user["correo"]}\', '+
                                    f'\'{bcrypt.hashpw(bytes(user["normal_password"], encoding="utf-8"), bcrypt.gensalt()).decode()}\', '+
                                     f'\'{user["nombre"]}\', \'{user["apellidos"]}\', \'{fecha}\');')
                    else:
                        cursor.execute(f'INSERT INTO "Usuario" (correo, voice_password, nombre, apellidos, fecha_registro) '+
                                    f'VALUES (\'{user["correo"]}\', \'{user["voice_password"]}\', '+
                                    f'\'{user["nombre"]}\', \'{user["apellidos"]}\', \'{fecha}\');')
                        
                    message = "Usuario agregado"
                    error = False
                    connection.commit()
                except psycopg2.Error as e:
                    print("Erorr psycopg2: ", e)
                    return {"Message": e, "Error": True, "User": None}
            else:
                message = "Este usuario ya existe"
                error = True
        except Exception as e:
            print("Error general: ", e)
            return {"Message": e, "Error": True, "User": None}
        finally:
            connection.close()
            return {"Message": message, "Error": error, "User": user}
        
    @classmethod
    def update_user(self, newData, correo):

        try:
            connection = get_connection()

            cursor = connection.cursor()

            try:
                    
                cursor.execute(f'UPDATE "Usuario" SET nombre=\'{newData["nombre"]}\', apellidos=\'{newData["apellidos"]}\' '+
                               f'WHERE correo=\'{correo}\';')
                    
                connection.commit()
                message = "Datos actualizados"
                error = False
            except psycopg2.Error as e:
                return {"Message": e, "Error": True, "NewData": None}

        except Exception as e:
            return {"Message": e, "Error": True, "NewData": None}
        finally:
            connection.close()
            return {"Message": message, "Error": error, "NewData": newData}
        
    @classmethod
    def obtener_servicios(self, esDiccionario):
        try:
            connection = get_connection()

            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM "Servicio";') 
            resultset = cursor.fetchall()

            if resultset is None:
                # No se encontró ningún usuario con el correo electrónico proporcionado
                return None

            if esDiccionario:
                dicSitios = {}
                for sitio in resultset:
                    dicSitios[sitio[1]] = {'id': sitio[0],
                                            'nombre': sitio[1],
                                            'url': sitio[2]}
                return dicSitios
            else:
                listaSitios = []
                for sitio in resultset:
                    listaSitios.append(sitio[2])

                return listaSitios
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            connection.close()

    @classmethod
    def obtener_servicios_enlazados(self, correo):
        try:
            connection = get_connection()

            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM "Servicio" where id_servicio IN ( '+
                           f'SELECT servicio_id FROM "Usuario-Servicio" where correo = \'{correo}\');')
            resultsetServicio = cursor.fetchall()

            if resultsetServicio is None:
                # No se encontró ningún usuario con el correo electrónico proporcionado
                return None

            listaSitios = {}
            for sitio in resultsetServicio:

                cursor.execute(f'SELECT * FROM "Usuario-Servicio" WHERE correo = \'{correo}\' AND servicio_id = {sitio[0]};')
                resultsetUsuarioServicio = cursor.fetchone()

                listaSitios[sitio[1]] = {'id': sitio[0],
                                           'nombre': sitio[1],
                                           'url': sitio[2],
                                           'ultimo_login': resultsetUsuarioServicio[3],
                                           'fecha_enlace': resultsetUsuarioServicio[4]}
            return listaSitios
        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            connection.close()

    @classmethod
    def enlazarServicio(self, correo, url):
        try:
            connection = get_connection()

            cursor = connection.cursor()
            cursor.execute(f'SELECT servicio_id FROM "Usuario-Servicio" where correo = \'{correo}\';') 
            resultsetUsuarioServicio = cursor.fetchall()

            cursor.execute(f'SELECT * from "Servicio" where url_servicio = \'{url}\';')
            resultsetServicio = cursor.fetchone()

            fecha = self.obtenerFechaHoy()

            if resultsetUsuarioServicio is None:
                # No se encontró ningún servicio para este usuario
                cursor.execute(f'INSERT into "Usuario-Servicio" (servicio_id, correo, ultimo_login, fecha_enlace) VALUES (\'{resultsetServicio[0]}\', \'{correo}\', \'{fecha}\', \'{fecha}\');')
                connection.commit()
                return True
            else:
                # El usuario ya tiene enlazado algún servicio
                for servicio in resultsetUsuarioServicio:
                    if resultsetServicio[0] == servicio[0]:
                        # El usuario ya tiene enlazado ese servicio
                        # Se actualiza la fecha del ultimo login
                        cursor.execute(f'UPDATE "Usuario-Servicio" SET ultimo_login = \'{fecha}\' WHERE ' + 
                                       f'correo = \'{correo}\' and servicio_id = {resultsetServicio[0]};')
                        connection.commit()
                        return False
                
                # Si no lo tiene enlazado
                cursor.execute(f'INSERT into "Usuario-Servicio" (servicio_id, correo, ultimo_login, fecha_enlace) VALUES (\'{resultsetServicio[0]}\', \'{correo}\', \'{fecha}\', \'{fecha}\');')
                connection.commit()
                return True

        except Exception as e:
            return {'error': str(e)}, 500
        finally:
            connection.close()

    @classmethod
    def convertirDeBase64(self, base64Data, nombreArchivo):
        # Extraer el archivo de audio del objeto recibido en Flask    
        decoded_audio = base64.b64decode(base64Data)

        # Almacenar el archivo de audio en el servidor de Flask
        audio_file_path = os.path.join(current_app.static_folder, nombreArchivo)
        with open(audio_file_path, 'wb') as f:
            f.write(decoded_audio)

        # Devuelve la ruta al audio almacenado en el servidor
        return audio_file_path

    @classmethod
    def createSession(self, idSesion):
        current_app.activeSessions[hashlib.sha512(bytes(idSesion, encoding='utf-8')).hexdigest()] = 'active'
        return True

