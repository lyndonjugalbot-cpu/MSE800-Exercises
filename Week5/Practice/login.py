import sqlite3

DB_NAME = "users.db"

def get_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def create_table(conn):
    conn = get_connection(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL)""")

    conn.commit()
    conn.close()

def main():
    create_table(DB_NAME)
    while True:
        print("\n1) Register a new user")
        print("2) Login")
        print("3) Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()