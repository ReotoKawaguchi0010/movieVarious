import sqlalchemy
import os

def get_path(db_name, file_name):
    path = os.getcwd()
    if 'models' not in path:
        path = path + '/models'
    if 'analysis' not in path:
        path = path + '/analysis'

    result = f'{db_name}:///{path}/{file_name}.db'

    return result

def engine(memory=False):
    if memory:
        engine = sqlalchemy.create_engine('sqlite:///:memory:')
        return engine
    engine = get_path('sqlite', 'analysis')
    return sqlalchemy.create_engine(engine)