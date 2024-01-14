# Establecer la imagen base
FROM node:16

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app
RUN npm install -g vite
# Copiar el archivo package.json y package-lock.json (si existe) al directorio de trabajo
COPY package*.json ./

# Instalar las dependencias del proyecto
RUN npm install

# Copiar el resto de los archivos del proyecto al directorio de trabajo
COPY . .

# Compilar la aplicación
RUN npm run build

# Exponer el puerto en el que se ejecuta la aplicación (el mismo que has configurado en tu vite.config.js)
EXPOSE 5100

# Comando para iniciar la aplicación
CMD [ "npm", "run", "dev", "--", "--host"]