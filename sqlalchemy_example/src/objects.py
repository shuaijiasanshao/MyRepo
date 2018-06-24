# coding: utf-8
import models


class User(object):

    @staticmethod
    def insert(db_session, student):
        db_session.add_all(student)
        db_session.commit()

    @staticmethod
    def query_all(db_session):
        db_session.query(models.User).all()
