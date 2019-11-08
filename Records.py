import sqlite3 as sql




def set_rec(game, name, scor):
    # подключение к базе
    connection = sql.connect('Records.db')
    cursor = connection.cursor()
    # проверка игры и запись рекорда
    if game == 'Змейка':
        for el in cursor.execute('SELECT player FROM Snake').fetchall():
            if str(name) == str(el[0]):
                scor_old = cursor.execute(f'SELECT score FROM Snake WHERE player = {el[0]}').fetchall()
                # проверка побития рекорда
                if int(scor_old[0][0]) < scor:
                    cursor.execute(
                        f'UPDATE Snake SET score = {scor} WHERE player = "{name}"')
                break
        else:
            record_call = f'INSERT INTO Snake(player, score) VALUES("{name}", {scor})'
            cursor.execute(record_call)
        connection.commit()
    elif game == "Ним":
        for el in cursor.execute('SELECT player FROM Nim').fetchall():
            if name == el[0]:
                ned = cursor.execute(
                    f'SELECT * FROM Nim WHERE player = "{name}"').fetchall()
                if scor == 0:
                    cursor.execute(
                        f'UPDATE Nim SET AI = {int(ned[0][3]) + 1} WHERE player = "{name}"')
                else:
                    cursor.execute(
                        f'UPDATE Nim SET winner = {int(ned[0][2]) + 1} WHERE player = "{name}"')
                break
        else:
            if scor == 0:
                record_call = f'INSERT INTO Nim(player, winner, AI) VALUES("{name}", "0", {scor})'
            else:
                record_call = f'INSERT INTO Nim(player, winner, AI) VALUES("{name}", {scor}, "0")'
            cursor.execute(record_call)
    connection.commit()
    connection.close()
