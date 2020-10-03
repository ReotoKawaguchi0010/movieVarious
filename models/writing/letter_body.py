import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import logging
import traceback

import models.writing.init
import models.writing.character
import models.writing.work

import utils.util

engine = models.writing.init.engine(memory=False)

Base = sqlalchemy.ext.declarative.declarative_base()

class LetterBody(Base):
    __tablename__ = 'letter_body'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.Integer)
    page_number = sqlalchemy.Column(sqlalchemy.Integer)
    letter_body = sqlalchemy.Column(sqlalchemy.String(1000))
    character = sqlalchemy.Column(sqlalchemy.Integer)


class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = self.Session()

    def create_new_letter_body(self, title, page_number, letter_body, character):
        try:
            page_num = LetterBody()
            page_num.title = str(title)
            page_num.page_number = int(page_number)
            page_num.letter_body = str(letter_body)
            page_num.character = int(character)

            self.session.add(page_num)
            self.session.commit()
        except:
            traceback.print_exc()
        finally:
            self.session.close()

    def read_titles(self):
        try:
            read_contents = self.session.query(LetterBody).all()
            contents = [utils.util.create_dict(id = read_content.id,
                                               title=read_content.title,
                                               page_number=read_content.page_number,
                                               letter_body=read_content.letter_body,
                                               character=read_content.character) for read_content in read_contents]
            return contents
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def read_title(self, title):
        read_titles = self.read_titles()
        for i in range(len((read_titles))):
            if read_titles[i]['title'] == title:
                return read_titles[i]
        return None

    def read_id(self, title):
        read_titles = self.read_titles()
        for i in range(len(read_titles)):
            if read_titles[i]['title'] == title:
                return i + 1
        return None

    def update_letter_body(self, title, update_contents):
        update_obj = self.read_id(title)
        t = self.session.query(LetterBody).get(update_obj)
        t.letter_body = update_contents
        self.session.add(t)
        self.session.commit()

    def delete_letter_body(self, id):
        delete_content = self.session.query(LetterBody).filter_by(id=id).first()
        self.session.delete(delete_content)
        self.session.commit()


if __name__ == '__main__':
    op = UserOperation()
    print(op.read_title(1))