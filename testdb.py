from dotenv import load_dotenv

load_dotenv('./.env')

import os
env = os.environ

from utils._database import DBInstance

if __name__ == '__main__':
    print('testdb')
    db_ins = DBInstance('postgres')
    print(db_ins)
    print(db_ins.mutate('select * from floatingmusic.user'))
    print(db_ins.query(['_id', 'wx_nickname'], 'floatingmusic.user'))