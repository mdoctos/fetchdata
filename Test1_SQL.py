# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="root")
# my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE Employees")
# #my_cursor.execute("SHOW DATABASES")
#
# print("database created")
# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="root",database="Employees")
# my_cursor = mydb.cursor()

# my_cursor.execute("CREATE TABLE Employe(name VARCHAR(20) , EMP_Id VARCHAR(20))")


#from sqlalchemy import create_engine
import requests
import json
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
response = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
db = mysql.connector.connect(host='localhost',user='root', password='root', database='usa_data')
mycursor = db.cursor()

def addData(i):



    data = i['ID Nation'], i['Nation'], i['Year']
    sql = '''INSERT INTO data_usa(id, data, source) values(%s, %s, %s)'''
    mycursor.execute(sql, data)
    db.commit()

data=response.json()
data1=data['data']
for i in data1:
    addData(i)
# def jprint(obj):
#
#         text = json.dumps(obj, sort_keys=True, indent=4)
#         print(text)
#
# jprint(response.json())
# #
# list = json.loads(response.text)
#
# print(list)
# columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in list.keys())
# values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in list.values())
# sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('mytable', columns, values)
# print(sql)
#
# for i in response:
#     print(i)
#
#     sql = "INSERT INTO DATA_usa (ID Nation, Nation,ID Year,Year,Population,Slug Nation) VALUES (%s,%s, %s,%s,%s)"
#     mycursor = db.cursor()
#     mycursor.execute(sql, i)
#     db.commit()
#     print(mycursor.rowcount, "record inserted.")

#     if 'ID Nation' in i :
#         ID_nation=i['ID_nation']
#     else :
#         ID_nation=""
#
#     if ' Nation' in i :
#         Nation=i['Nation']
#     else :
#         Nation=""
#     if 'ID Year' in i :
#         ID_Year=i['ID_Year']
#     else :
#         ID_Year=""
#     if 'Year' in i :
#         Year=i['Year']
#     else :
#         Year=""
#     if 'Population' in i :
#         Population=i['Population']
#     else :
#         Population=""

print(addData)
# ?def addData():



# def jprint(obj):
#
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
#
#     jprint(response.json())


#mydb = mysql.connector.connect(host="localhost",user="root",password="root")

#df = pd.DataFrame(data,columns=['ID_Nation','Nation','ID_Year','Year','Population','SlugNation'])


#mycursor.execute("CREATE DATABASE USA_DATA")
# mydb = mysql.connector.connect(host='localhost',user='root', password='root', database='usa_data')
# mycursor.execute("CREATE TABLE DATA_usa(ID_Nation VARCHAR(255), Nation VARCHAR(255), ID_Year INT(255), Year INT(255), Population INT(255), SlugNation VARCHAR(255))")
#
#
# print(mydb)







# engine = create_engine('mysql+pymysql://{user}:{pw}@localhost/{db}'
#                        .format(user='root',
#                                pw='root',
#                                db='usa_data'))
# df.to_sql(con=engine, name='data_usa', if_exists='replace', index_label='id')