from utils.DateFormat import DateFormat

class Usuario():

    def __init__(self, correo, voice_password=None, normal_password=None, nombre=None, apellidos=None, fecha_registro=None) -> None:
        self.correo = correo
        self.voice_password = voice_password
        self.normal_password = normal_password
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_registro = fecha_registro

    def to_JSON(self):
        return {
            'correo': self.correo,
            'voice_password': self.voice_password,
            'normal_password': self.normal_password,
            'nombre': self.nombre,
            'apellidos': self.apellidos,
            'fecha_registro': self.fecha_registro#DateFormat.convert_date(self.fecha_registro)
        }