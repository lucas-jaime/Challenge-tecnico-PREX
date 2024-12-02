# Imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar todo el código de la API al contenedor
COPY . /app/

# Exponer el puerto que usa la API
EXPOSE 5000

# Comando para iniciar la API
CMD ["python", "app.py"]
