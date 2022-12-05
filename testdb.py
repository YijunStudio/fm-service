from dotenv import load_dotenv

load_dotenv('./.env')

import os
env = os.environ

from utils._database import DBInstance

if __name__ == '__main__':
    print('testdb')
    db_ins = DBInstance('postgres')
    print(db_ins)
    sql = """
    insert into floatingmusic.project(name) values('lingling-1207');
    insert into floatingmusic.topic(name, project_id) values('卡萨多大提琴无伴奏幻想曲第一乐章', 2),('阿连斯基钢琴三重奏No.1', 2),('拉尔森小协奏曲', 2),('皮亚佐拉四季', 2);
    """
    
    sql = """
    insert into floatingmusic.user(wx_openid, wx_phone) values('virtual_user', '19999999999')
    """
    sql = """
    insert into floatingmusic.key(name, topic_id) values('我emo了', 5),('上头', 5),('灵魂得到升华', 5),('扎劲', 5),('飘飘然', 5),('少女心泛滥', 5),('温暖', 5),('冷酷', 5),('好吃', 5),('来自呼和浩特的草原', 5),('来自喜马拉雅的泉水', 5),('是心动的感觉', 5),('勇者斗恶龙', 5),('elegant！', 5);
    insert into floatingmusic.key(name, topic_id) values('我emo了', 6),('上头', 6),('灵魂得到升华', 6),('扎劲', 6),('飘飘然', 6),('少女心泛滥', 6),('温暖', 6),('冷酷', 6),('好吃', 6),('来自呼和浩特的草原', 6),('来自喜马拉雅的泉水', 6),('是心动的感觉', 6),('勇者斗恶龙', 6),('elegant！', 6);
    insert into floatingmusic.key(name, topic_id) values('我emo了', 7),('上头', 7),('灵魂得到升华', 7),('扎劲', 7),('飘飘然', 7),('少女心泛滥', 7),('温暖', 7),('冷酷', 7),('好吃', 7),('来自呼和浩特的草原', 7),('来自喜马拉雅的泉水', 7),('是心动的感觉', 7),('勇者斗恶龙', 7),('elegant！', 7);
    insert into floatingmusic.key(name, topic_id) values('我emo了', 8),('上头', 8),('灵魂得到升华', 8),('扎劲', 8),('飘飘然', 8),('少女心泛滥', 8),('温暖', 8),('冷酷', 8),('好吃', 8),('来自呼和浩特的草原', 8),('来自喜马拉雅的泉水', 8),('是心动的感觉', 8),('勇者斗恶龙', 8),('elegant！', 8);
    """
    rawsql = """
    select * from floatingmusic.view_topic
    """
    # print(db_ins.mutate(sql))
    print(db_ins.query(['_id'], 'floatingmusic.topic'))
    print(db_ins.query_by_rawsql(rawsql))