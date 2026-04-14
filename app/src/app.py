# app/src/app.py
from flask import Flask
from routes import tasks_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.register_blueprint(tasks_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
