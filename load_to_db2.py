# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
import pymysql
import pandas as pd
from secret import HOST
from secret import USER
from secret import PASSWORD
from secret import DATABASE

def load_to_db2(csv_path):
    
    # db 연결
    db_conn_str = r'mysql+pymysql://' + USER + ':' + PASSWORD + '@' + HOST + r'/' + DATABASE + "?local_infile=1"
    engine = create_engine(db_conn_str)
    
    Session = sessionmaker(engine)
    
    with Session() as session:

        # 기존 event 삭제
        session.execute("DELETE FROM dayevent WHERE event_type = 1")
        session.commit()
        
        # ubuntu 배포 시 `/r`로 변경 필요
        sql = r"LOAD DATA LOCAL INFILE '" + csv_path + r"' REPLACE INTO TABLE `dayevent` COLUMNS TERMINATED BY ',' LINES TERMINATED BY '\r\n' (@event_id, @start_date, @event_type, @teacher_id, @student_id, @student_name, @event_name, @end_date) SET event_id = UNHEX(@event_id), teacher_id = UNHEX(@teacher_id), student_id = UNHEX(@student_id), lecture_id = UNHEX(@lecture_id), start_date = STR_TO_DATE(@start_date, '%Y-%m-%d %H-%i-%S'), end_date = STR_TO_DATE(@end_date, '%Y-%m-%d %H-%i-%S'), event_type=@event_type, student_name=@student_name, event_name=@event_name"
        query = text(sql)
        
        print(query)
        session.execute(query)
        session.commit()
    
    engine.dispose()
    
    
    