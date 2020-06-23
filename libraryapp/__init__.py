from flask import Flask
import psycopg2


def create_app():
    app = Flask(__name__)
    return app


def create_db():
    return psycopg2.connect(
        dbname='rmtswqut',
        user='rmtswqut',
        password='2cHJDZZGDcDnakBXSrvGevKdIqaGWdqM',
        host='rajje.db.elephantsql.com'
    )


app = create_app()
db = create_db()
