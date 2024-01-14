# Proyecto de inicio de sesión por voz y enlace de cuentas
Este proyecto es una implementación de inicio de sesión utilizando comandos de voz para autenticar a los usuarios y vincular sus cuentas. Proporciona una forma segura y conveniente de acceder a aplicaciones y servicios utilizando la voz como método de autenticación.


## Características principales
- Inicio de sesión por voz: Los usuarios pueden iniciar sesión diciendo cualquier cosa, lo que elimina la necesidad de escribir contraseñas u otros datos de autenticación manualmente.
- Vinculación de cuentas: Permite a los usuarios vincular varias cuentas y acceder a ellas fácilmente. Esto simplifica el proceso de cambio entre cuentas y proporciona una experiencia de usuario fluida.
- Seguridad avanzada: El sistema utiliza algoritmos de reconocimiento de voz y técnicas de autenticación para garantizar la seguridad de las cuentas de usuario y prevenir el acceso no autorizado.
- Interfaz intuitiva: La interfaz de usuario es sencilla e intuitiva, lo que facilita a los usuarios interactuar con el sistema y realizar las acciones necesarias.


## Instalación y configuración
Clona este repositorio en tu equipo, no te olvides de utilizar git lfs para descargar los archivos grandes.
Se puede descargar aquí: https://git-lfs.com/

### Es necesario
- Git lfs.
- Para descargar el repositorio, utilizar el comando 'git lfs clone <url_repositorio>'

### Ejecución con Docker (recomendado)
1. Asegúrate de tener Docker en tu equipo
2. Sitúate en la carpeta raíz del proyecto
3. Ejecuta el siguiente comando en la terminal:
        docker-compose up -d
4. Abre el navegador e introduce la URL http://localhost:5173 en la barra de búsqueda para acceder a la web


## Tener en cuenta
- La primera vez que se intente iniciar sesión con voz cada vez que se levante el servidor este tardará un tiempo en procesar la petición, ya que debe cargar la red neuronal. Los siguientes intentos se procesarán con mayor velocidad.
- En la vista de perfil, al solicitar ver los servicios enlazados o disponibles para enlazar es posible que la información tarde unos segundos en aparecer en pantalla. Esto es debido a la conexión con el servidor de la base de datos.
- Si se descarga el proyecto e intenta utilizarse no va a funcionar, debido a que la instancia de AWS con la base de datos que se utilizó ha sido deshabilitada. Si se desea habilitar una base de datos, se deberá actualizar el fichero .env, huubicado en la carpeta API. La base de datos se creo en PostgreSQL, siguiendo el modelo definido en la imagen EsquemaBBDD.png, hubicada en la carpeta API.