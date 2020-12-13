from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, desc, Table, Float, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

Base = declarative_base()

# 创建一个test_table类
class test_table(Base):
    __tablename__ = 'test'
    user_id = Column(Integer(), primary_key = True)
    user_name = Column(String(25), nullable = False, unique = True)
    age = Column(Integer(), nullable = False)
    birthday = Column(Date(), nullable = False)
    gender = Column(String(25), nullable = False)
    edu_degree = Column(String(25), nullable = False)
    created_on = Column(DateTime(), default = datetime.now)
    updated_on = Column(DateTime(), default = datetime.now,onupdate=datetime.now)
    def __repr__(self):
        return "test_table(user_id = '{self.user_id}', " \
            "user_name = '{self.user_name}', " \
            "age = '{self.age}', " \
            "birthday = '{self.birthday}', " \
            "gender = '{self.gender}', " \
            "edu_degree = '{self.edu_degree}', " \
            "created_on = '{self.created_on}', " \
            "updated_on = '{self.updated_on})'".format(self = self)
#数据库连接
dburl = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(
                                                                self.db_config['user_name'], 
                                                                self.db_config['password'], 
                                                                self.db_config['server'],
                                                                self.db_config['port'],
                                                                self.db_config['database'],
                                                                )
engine = create_engine(dburl, echo=True, encoding="utf-8")
    #进程函数创建
    #def init_session(self):
     #   SessionClass = sessionmaker(bind = self.engine)
      #  session = SessionClass()
       # return session
    #表函数创建
    #def create_table(self):
     #   try:
      #      Base.metadata.create_all(self.engine)
       # except Exception as e:
        #    sys.exit(e)
#插入操作
db = pymysql.connect("localhost","root", "root", "testdb")
try:
    sql = '''INSERT INTO test (user_id, user_name, age, birthday, gender, edu_degree, created_on, updated_on) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)'''
    values = (
        (1, 'Li Ming', 22, '1998-1-2', 'man',
         'University', datetime.now(), datetime.now()),
        (2, 'Li Hua', 25, '1995-2-3', 'men',
         'Master', datetime.now(), datetime.now()),
        (3, 'Li Hong', 30, '1990-3-4', 'women',
         'High School', datetime.now(), datetime.now())
    )
    with db.cursor() as cursor:
        cursor.executemany(sql, values)
    db.commit()
except Exception as e:
    print(f'Insert error: {e}')
#查询操作
try:
    sql = '''SELECT user_id, user_name, age, birthday, gender, edu_degree FROM test'''
    with db.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            print(result)
    db.commit()
except Exception as e:
    print(f'SELECT error: {e}')
finally:
    db.close()