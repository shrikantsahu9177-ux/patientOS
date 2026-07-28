"""
database.py
SQLite Database Manager
"""

import sqlite3

from config.config import DATABASE_DIR, DATABASE_PATH


class DatabaseManager:

    def __init__(self):

        DATABASE_DIR.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(DATABASE_PATH)

        self.connection.execute("PRAGMA foreign_keys = ON")

        self.cursor = self.connection.cursor()

        self.create_tables()

        self.create_default_admin()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            role TEXT NOT NULL
        )
        """)

        self.connection.commit()

    def create_default_admin(self):

        self.cursor.execute(
            """
            SELECT * FROM users
            WHERE username=?
            """,
            ("admin",)
        )

        user = self.cursor.fetchone()

        if user is None:

            self.cursor.execute(
                """
                INSERT INTO users
                (username,password,role)
                VALUES(?,?,?)
                """,
                (
                    "admin",
                    "admin123",
                    "Administrator"
                )
            )

            self.connection.commit()

    def execute(self, query, values=()):

        self.cursor.execute(query, values)

        self.connection.commit()

    def fetchone(self, query, values=()):

        self.cursor.execute(query, values)

        return self.cursor.fetchone()

    def fetchall(self, query, values=()):

        self.cursor.execute(query, values)

        return self.cursor.fetchall()

    def close(self):

        self.connection.close()