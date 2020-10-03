import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm
import logging
import traceback

import models.writing.init
import models.writing.letter_body

import utils.util

engine = models.writing.init.engine(memory=False)

Base = sqlalchemy.ext.declarative.declarative_base()

class NewTitle(Base):
    __tablename__ = 'new_title'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(40))
    author = sqlalchemy.Column(sqlalchemy.String(20))


class UserOperation(object):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.Session = sqlalchemy.orm.sessionmaker(bind=engine)
        self.session = self.Session()

    def create_new_title(self, title, author):
        try:
            new_title = NewTitle()
            new_title.title = str(title)
            new_title.author = str(author)
            self.session.add(new_title)
            self.session.commit()
        except:
            traceback.print_exc()
        finally:
            self.session.close()

    def read_titles(self):
        try:
            read_contents = self.session.query(NewTitle).all()
            contents = [utils.util.create_dict(id=read_content.id,
                                               title=read_content.title,
                                               author=read_content.author) for read_content in read_contents]
            return contents
        except:
            logging.error('fail')
        finally:
            self.session.close()

    def delete_title(self, title):
        delete_content = self.session.query(NewTitle).filter_by(title=title).first()
        self.session.delete(delete_content)
        self.session.commit()

    def read_title_name(self, title_name):
        read_titles = self.read_titles()
        for i in range(len(read_titles)):
            if title_name == read_titles[i]['title']:
                return read_titles[i]
        return None

    def read_title_id(self, id):
        read_titles = self.read_titles()
        for i in range(len(read_titles)):
            if id == read_titles[i]['id']:
                return read_titles[i]
        return None



if __name__ == '__main__':
    op = UserOperation()
