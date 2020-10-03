import ast
import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import logging
import traceback
import json

import models.writing.init
import models.writing.work

import utils.util

engine = models.writing.init.engine(memory=False)

Base = sqlalchemy.ext.declarative.declarative_base()

class Character(Base):
    __tablename__ = 'character'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True)
    character = sqlalchemy.Column(sqlalchemy.String(40))
    title = sqlalchemy.Column(sqlalchemy.Integer)

class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = self.Session()

    def create_new_character(self, character, title):
        try:
            chara = Character()
            chara.character = str(character)
            chara.title = str(title)
            self.session.add(chara)
            self.session.commit()
        except:
            traceback.print_exc()
        finally:
            self.session.close()

    def read_characters(self):
        try:
            read_contents = self.session.query(Character).all()
            contents = [utils.util.create_dict(id=read_content.id,
                                               character=read_content.character,
                                               title=read_content.title) for read_content in read_contents]
            return contents
        except:
            logging.error('fail')
        finally:
            self.session.close()


    def delete_character(self, id):
        delete_content = self.session.query(Character).filter_by(id=id).first()
        self.session.delete(delete_content)
        self.session.commit()

    def update_character(self, title, update_contents):
        update_obj = self.read_character_title(title)
        t = self.session.query(Character).get(update_obj)
        t.character = update_contents
        self.session.add(t)
        self.session.commit()

    def read_character_id(self, id):
        read_contents = self.read_characters()
        for i in range(len(read_contents)):
            if id == read_contents[i]['id']:
                return read_contents[i]
        return None

    def read_character_name(self, character):
        read_contents = self.read_characters()
        for i in range(len(read_contents)):
            if character == read_contents[i]['character']:
                return read_contents[i]
        return None

    def read_character_title(self, title):
        read_contents = self.read_characters()
        for i in range(len(read_contents)):
            if title == read_contents[i]['title']:
                return read_contents[i]['id']
        return None


if __name__ == '__main__':
    op = UserOperation()
    print(op.read_character_id(1))
