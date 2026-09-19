import random
import sqlite3

class Database:
    DB_NAME = "bank.db"
    
    @staticmethod
    def get_connection(db_name):
        conn = sqlite3.connect(db_name)
        return conn

    @staticmethod
    def create_table(db_name):
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
                card_num INTEGER PRIMARY KEY AUTOINCREMENT,
                cus_name TEXT NOT NULL,
                balance INTEGER)""")

        conn.commit()
        conn.close()