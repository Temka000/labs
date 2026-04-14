# app/src/config/database.py
import os

class Config:
    DB_HOST = os.getenv('DB_HOST', 'db')
    DB_NAME = os.getenv('DB_NAME', 'tasksdb')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD')

    @staticmethod
    def get_db_url():
        return f"host={Config.DB_HOST} dbname={Config.DB_NAME} user={Config.DB_USER} password={Config.DB_PASSWORD}"
