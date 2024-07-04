FROM node:18

# Directorio de trabajo
WORKDIR /app

# Copiar package.json y package-lock.json
COPY package*.json .

# Instalar dependencias
RUN npm install

COPY . .