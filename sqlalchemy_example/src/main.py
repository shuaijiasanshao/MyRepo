# coding: utf-8

import datetime
import random
import uuid

from db import UserDB


NAME = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz"
NAME_LENGTH = 10
AGE_MIN = 10
AGE_MAX = 30
SCORE_MIN = 30
SCORE_MAX = 100
SEX = ["F", "M"]
USER_FIELDS = ['id', 'name', 'sex', 'age', 'create_at']


class GenerateStudent(object):

    @staticmethod
    def generate_id():
        return uuid.uuid4()

    @staticmethod
    def generate_name():
        return "".join([random.choice(NAME) for _ in range(NAME_LENGTH)])

    @staticmethod
    def generate_age():
        return random.randint(AGE_MIN, AGE_MAX)

    @staticmethod
    def generate_sex():
        return random.choice(SEX)

    @staticmethod
    def generate_create_at():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def generate_user_info():
    return {field: getattr(GenerateStudent, 'generate_%s' % field)() for field in USER_FIELDS}


def add_user(db_op, nums=100):
    user = [generate_user_info() for _ in range(nums)]
    print user
    db_op.insert(user)


def prep_db():
    user_db = UserDB()
    try:
        user_db.init_conn()
    except Exception as e:
        print(e)
        user_db.release_conn()
        user_db = None
    return user_db


def main():
    db_op = prep_db()
    if db_op is not None:
        add_user(db_op, 1)


if __name__ == '__main__':
    main()
