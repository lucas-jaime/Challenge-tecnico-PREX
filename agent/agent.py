import psutil  # Para obtener los procesos del sistema
import platform  # Para obtener el nombre y versión del sistema operativo
import requests

# Obtener la información del sistema operativo
processor = platform.processor()
os_name = platform.system()
os_version = platform.version()

# Obtener la lista de procesos
process_list = [p.info['name'] for p in psutil.process_iter(['name'])]

# Obtener los usuarios conectados
users = [user.name for user in psutil.users()]

# Datos a enviar
data = {
    "processor": processor,
    "process_list": process_list,
    "users": users,
    "os_name": os_name,
    "os_version": os_version
}

# La URL de la API (reemplazar con la IP pública de EC2)
url = "http://3.137.162.127:5000/collect_data"  # Aquí se usa la IP pública de tu EC2

# Enviar los datos a la API
response = requests.post(url, json=data)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print("Datos enviados correctamente")
else:
    print(f"Error al enviar los datos: {response.status_code}")
