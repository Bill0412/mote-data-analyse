from config import mysql_config
import argparse
from db import populate_db
from transform import transform_menu, transform_outlet, transform_user, transform_review
from api import app
from db import db_proxy
from peewee import MySQLDatabase

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Mote Transform Parser')
    parser.add_argument('--host', dest='host', type=str, default='127.0.0.1', help='host for db')
    args = parser.parse_args()

    mysql_config.update({'host': args.host})

    db_proxy.initialize(MySQLDatabase(**mysql_config))

    populate_db(mysql_config, drop_exist=True)
    transform_outlet()
    transform_user()
    transform_review()
    transform_menu()

    app.run(host='0.0.0.0')

