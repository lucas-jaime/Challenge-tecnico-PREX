from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Configuración de la base de datos SQLite (embebida en la aplicación)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mi_base_de_datos.db'  # Archivo SQLite local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definir el modelo de la base de datos
class SystemInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    processor = db.Column(db.String(100))
    process_list = db.Column(db.String(255))
    users = db.Column(db.String(255))
    os_name = db.Column(db.String(100))
    os_version = db.Column(db.String(50))

# Ruta para recibir los datos del agente
@app.route('/collect_data', methods=['POST'])
def collect_data():
    data = request.get_json()

    # Crear una nueva entrada en la base de datos
    new_entry = SystemInfo(
        processor=data['processor'],
        process_list=str(data['process_list']),
        users=str(data['users']),
        os_name=data['os_name'],
        os_version=data['os_version']
    )

    try:
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({"message": "Datos almacenados correctamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Crear todas las tablas si no existen
    db.create_all()
    app.run(host="0.0.0.0", port=5000)  # Asegúrate de que Flask escuche en todas las interfaces
