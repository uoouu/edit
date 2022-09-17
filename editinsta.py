import requests,time,pytz
from datetime import datetime

IST = pytz.timezone('Asia/Baghdad')
ct = datetime.now(IST)
timee = int(datetime.now().timestamp())

url = 'https://www.instagram.com/accounts/login/ajax/'

user = 'nzosiebw'
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
		tor = (ct.strftime('%H:%M'))
		pa = (ct.strftime('%p'))
		if pa == 'AM':
			po = 'صَ'
		elif pa == 'PM':
			po = 'مَ'
		bio = f'''‍ ‍ ‍ ‍
عيناك عليَّ ولا تراني - {tor} {po} -'''
		data2 = {
	'first_name': '',
	'email': 'aa846513188@gmail.com',
	'username': 'nzosiebw',
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
