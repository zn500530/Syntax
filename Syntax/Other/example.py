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
1 建立dataframe
df = DataFrame({'name':['a','a','b','b'],'classes':[1,2,3,4],'price':[11,22,33,44]})
summary = pd.DataFrame(columns=['成交价格', '价格变动', '成交手', '成交金额(元)','流入金额(元)'])

2 是否存在文件
if os.path.exists(sourcefile) == True:

3 连接两个list
codes = codes + list(df['股票代码'])



sex = df.loc[(df.classes==1)&(df.name=='a'),'price'].values[0]

等到根据条件筛选后行所在索引的位置
base = df.index.get_indexer_for((df[df.A == 2].index))

df3.set_axis(range(1, len(stockcode) + 1), axis=0, inplace=True)  # 在原DATAFRAME中直接修改行索引的编号,起始值为1

df3=data[data['TS股票代码'].isin(ts_codes)] #提取当日涨停股的十大流通股东信息
df4=df3.groupby(['股东名称'])['股东名称'].agg('count').sort_values(ascending=False)[:5]
print(df4,df3[df3['股东名称'].isin(df4.index)])


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


oldfile=os.listdir(path4)
print(oldfile)
for eachfile in oldfile:
    os.unlink(path4+'/'+eachfile)
df=pd.read_csv(path3,encoding='gbk',index_col=['股票代码'])
df1=pd.read_csv(path2,encoding='gbk',index_col=['代码'])


file=csv.reader(open(path))
for i,eachblock in enumerate(file):   #每个板块代码及包含的股票代码
    stockcode = []
    stockprirange = []
    blockcode=eachblock[0]   #板块代码在首位
    stocks=eachblock[1:]     #板块所在股票代码的集合
    try:
        blockname=list(df1.loc[int(blockcode)])[-1]   #block是str 类型,index是整数,因此要转换下
    except:
        continue
    for eachstock in stocks:  #遍历板块中每个股票
        try:
            pricerange=list(df.loc[eachstock.lower()])[-3]   # 1)股票名称都小写2)条件: dataframe中等于股票代码所在的行 3) 提取该行所在最后一列即区间涨跌幅
            stockprirange.append(pricerange)  #添加到stockprirange列表
            stockcode.append(eachstock)   #添加到stockname列表,位置对应相应的stockprirange
        except:
            continue
    collection={'股票代码':stockcode,'区间涨跌幅':stockprirange}
    obj=pd.DataFrame(collection,columns=['股票代码','区间涨跌幅'],)
    obj2=obj.sort_values(by='区间涨跌幅',ascending=False )
    obj2.set_axis(range(1,len(stockcode)+1), axis=0, inplace=True)   #在原DATAFRAME中直接修改行索引的编号,起始值为1
    obj2['板块']=blockname
    obj2.index.name='Seq No'
    #obj2.head(10).to_csv(path4 + '/'+blockname+'.csv', encoding='gbk')
    try:
        obj2.to_csv(path4 + '/' + blockname + '.csv', encoding='gbk')
    except:
        print(i,blockcode)
print(i)

stock_in_block = list(data['股票代码'])
stockcode = []
stockname = []
stockprirange = []
print(eachblock, stock_in_block, len(stock_in_block))
for eachstock in stock_in_block:  # 对于每个板块中的股票从阶段涨幅值文件中拿到阶段涨幅值
    try:
        pricerange = list(df2.loc[eachstock.lower()])[-3]  # 1)股票名称都小写2)条件: dataframe中等于股票代码所在的行 3) 提取该行所在倒数第3列即区间涨跌幅
        stockname = list(df2.loc[eachstock.lower()])[1]  # 提取该股票名称
        stockprirange.append(pricerange)  # 添加到stockprirange列表
        stockcode.append(eachstock)  # 添加到stockcode列表,位置对应相应的stockprirange
        stockname.append(stockname)  # 添加到stockname列表,位置对应相应的stockprirange
    except:
        print(str(eachstock) + 'has no trading days during the period')
        continue

# 建立一个dataframe
collection = {'股票代码': stockcode, '股票名称': stockname, '区间涨跌幅': stockprirange}
obj = pd.DataFrame(collection, columns=['股票代码', '股票名称', '区间涨跌幅'], )

#这样的填空题会让我们印象深刻，当字符串中有多个这样的“空”需要填写的时候，我们可以使用.format（）进行批处理，它的基本使用方法有如下几种，输入代码
print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))

city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)

