# -*- coding: utf-8 -*-
# main.py

from get_schools import get_schools
from call_api import call_api
from parse_result import parse_result
from save_as_csv import save_as_csv
from backup_table import backup_table
from load_to_db2 import load_to_db2
from datetime import datetime


def main():
    
    # 서치할 학교 목록 가져오기
    schools = get_schools()
    dt_string = datetime.now().strftime("%Y%m%d_%H%M%S").lstrip("0")
    csv_path = r"result_daily/" + "result_" + dt_string + ".csv"
    # backup_path = r"backup_daily/" + "backup_" + dt_string + ".csv"
    
    if schools is not None:
        for row in schools:
            # print(row)
            school_code, school_district_code, teacher_id, student_id, student_name = row[0], row[2], row[4], row[5], row[6]
            # api 콜
            event_dict = call_api(school_district_code, school_code)
            # 결과 파싱
            result_df = parse_result(event_dict, teacher_id, student_id, student_name)
            # csv에 덧붙이기 
            save_as_csv(result_df, csv_path)
            
        # table 백업
        backup_table()
        
        # DB 적재 
        load_to_db2(csv_path)


if __name__ == "__main__":
    main()