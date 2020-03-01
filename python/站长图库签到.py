#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import time

cookies_a = ''
cookies_b = ''

cookie_lists={cookies_a,cookies_b}

for cookie in cookie_lists:
	headers = {
		'referer': 'https://www.zztuku.com/Index-index.html',
		'cookie': 'cookie',
		'dnt': '1',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'x-requested-with': 'XMLHttpRequest',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
	}
	url = 'https://www.zztuku.com/member-signin.html'
	response = requests.get(url=url, headers=headers)
	response.encoding = 'ascii'
	msg = response.text.encode().decode('unicode-escape')
	
	with open('/home/py/zztu/log.text', 'a') as log:
		now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		log.write('{} --- {}\n'.format(now,msg))
		log.close
	
