# -*- coding: utf-8 -*-
import mysql.connector
from secret import *
from secret import HOST
from secret import USER
from secret import PASSWORD
from secret import DATABASE

def get_schools():
    # input: none
    # output: list of tuples
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        database=DATABASE
    )

    cur = mydb.cursor()
    cur.execute("SELECT C.*, S.tchr_id, S.stu_id, S.stu_name FROM school C INNER JOIN student S ON S.sch_id = C.sch_id")
    myresult = cur.fetchall()

    cur.close()
    mydb.close()
    
    return myresult

