# -*- coding: utf-8 -*-
import requests
import json
from urllib.parse import urlencode

from secret import NEIS_API_KEY

def call_api(school_district_code, school_code):
    url_origin = "https://open.neis.go.kr/hub/SchoolSchedule?"
    params = {
        'KEY': NEIS_API_KEY,
        'Type': 'JSON',
        'pIndex': '1',
        'pSize': '1000',
        'ATPT_OFCDC_SC_CODE': school_district_code,
        'SD_SCHUL_CODE': school_code,
        'AA_FROM_YMD': 20220101,
        'AA_END_YMD': 20221231
        
    }
    query_string = url_origin + urlencode(params)
    answer = requests.get(query_string).text
    answer.encode("utf-8")
    # print(answer)
    
    dict = json.loads(answer)
    
    return dict
