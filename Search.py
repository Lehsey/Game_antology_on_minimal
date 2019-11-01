import sqlite3 as sql

connection = sql.connect('games.db')
cursor = connection.cursor()

def root(game):
    game_name_call = f'SELECT root FROM games WHERE game = "{game}"'
    game_name = cursor.execute(game_name_call).fetchone()[0]
    game_type_call = f'SELECT type FROM types WHERE id = (SELECT type FROM games WHERE game = "{game}")'
    game_type = cursor.execute(game_type_call).fetchone()[0]
    return f'{game_type}\\{game_name}.exe'

def proc(game):
    game_name_call = f'SELECT root FROM games WHERE game = "{game}"'
    game_name = cursor.execute(game_name_call).fetchone()[0]
    return f'{game_name}.exe'
