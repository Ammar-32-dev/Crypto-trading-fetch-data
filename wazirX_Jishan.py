import requests
import sqlite3

url="https://api.wazirx.com/sapi/v1/tickers/24hr"

response=requests.get(url)
#print(response.text)

data=response.json()#jspn matalab list of dictianory
#print(data[0])
data2=data[11:20]#change these values to get new data everytime   
#print(data2)

with sqlite3.connect('wiz.db') as con:
    pass
con.execute('''create table if not exists crypto(
  symbol TEXT,  
  baseAsset TEXT,  
  quoteAsset TEXT,  
  openPrice  TEXT,  
  lowPrice TEXT,  
  highPrice TEXT,  
  lastPrice TEXT,  
  volume TEXT,  
  bidPrice TEXT,  
  askPrice TEXT,  
  at TEXT
);
''')
cur=con.cursor()

list1=[]

for a in data2:
    main_data=tuple(a.values())
    #print(main_data)
    list1.append(main_data)
cur.executemany("insert into crypto VALUES (?,?,?,?,?,?,?,?,?,?,?)",list1)
con.commit()



query=" SELECT * FROM crypto "
for row in con.execute(query):
    print(row)
