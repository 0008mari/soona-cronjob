import mysql.connector
from secrets import *

from secrets import HOST

from secrets import USER

from secrets import PASSWORD

from secrets import DATABASE;

mydb = mysql.connector.connect(
    host=HOST,
    user=USER,
    passwd=PASSWORD,
    database=DATABASE
)

cur = mydb.cursor()
cur.execute("select * from teacher")
myresult = cur.fetchall()
for x in myresult:
    print(x)