counter += 1
if counter >= 75:
    print('休息一下:' + str(counter))
    time.sleep(55)
    counter = 0

    # code='300232.SZ'
    # df = pro.balancesheet(ts_code=code,period=each_period, fields='ts_code,ann_date,f_ann_date,end_date,report_type,notes_receiv,accounts_receiv,prepayment,inventories,lt_rec,fix_assets,cip,notes_payable,acct_payable,adv_receipts,lt_payable')
    # df.fillna('NULL',inplace=True)
    # for i in range(5,df.columns.size):
    #   try:
    #      df.ix[:,i]=df.ix[:,i].apply(lambda x: round(x/10000,2))
    # except:
    #    print(str(i)+'has null value')
    #   continue
    # df.to_csv('F:/Run/Output/balancesheet.csv',encoding='gbk' )


import pandas as pd,numpy as np,os,csv

path='F:/Run/dailydata'
path2='F:/Run/Output/Statistic'
if os.path.exists(path2+'/magicdata.csv')==True:
   os.unlink(path2+'/magicdata.csv')

files = os.listdir(path)  # 遍历该文件夹下所有文件
for i,file in enumerate(files):
    df = pd.read_csv(path + '/' + file, encoding='gbk', parse_dates=[2],index_col=[2])  # 读取每个文件进入dataframe,第三列交易日期解析日期， 并且设为行索引
    df2 = df.sort_index(ascending=True)
    stockcode = list(df2['股票代码'])[-1]
    stockname = list(df2['股票名称'])[-1]
    lowestprice=min(df['最低价'])
    highestprice=max(df['最高价'])
    newestprice=df.iat[-1,8]  #由于交易日期设为index,所以第9列为收盘价
    multiple=newestprice//lowestprice   #取倍数
    goldenfigure=[0,0.25,0.33,0.372,0.5,0.618,0.66,0.75,1]
    newgoldenfigure=np.array(goldenfigure)+multiple       #根据当前价计算出适用的倍数系数
    targetprice=(lowestprice*newgoldenfigure).tolist()      #根据百分比计算出当前的支撑位和压力位,
    for b in range(len(targetprice)):
        targetprice[b]=round(targetprice[b],2)
    pricediff=round(highestprice - lowestprice)
    targetprice2=(np.array(goldenfigure[0:])*pricediff+lowestprice).tolist()  #计算出历史最高价和最低价之间差异保留两位小数,保留两位小数
    for b in range(len(targetprice2)):
        targetprice2[b] = round(targetprice2[b], 2)

    position=0 # 计算当前最新价在黄金数字序列1中的位置
    for i in range(8):
        if newestprice > targetprice[i] and newestprice > targetprice[i+1]:
            position+= 1
            if position < 8:
               continue
            else:
               position+=1
        elif newestprice >= targetprice[i] and  newestprice < targetprice[i+1]:
            position=i+1
            profit_percent=round((targetprice[i+1]-newestprice)/newestprice*100,2)  # 当前价距离压力位的盈利百分比
            loss_percent=round((newestprice-targetprice[i])/newestprice*100,2) # 当前价距离支撑位的亏损百分比
            break

    position1=0 # 计算当前最新价在黄金数字序列2中的位置
    for a in range(8):
        if newestprice > targetprice2[a] and newestprice > targetprice2[a + 1]:
            position1 += 1
            if position1 < 8:
                continue
            else:
                position1 += 1
        elif newestprice >= targetprice2[a] and newestprice < targetprice2[a + 1]:
            position1 = a + 1
            break
    header=['股票代码','股票名称','当日最新价','序列1位置','序列2位置','黄金数字序列1(0,0.25,0.33,0.372,0.5,0.618,0.66,0.75,1)','盈利百分比(％)','亏损百分比（％）','黄金数字序列2']
    summary=[stockcode,stockname,newestprice,position,position1]
    summary.append(targetprice)
    summary.append(profit_percent)
    summary.append(loss_percent)
    summary.append(targetprice2)
    if os.path.exists(path2+'/magicdata.csv') == True:  # 如果该股票文件存在,则打开此文件并添加该行
        targetfile = open(path2+'/magicdata.csv', 'a', newline='', encoding='gbk')  # 以添加模式写入文件
        targesinglefile = csv.writer(targetfile)
        targesinglefile.writerow(summary)
        targetfile.close()
    else:  # 如果该股票文件不存在,则建立此文件写入header,并添加数据
        targetfile = open(path2+'/magicdata.csv', 'w', newline='', encoding='gbk')  # 以覆盖模式写入文件
        targesinglefile = csv.writer(targetfile)
        targesinglefile.writerow(header)
        targesinglefile.writerow(summary)
        targetfile.close()
