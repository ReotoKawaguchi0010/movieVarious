import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import logging
import traceback

import models.users.init

import utils.util as utils

engine = models.users.init.engine(memory=True)

Base = sqlalchemy.ext.declarative.declarative_base()

class Users(Base):
    __tablename__ = 'new_title'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    username = sqlalchemy.Column(sqlalchemy.String(40))
    password = sqlalchemy.Column(sqlalchemy.String(40))


class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = self.Session()

    def create_new_user(self, username, password):
        try:
            users = Users()
            users.username = str(username)
            users.password = utils.password_encode(str(password))
            self.session.add(users)
            self.session.commit()
        except:
            traceback.print_exc()
        finally:
            self.session.close()

    def read_users(self):
        try:
            read_contents = self.session.query(Users).all()
            contents = [utils.create_dict(username=read_content.username,
                                          password=read_content.password) for read_content in read_contents]
            return contents
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def delete_user(self, username):
        delete_content = self.session.query(Users).filter_by(username=username).first()
        self.session.delete(delete_content)
        self.session.commit()

    def read_user(self, username):
        read_users = self.read_users()
        for i in range(len(read_users)):
            if username == read_users[i]['username']:
                return read_users[i]
        return None



if __name__ == '__main__':
    op = UserOperation()
    op.create_new_user('test', 'test')
    print(op.read_users())


