import sqlite3
from datetime import datetime
from controllers.GamePersistenceHandler import GamePersistenceHandler


class GameSQLiteHandler(GamePersistenceHandler):

    @staticmethod
    def connect_db():
        db = sqlite3.connect('data/score.db')

        db.execute("""
                    CREATE TABLE IF NOT EXISTS score 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                    username TEXT, 
                    game_date DATETIME, 
                    user_score INTEGER,
                    computer_score INTEGER
                    )
                   """)
        return db

    @staticmethod
    def save_game(controller):
        db = GameSQLiteHandler.connect_db()
        print("DB OK")
        now = datetime.now().strftime("%B %d, %Y %I:%M%p")
        name = controller.user.name
        user_score = controller.user.score
        computer_score = controller.computer.score
        query =f"INSERT INTO score (username, game_date, user_score, computer_score) " + \
               f"VALUES ('{name}', '{now}', {user_score}, {computer_score})"
        print(query)
        db.execute(query)
        db.commit()

    @staticmethod
    def load_history(username):
        history = []
        db = GameSQLiteHandler.connect_db()
        cursor = db.cursor()
        query = f"SELECT * FROM score WHERE username='{username}'"
        result = cursor.execute(query)

        for row in result:
            history.append([
                row[1], row[2], row[3], row[4]
            ])
        print("DB history")
        print(history)
        return history
