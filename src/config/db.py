import mariadb
from os import path
import json

CONEXION_PATH = path.abspath('src/config/conexion.json')
SQL_PARH =path.abspath('tienda.sql')


def createDB():
    if path.exists(CONEXION_PATH):
        file_conexion = open=(CONEXION_PATH, 'r')

        config = json.loads(file_conexion.read())

        globals.DB = mariadb.connect(**config)
        globals.DB.autocommit= True

    else:
        globals.DB = False

createDB()

def instalarDB():
    file_sql = open(SQL_PATH, 'r')
    sql = file_sql.read()

    cursor = globals.DB.cursor()

    sqlCommands = sql.split(';')
    
    for command in sqlCommands:
        try:
            if command.strip() != '':
                cursor.execute(command)
        except:
            print ("Saltando comando")

    cursor.close()