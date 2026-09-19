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
                ac_num INTEGER PRIMARY KEY AUTOINCREMENT,
                cus_name TEXT NOT NULL,
                balance INTEGER,
                savings INTEGER)""")

        conn.commit()
        conn.close()

    @staticmethod
    def generate_account_number(db_name):
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        while True:
            candidate = random.randint(100000, 999999)
            cursor.execute("SELECT 1 FROM users WHERE ac_num = ?", (candidate,))
            if cursor.fetchone() is None:
                conn.close()
                return candidate

    @staticmethod
    def create_customer(db_name, cus_name, balance=0):
        account_number = Database.generate_account_number(db_name)
        savings = 0
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (ac_num, cus_name, balance, savings) VALUES (?, ?, ?, ?)",
            (account_number, cus_name, balance, savings),
        )
        conn.commit()
        conn.close()
        return account_number

    @staticmethod
    def create_cust_savings(db_name, cus_name, balance=0):
        account_number = Database.generate_account_number(db_name)
        savings = 1
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        cursor.execute(
                "INSERT INTO users (ac_num, cus_name, balance, savings) VALUES (?, ?, ?, ?)",
                (account_number, cus_name, balance, savings),
            )
        conn.commit()
        conn.close()
        return account_number

    @staticmethod
    def deposit_money(db_name, amount, ac_num):
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        cursor.execute(
             "UPDATE users SET balance = balance + ? WHERE ac_num = ?", (amount, ac_num),
        )

        cursor.execute("SELECT balance FROM users WHERE ac_num = ?", (ac_num,))
        balance = cursor.fetchone()[0]


        conn.commit()
        conn.close()

        return balance


    @staticmethod
    def withdraw_money(db_name, amount, ac_num):
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        cursor.execute(
                "UPDATE users SET balance = balance - ? WHERE ac_num = ?", (amount, ac_num),
        )
    
        cursor.execute("SELECT balance FROM users WHERE ac_num = ?", (ac_num,))
        balance = cursor.fetchone()[0]
    
    
        conn.commit()
        conn.close()
    
        return balance

    @staticmethod
    def check_balance(db_name, ac_num):
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT balance FROM users WHERE ac_num = ?", (ac_num,))
        balance = cursor.fetchone()[0]
        
        conn.close()
        
        return balance


    @staticmethod
    def check_savings_acct(db_name, ac_num):
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
            
        cursor.execute("SELECT savings FROM users WHERE ac_num = ?", (ac_num,))
        savings = cursor.fetchone()[0]
            
        conn.close()
            
        return savings


    @staticmethod
    def interest_balance(db_name, ac_num):
        interest = 0.03
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT balance FROM users WHERE ac_num = ?", (ac_num,))
        balance = cursor.fetchone()[0]

        if balance > 1:
            interest_rate = balance * interest
            balance += interest_rate

        conn.close()

        return balance


    #test code to check the value of savings
    @staticmethod
    def check_status(db_name, ac_num):
        conn = Database.get_connection(db_name)
        cursor = conn.cursor()
                    
        cursor.execute("SELECT savings FROM users WHERE ac_num = ?", (ac_num,))
        status = cursor.fetchone()[0]
    
        conn.close()
                    
        return status