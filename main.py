import requests
import time

url = 'https://api.telegram.org/bot1224151682:AAHih_OGH--dTZxL-SR4lcZZbpEYXZA1SMg/'


def get_updates_json(request):
	response = requests.get(request + 'getUpdates')
	return response.json()


def last_update(data):
	results = data['result']
	total_updates = len(results) - 1
	return results[total_updates]


def get_chat_id(update):
	chat_id = update['message']['chat']['id']
	return chat_id


def get_text(request):
	return last_update(request)['message']['text']


def send_mess(chat, text):
	params = {'chat_id': chat, 'text': text}
	response = requests.post(url + 'sendMessage', data=params)
	return response


key = True
run = True
cur_num = len(get_updates_json(url)['result'])
data = [{'user': '0', 'text': '0'}]
while run:
	request = get_updates_json(url)
	if len(request['result']) > cur_num:
		cur_num = len(request['result'])
		data.append([{'user': last_update(request)['message']['from']['username'], 'text': get_text(request)}])
		print(data)
		if get_text(request) == 'show':
			ans = ''
			for i in range(len(data)):
				ans += str(data[i]) + '\n'
			send_mess(get_chat_id(last_update(request)), ans)
		if get_text(request) == 'stop':
			run = False
			send_mess(get_chat_id(last_update(request)), 'I am dying')
