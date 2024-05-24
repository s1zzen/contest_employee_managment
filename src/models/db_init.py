import sqlite3
import os
from src.config import Configuration


def init_db():
    cfg = Configuration()
    os.makedirs(os.path.dirname(cfg.db_path), exist_ok=True)  # Создание папки, если её нет
    conn = sqlite3.connect(cfg.db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Branches (
            branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            director_id INTEGER DEFAULT NULL,
            FOREIGN KEY (director_id) REFERENCES Employees(employee_id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            branch_id INTEGER,
            FOREIGN KEY (branch_id) REFERENCES Branches(branch_id)
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
