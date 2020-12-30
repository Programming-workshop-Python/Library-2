from flask import Flask
import psycopg2
import logging


def create_app():
    app = Flask(__name__)
    return app

#---Данные для работы с облачной БД---
#def create_db():
#    return psycopg2.connect(
#        dbname='rmtswqut',
#        user='rmtswqut',
#        password='2cHJDZZGDcDnakBXSrvGevKdIqaGWdqM',
#        host='rajje.db.elephantsql.com'
#    )
#---Данные для работы с развёрнутой БД
def create_db():
    con = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='123',
        host="127.0.0.1",
        port="5432"
    )
    return con



def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s - %(message)s')
    file_handler = logging.FileHandler(filename='Logs.log', mode='w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

app = create_app()
db = create_db()
logger = setup_logger()

