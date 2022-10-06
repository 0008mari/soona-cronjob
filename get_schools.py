import mysql.connector
from secrets import *
from secrets import HOST
from secrets import USER
from secrets import PASSWORD
from secrets import DATABASE;

def get_schools():
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        database=DATABASE
    )

    cur = mydb.cursor()
    cur.execute("SELECT C.*, S.tchr_id FROM school C INNER JOIN student S ON S.sch_id = C.sch_id")
    myresult = cur.fetchall()
    for x in myresult:
        print(x)

    cur.close()
    mydb.close()