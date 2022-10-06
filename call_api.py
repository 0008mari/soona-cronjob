import requests
import json
from urllib.parse import urlencode

def call_api():
    url_origin = "https://open.neis.go.kr/hub/SchoolSchedule"
    params = {
        '': '',
    }
    query_string = url_origin + urlencode(params)
    