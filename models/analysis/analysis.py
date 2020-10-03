import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import logging
import traceback

import models.analysis.init

import utils.util

engine = models.analysis.init.engine(memory=True)

Base = sqlalchemy.ext.declarative.declarative_base()

class Character(Base):
    __tablename__ = 'character'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(40))
    character = sqlalchemy.Column(sqlalchemy.String(40))

class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = self.Session()

    def create_new_title(self, title, character):
        try:
            chara = Character()
            chara.title = str(title)
            chara.character = str(character)
            self.session.add(chara)
            self.session.commit()
        except:
            traceback.print_exc()
        finally:
            self.session.close()

    def read_titles(self):
        try:
            read_contents = self.session.query(Character).all()
            contents = [utils.util.create_dict(title=read_content.title,
                                                page_number=read_content.page_number) for read_content in read_contents]
            return contents
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def delete_title(self, id):
        delete_content = self.session.query(Character).filter_by(id=id).first()
        self.session.delete(delete_content)
        self.session.commit()


if __name__ == '__main__':
    op = UserOperation()
    op.create_new_title('test', 5)
    print(op.read_titles())