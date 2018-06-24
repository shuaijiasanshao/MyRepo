# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import models
import objects


CONN = "mysql+mysqlconnector://root:test@localhost:3306/test"


class BaseDB(object):

    def __init__(self, conn):
        self.conn = conn
        self.engine = None
        self.db_session = None
        self.metadata = None

    def init_conn(self):
        try:
            self.engine = create_engine(self.conn, echo=True)
            session = sessionmaker(bind=self.engine)
            self.db_session = session()
            self.metadata = models.Base.metadata
        except Exception:
            self.release_conn()
            raise Exception("init connection failed")

    def release_conn(self):
        if self.db_session:
            self.db_session.close()
        self.engine = None
        self.db_session = None

    def insert(self, info):
        raise NotImplementedError

    def query_all(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def delete(self, user_id):
        raise NotImplementedError


class UserDB(BaseDB):
    
    def __init__(self, conn=CONN):
        super(UserDB, self).__init__(conn)
    
    def insert(self, user_infoes):
        user_objs = []
        for user_info in user_infoes:
            student = models.User()
            for key, value in user_info.iteritems():
                setattr(student, key, value)
            user_objs.append(student)
        import pdb
        pdb.set_trace()
        objects.User.insert(self.db_session, user_objs)

    def query_all(self):
        return objects.User.query_all()

    def update(self):
        pass

    def delete(self, user_id):
        pass
