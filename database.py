import sqlite3

class Database:
    def __init__(self, db_name='example.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            feature REAL NOT NULL,
            target REAL NOT NULL
        )
        ''')
        self.conn.commit()

    def insert_data(self, feature, target):
        self.cursor.execute('''
        INSERT INTO data (feature, target)
        VALUES (?, ?)
        ''', (feature, target))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute('SELECT * FROM data')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()



