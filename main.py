from sqlalchemy.orm import Session,sessionmaker
import sqlalchemy as s
engine = s.create_engine('sqlite:///CmpTelega3.db', echo=True)
meta = s.MetaData()
session = Session(bind=engine)

UsersData = s.Table(
   'table1', meta,
   s.Column('id', s.Integer, primary_key=True,unique=True),
   s.Column('login', s.String),
   s.Column('password',s.String,unique=True)
)

UsersData2 = s.Table(
   'table2', meta,
   s.Column('id', s.Integer, primary_key=True,unique=True),
   s.Column('login', s.String),
   s.Column('password',s.String,unique=True)
)

UsersData3 = s.Table(
   'table3', meta,
   s.Column('id', s.Integer, primary_key=True,unique=True),
   s.Column('login', s.String),
   s.Column('password',s.String,unique=True)
)


meta.create_all(engine)