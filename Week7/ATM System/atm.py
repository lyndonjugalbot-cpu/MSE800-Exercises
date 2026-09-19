from abc import ABC, abstractmethod
from db import Database

class ATM(ABC):
    @abstractmethod
    def insert_card(self, card_num): 
        pass

    @abstractmethod
    def enter_pin(self, pin): 
        pass

    @abstractmethod
    def check_balance(self): 
        pass

    @abstractmethod
    def withdraw_money(self): 
        pass


class BankATM(ATM):
    database = Database.DB_NAME
    def insert_card(self, card_num): 
        card_num = input("Enter your account number: {card_num}")
        return card_num
   
    def enter_pin(self, pin): 
        pin = input("Enter your 4 digit PIN: {pin}")
        return pin
    
    def check_balance(self): 
        card_num = self.insert_card
        #check balance
        conn = Database.get_connection(self.database)
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE card_num = ?", (card_num,))
        balance = cursor.fetchone()[0]
        return balance


    def withdraw_money(self, amount, card_num):
        conn = Database.get_connection(self.database)
        cursor = conn.cursor()
        cursor.execute(
                    "UPDATE users SET balance = balance - ? WHERE card_num = ?", (amount, card_num),
            )
        
        cursor.execute("SELECT balance FROM users WHERE card_num = ?", (card_num,))
        balance = cursor.fetchone()[0]
        
        
        conn.commit()
        conn.close()
        
        return balance