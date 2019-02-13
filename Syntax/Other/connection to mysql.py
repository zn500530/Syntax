import pandas as pd,os,tushare as ts,datetime,csv,time

pro=ts.pro_api()
from Personalkit import stock

#常用参数说明：

#    name:表名，pandas会自动创建表结构
#   con：数据库连接，最好是用sqlalchemy创建engine的方式来替代con
#   flavor:数据库类型 {‘sqlite’, ‘mysql’}, 默认‘sqlite’，如果是engine此项可忽略
#   schema:指定数据库的schema，默认即可
#   if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
#   index:将pandas的Index作为一列存入数据库，默认是True
#   index_label:Index的列名
#   chunksize:分批存入数据库，默认是None，即一次性全部写人数据库
#   dtype:设定columns在数据库里的数据类型，默认是None

#调用方法：

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Test123@127.0.0.1:3306/test')
# Create engine

# 管理connnection
#with engine.connect() as conn, conn.begin():
   # data = pd.read_sql_table('data', conn)

#输出到数据库表格中, Chunksiz可选参数,一次上传1000条记录, data 是在TEST SCHEMA里建立的TABLE名字, index=True将df的索引作为列写入TABLE里面去
data = ts.get_tick_data('600841', date='2018-12-28',src='tt')
data.to_sql('data', engine, chunksize=1000, index=True)
#df.to_sql('tick_data',engine,if_exists='append', ) #如果已存在该表格,指定处理方式' fail, replace and append

# 读取表格时，可以指定哪一列作为dataframe的索引,指定只显示Col_1,Col_2列, 将date列读取为日期,可以指定从哪个schema读取TABLE
#pd.read_sql_table('data', engine,index_col='id', schema='other_schema', columns=['Col_1', 'Col_2'],parse_dates=['Date']　or  parse_dates={'Date': '%Y-%m-%d'}, or  parse_dates={'Date': {'format': '%Y-%m-%d %H:%M:%S'}})

#读取sql query

pd.read_sql_query("SELECT id, Col_1, Col_2 FROM data WHERE id = 42;", engine)
#for chunk in pd.read_sql_query("SELECT * FROM data_chunks", engine, chunksize=5)

from pandas.io import sql
sql.execute('delete FROM tick_data', engine)
sql.execute('INSERT INTO table_name VALUES(?, ?, ?)', engine,
            params=[('id', 1, 12.2, True)])

#data_buy = pd.read_sql_query("SELECT * FROM realtime.data where 代码='%s' and 时间 between'%s'and '%s';"%(code,date_start,date_end),engine)
# $s 是对string  ,%d 是对int, %f是针对float

#D:\eastmoney\swc8\config\User\1680112946620416

