# Imagen base
FROM python:3.9

RUN apt-get update && \
    apt-get install -y ffmpeg

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY requirements.txt .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

ENV FFMPEG_PATH=/usr/bin/ffmpeg

# Exponer el puerto en el que se ejecutará la aplicación
EXPOSE 5000
WORKDIR /app/src
# Comando para iniciar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]