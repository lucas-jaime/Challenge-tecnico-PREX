# Imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requisitos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar todo el código del agente al contenedor
COPY . /app/

# Comando para ejecutar el agente
CMD ["python", "agent.py"]
