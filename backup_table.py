# backup_table
import mysql.connector
from secret import HOST
from secret import USER
from secret import PASSWORD
from secret import DATABASE

def backup_table():
    
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        database=DATABASE
    )
    cur = mydb.cursor()
    
    sql1 = "DROP TABLE dayevent_copy;"
    cur.execute(sql1)
    mydb.commit()
    
    sql = "CREATE TABLE dayevent_copy (SELECT * FROM dayevent);"
    cur.execute(sql)
    
    mydb.commit()
    print("---")


if __name__ == "__main__":
    backup_table()