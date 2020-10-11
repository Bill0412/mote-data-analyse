from db import populate_db
from db import insert_outlet, get_outlet_by_id_outlet
from db import insert_user, get_user_by_name
from db import insert_review
from db import insert_menu
from db import db_proxy
from peewee import MySQLDatabase
import datetime
import argparse
import pycountry
import json

BASE_PATH = 'data/'
SUFFIX = '_clean_nan.json'

TRIPADVISOR_SOURCE = 'tripadvisor'
UBEREATS_SOURCE = 'ubereats'


def transform_outlet():
    ta_outlet = json.load(open(BASE_PATH + 'tripadvisor_outlet' + SUFFIX, 'r'))
    ue_outlet = json.load(open(BASE_PATH + 'ubereats_outlet' + SUFFIX, 'r'))

    for outlet in ta_outlet:
        data = {
            'id_outlet': outlet['id_outlet'],
            'name': outlet['name'],
            'source': TRIPADVISOR_SOURCE,
            'address': outlet['address'],
            'country': name_to_alpha_2(outlet['country']),
            'phone': outlet['phone'],
            'reviews_nr': outlet['reviews_nr']
        }

        insert_outlet(data)

    for outlet in ue_outlet:
        data = {
            'id_outlet': outlet['id_outlet'],
            'name': outlet['name'],
            'source': UBEREATS_SOURCE,
            'address': outlet['address'],
            'country': outlet['country'],
            'phone': '',
            'reviews_nr': outlet['reviews_nr']
        }
        insert_outlet(data)


def transform_user():
    users = json.load(open(BASE_PATH + 'tripadvisor_user' + SUFFIX, 'r'))

    for user in users:
        data = {
            'user': user['user'],
            'source': TRIPADVISOR_SOURCE,
            'likes': -1 if user['likes'] == '' else float(user['likes']),
            'reviews': user['reviews']
        }

        insert_user(data)


def transform_review():
    reviews = json.load(open(BASE_PATH + 'tripadvisor_reviews' + SUFFIX, 'r'))

    for review in reviews:
        data = {
            'user': get_user_by_name(review['user']),
            'outlet_id': get_outlet_by_id_outlet(review['id_outlet']),
            'date': convert_date(review['date']),
            'review': review['body'],
            'rating': review['rating']
        }
        insert_review(data)


def transform_menu():
    menus = json.load(open(BASE_PATH + 'ubereats_menu' + SUFFIX, 'r'))

    for menu in menus:
        data = {
            'outlet_id': get_outlet_by_id_outlet(menu['id_outlet']),
            'brand': menu['brand'],
            'price': menu['price'] if menu['price'] is not None else 0,
            'volume': -1 if menu['volume'] == 'unknown' else int(menu['volume']),
            'name': menu['name']
        }

        insert_menu(data)


def name_to_alpha_2(name: str) -> str:
    """
    :param name: country name(e.g. China, United States)
    :return: 2-char country name in lowercase(e.g. CN, US)
    """
    country = pycountry.countries.get(name=name)
    return country.alpha_2


def convert_date(date) -> str:
    """
    'January 15, 2018' => '2018-01-15'
    :param date: date in 'January 15, 2018' format
    :return: in the above example, returns '2018-01-15'
    """
    month_day, year = date.split(', ')
    month_raw, day_raw = month_day.split()
    month = str(datetime.datetime.strptime(month_raw, "%B").month).rjust(2, '0')
    day = day_raw.rjust(2, '0')
    return "{}-{}-{}".format(year, month, day)


if __name__ == '__main__':
    from config import mysql_config

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
