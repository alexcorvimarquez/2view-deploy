
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Ruta pública
@app.route("/public/<path:filename>")
def public_files(filename):
    return send_from_directory("public", filename)

# Página raíz (puede ser útil para testeo)
@app.route("/")
def index():
    return "Servidor 2View funcionando correctamente"

# Solo si quieres ejecutar localmente
if __name__ == "__main__":
    app.run(debug=True)