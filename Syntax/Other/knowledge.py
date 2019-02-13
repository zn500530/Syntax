#for file in files:
#df= pd.read_csv(path+'/'+file,encoding='gbk',parse_dates=[2],index_col=[2]) #读取每个文件进入dataframe,第三列交易日期解析日期， 并且设为行索引
#df2 = df.sort_index(ascending=True)
#listeddate = str((list(df2.index.values)[0]))[:10]  #取前10位数字,后面时间省略　　#将上市日期格式从timestampe2018-02-05 0:00: 00 转换成date
#stocknames.append(df.iat[-1,1]) 定位单元值并添加在列表最后
#stockcodes.append(df.iat[-1,0]) 定位单元值并添加在列表最后
#listdates.append(listeddate)
#data={'股票名称':stocknames,'股票代码':stockcodes,'上市日期': listdates } 创建一个dataframe
#df3=pd.DataFrame(data)

#df3=pd.DataFrame(df2,columns=['交易日期','股票名称','开盘价'])
#df3.to_csv(path2+'/test.csv',encoding='gbk') #导出文件
#f2.ix['2018-02'].to_csv(path2+'/test.csv',encoding='gbk') #导出文件
#a=len(df2['2018-02-03':'2018-02-26'].index)
#print(a)
#df2['2018-02-03':'2018-02-26'].to_csv(path2+'/test.csv',encoding='gbk') #导出文件
#df3=data[data['TS股票代码'].isin(ts_codes)] #提取当日涨停股的十大流通股东信息

#df2[date_start:date_end].to_csv(path2+'/test.csv',encoding='gbk') #导出文件

#for i,Dir in enumerate(Dirs):
#print(df.sort_index(ascending=True))#行索引升序排列
#df2=df.sort_index(ascending=True)#生成新dataframe
#print(list(df2.index>'2018-02-25'))
#print(df2[df2.index>'2018-02-25'])
#df3=df2[df2.index>'2018-02-25']
df = DataFrame({'name':['a','a','b','b'],'classes':[1,2,3,4],'price':[11,22,33,44]})

summary = pd.DataFrame(columns=['成交价格', '价格变动', '成交手', '成交金额(元)','流入金额(元)'])

sex = df.loc[(df.classes==1)&(df.name=='a'),'price'].values[0]

等到根据条件筛选后行所在索引的位置
base = df.index.get_indexer_for((df[df.A == 2].index))






import os,pandas as pd
path='F:/Run/dailydata/sz300542.csv'
df = pd.read_csv(path, encoding='gbk')
print(df.shape)
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.head(10))
print(df.tail(10))

if df.index.is_unique == True:  #此文件用于做数据清理,包括有无重复交易日期记录,
    continue
else:
    print(file + ': has duplicated data.')
    # print(df1.rename(columns={'交易日':'交易日数'}))
    # print(df1[(df1['涨停板数']>=6) &(df1['涨停板数']<10)])

print(df9.iloc[:, 0].size)
total = pd.Series(df.sum())  # 计算dataframe 各列总合
noofzhangting = int(total['是否涨停'])
noofdieting = int(total['是否跌停'])

df3 = df[df['是否跌停'] == 1]  # 选出所有跌停股票
df4 = df2[['股票代码', '股票名称', '交易日期', '新浪行业', '新浪概念', '新浪地域']]  # 选择涨停股票相关字段
a = set(list(df4['股票代码']))  # 当日涨停股票代码
b = set(list(df6['股票代码']))  # 如果没有zhangting.csv此处会发生错误,需要建一个含两列"股票代码""交易日期"的文件
zcodes = list(a - b)  # 剔除此前已涨停股票代码后,本次需要添加的涨停股票代码


import common

print('请输入命令选项:\n1)清洗代码\n2)增加当日新涨停股票\n3)归档当日股票数据到当月数据\n4)归档当日股票数据到历史数据')
commandoption=int(input())
while commandoption >0:
    if commandoption==1:
        inputfile='F:/Run/Input/original.csv'#存放要清洗的股票代码，代码必须放在第一列
        outputfile='F:/Run/Input/import.csv'#输出路径
        common.codecleanser(inputfile,outputfile)
    elif commandoption==2:
        sourcedir='F:/Run/download/temp'#某交易日期股票数据，可存放多日股票数据用于读取．
        sourcedir2='F:/Run/Input/zhangting.csv'#该文件包含某日期开始的过往涨停股票代码
        common.zhangting(sourcedir,sourcedir2)
    print('请再次输入命令选项:\n0)退出程序\n1)清洗代码\n2)增加当日新涨停股票\n3)归档当日股票数据到当月数据\n4)归档当日股票数据到历史数据')
    commandoption=int(input())

print('程序已退出')
