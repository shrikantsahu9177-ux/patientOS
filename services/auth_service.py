"""
Authentication Service
"""

from config.database import DatabaseManager


class AuthService:

    def __init__(self):

        self.db = DatabaseManager()

    def login(self, username, password):

        user = self.db.fetchone(
            """
            SELECT *
            FROM users
            WHERE username=?
            AND password=?
            """,
            (
                username,
                password
            )
        )

        return user