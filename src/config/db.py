import mariadb

config ={
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '1273',
    'database': 'papeleria',
}

DB = mariadb.connect(**config)
DB.autocommit= True

