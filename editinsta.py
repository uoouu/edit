import requests,time,pytz
from datetime import datetime


timee = int(datetime.now().timestamp())

url = 'https://www.instagram.com/accounts/login/ajax/'

user = 'xtrrryuvr'
pas = '12345@00'
re = requests.Session()

r = re.get('https://www.instagram.com')
csrf = r.cookies['csrftoken']
print(csrf)
hed = { 
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
	'content-type': 'application/x-www-form-urlencoded',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-prefers-color-scheme': 'dark',
	'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	'viewport-width': '759',
	'x-asbd-id': '198387',
	'x-csrftoken': csrf,
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': 'hmac.AR1LV8rWWLK-ZXLT5rUxiXPuP3Mfwj4DRf3OZZ68uzx91ErT',
	'x-instagram-ajax': '2c4a166c736d',
	'x-requested-with': 'XMLHttpRequest'
}

data = {
	'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timee}:{pas}',
	'username': user,
	'queryParams': '{}',
	'optIntoOneTap': 'false',
	'stopDeletionNonce': '',
	'trustedDeviceRecords': '{}'
}

log = re.post(url,data=data,headers=hed)

if '"authenticated":true' in log.text:
	print('done login.')
	csrf2 = re.cookies['csrftoken']
	print(csrf2)
	urll = 'https://i.instagram.com/api/v1/web/accounts/edit/'
	sessi = re.cookies["sessionid"]
	print(sessi)

	hed2 = {
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
	'content-type': 'application/x-www-form-urlencoded',
	'cookie': f'sessionid={sessi}',
	'origin': 'https://www.instagram.com',
	'referer': 'https://www.instagram.com/',
	'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
	'x-asbd-id': '198387',
	'x-csrftoken': csrf2,
	'x-ig-app-id': '936619743392459',
	'x-ig-www-claim': 'hmac.AR1LV8rWWLK-ZXLT5rUxiXPuP3Mfwj4DRf3OZZ68uzx91ErT',
	'x-instagram-ajax': '1006149188' }
  
	while True:
		IST = pytz.timezone('Asia/Baghdad')
		ct = datetime.now(IST)
		tor1 = int(ct.strftime('%H'))
		if tor1 > 12:
			if tor1 == 13:
				tor1 = 1
			elif tor1 == 14:
				tor1 = 2
			elif tor1 == 15:
				tor1 = 3
			elif tor1 == 16:
				tor1 = 4
			elif tor1 == 17:
				tor1 = 5
			elif tor1 == 18:
				tor1 = 6
			elif tor1 == 19:
				tor1 = 7
			elif tor1 == 20:
				tor1 = 8
			elif tor1 == 21:
				tor1 = 9
			elif tor1 == 22:
				tor1 = 10
			elif tor1 == 23:
				tor1 = 11
			elif tor1 == 24:
				tor1 = 12
		elif tor1 < 13:
			tor1 = tor1
		tor2 = (ct.strftime('%M'))
		tor = f'{tor1}:{tor2}'
		pa = (ct.strftime('%p'))
		if pa == 'AM':
			po = 'صَ'
		elif pa == 'PM':
			po = 'مَ'
		bio = f'''‍ ‍ ‍ ‍
عيناك عليَّ ولا تراني - {tor} {po} -'''
		data2 = {
	'first_name': '',
	'email': 'aa846j13188@gmail.com',
	'username': 'xtrrryuvr',
	'phone_number': '',
	'biography': bio,
	'external_url': '',
	'chaining_enabled': 'on'}
		rd = requests.post(urll,headers=hed2,data=data2)
		if '"status":"ok"' in rd.text:
			print('done edit.')
		else:
			print('error edit.')
			print(rd.text)
		time.sleep(59)
else:
	print('error login.')
	print(log.text)
