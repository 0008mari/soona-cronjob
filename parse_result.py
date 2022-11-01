# -*- coding: utf-8 -*-

from json import load
import pandas as pd
import uuid
import datetime

def parse_result(event_dict, teacher_id, student_id, student_name):
    # input: dictionary
    # output: dictonary
    dict = event_dict['SchoolSchedule'][1]['row']
    test_df = pd.DataFrame(dict)
    
    df = test_df[['SCHUL_NM', 'AA_YMD', 'EVENT_NM']]
    no_events = df[df['EVENT_NM'].str.contains('영어듣기평가|재량휴업일|중간고사|기말고사|개학식|영어듣기|재량휴업|지필평가|고사|학력평가') == False].index
    # 시험만 넣고, 휴업일이나 방학식은 필요 없을 수 있다.
    df.drop(no_events, inplace=True, axis=0)
    
    column_list = ['event_id', 'start_date', 'event_type', 'teacher_id', 'student_id', 'student_name', 'event_name']
    load_df = pd.DataFrame(columns=column_list)
    load_df['event_id'] = df['AA_YMD'].apply(lambda _: uuid.uuid4().hex)
    load_df['start_date'] = df['AA_YMD'].map(parse_time) # df 순서 상 이게 먼저 와야됨 
    load_df['end_date'] = df['AA_YMD'].map(parse_end_time)
    load_df['event_type'] = '1'
    
    if teacher_id is not None:
        load_df['teacher_id'] = teacher_id.hex()
    else:
        load_df['teacher_id'] = ''
    if student_id is not None:
        load_df['student_id'] = student_id.hex()
    else:
        load_df['student_id'] = ''
    if student_name is not None:
        load_df['student_name'] = student_name
    else:
        load_df['student_name'] = ''
    
    load_df['event_name'] = df.apply(lambda r:r.SCHUL_NM+" "+r.EVENT_NM, axis=1)
    
    print(load_df)
    
    return load_df.copy()

# parse_result()

def name_apply(school_name, event_name):
    apply_name = school_name + " " + event_name
    return apply_name

def parse_time(date):
    return datetime.datetime.strptime(date, "%Y%m%d").strftime("%Y-%m-%d %H-%M-%S")

def parse_end_time(date):
    return (datetime.datetime.strptime(date, "%Y%m%d") + datetime.timedelta(hours=23, minutes=59, seconds=59)).strftime("%Y-%m-%d %H-%M-%S")