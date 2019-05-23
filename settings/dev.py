from .base import *

API_URL = 'http://localhost:58001'

DB = {
    'NAME'    : 'core',
    'USER'    : 'postgres',
    'PASSWORD': 'devpass',
    'HOST'    : 'localhost',
    'PORT'    : 5433
}

USER_AGENT = {
    'mobile': [
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X)' \
        'AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304' \
        'Safari/602.1',

        'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H)' \
        'AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile' \
        'Safari/534.30',

        'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M)' \
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile' \
        'Safari/537.36'
    ],
    'desktop': [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,' \
        'like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',

        'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML,' \
        'like Gecko) Chrome/51.0.2704.64 Safari/537.36',

        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9' \
        '(KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
    ]
}
