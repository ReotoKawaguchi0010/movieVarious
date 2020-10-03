import sqlalchemy
import os
import platform

def get_path(db_name, file_name):
    path = os.getcwd()
    if 'Window' in platform.platform():
        if 'models' not in path:
            path = path + '\\models'
        if 'writing' in path:
            path = path + '\\writing'
        result = f'{db_name}:///{path}\\{file_name}.db'
    else:
        if 'models' not in path:
            path = path + '/models'
        if 'writing' not in path:
            path = path + '/writing'
        result = f'{db_name}:///{path}/{file_name}.db'
    return result

def engine(memory=False):
    if memory:
        engine = sqlalchemy.create_engine('sqlite:///:memory:')
        return engine
    engine = get_path('sqlite', 'writing')
    return sqlalchemy.create_engine(engine)