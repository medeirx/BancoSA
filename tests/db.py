import sqlite3 as sql

connection = sql.connect("../data/database.db")
cursor = connection.cursor()

query = '''
        INSERT INTO users (name, surname, cpf)
        VALUES (?,?, ?);
        '''

data = ('Matheus', 'Medeiros', '21054787786')

cursor.execute(query, data)

connection.commit()