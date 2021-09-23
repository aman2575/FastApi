from sqlalchemy import create_engine, MetaData

meta =  MetaData()
engine = create_engine("mysql+pymysql://root@localhost:3306/test")


conn =  engine.connect()