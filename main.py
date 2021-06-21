import time
from config import bot, admins, SECRET_P2P, WORKER_ACCESS, P2P_COMMENT, worker_p2p_text, \
	profile_text, statistics_text, worker_manuals_text, worker_add_mamont_text
from keyboard import main_keyboard, p2p_deposit_keyboard, del_msg_keyboard, worker_menu_keyboard, \
	back_to_main_keyboard, back_to_worker_keyboard, data_keyboard, back_to_data_keyboard, \
	qiwi_keyboard, admin_menu_keyboard
from functions import get_user, add_user_to_db, get_worker, add_worker_to_db, gen_random_string, \
	registration_1, output1, qiwi_balance, qiwi_number, upd_token, give_work_access_1, \
	mailing_to_workers_1, mailing_to_mamonts_1, send_message_1, take_work_access_1
from p2p_pay import get_p2p_payment_url, check_p2p_payment

@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user == None:
		if len(message.text.split(" ")) > 1:
				boss_id = message.text.split(" ")[1]
				boss_profile = get_user(boss_id)
				if boss_profile == None:
					boss_id = admins[0]
				else:
					bot.send_message(chat_id=boss_id,
				 				text=f"<b>馃帀 <a href='tg://user?id={chat_id}'>袦邪屑芯薪褌</a> 蟹邪褕褢谢 锌芯 胁邪褕械泄 褉械褎械褉邪谢褜薪芯泄 褋褋褘谢泻械.</b>",
				  				parse_mode="HTML")
		else:
			boss_id = admins[0]
		add_user_to_db(chat_id, boss_id)
	
	bot.send_message(chat_id=chat_id,
			text="<b>馃挵 袩芯谢褍褔懈褌械 锌褉褟屑芯 褋械泄褔邪褋 1220 褉褍斜谢械泄! 袧邪卸屑懈褌械 薪邪 泻薪芯锌泻褍 '袪械谐懈褋褌褉邪褑懈褟'</b>",
			reply_markup=main_keyboard(),
			parse_mode="HTML")

@bot.message_handler(commands=['worker'])
def worker_menu(message):
	chat_id = message.chat.id
	worker = get_worker(chat_id)
	if worker == None:
		bill_id = gen_random_string(16)
		url = get_p2p_payment_url(SECRET_P2P, bill_id, WORKER_ACCESS, P2P_COMMENT)
		bot.send_message(chat_id=chat_id,
			text=worker_p2p_text(),
			reply_markup=p2p_deposit_keyboard(bill_id, url),
			parse_mode="HTML")
	else:
		bot.send_message(chat_id=chat_id,
					text="袙褘 锌械褉械褕谢懈 胁 屑械薪褞 胁芯褉泻械褉邪",
					reply_markup=worker_menu_keyboard(),
					parse_mode="HTML")

@bot.message_handler(commands=['admin'])
def admin_menu(message):
	chat_id = message.chat.id
	if chat_id in admins:
		bot.send_message(chat_id=chat_id,
					text="袙褘 锌械褉械褕谢懈 胁 屑械薪褞 邪写屑懈薪邪",
					reply_markup=admin_menu_keyboard(),
					parse_mode="HTML")

@bot.message_handler(content_types="text")
def get_text_message(message, *args):
	chat_id = message.chat.id
	user = get_user(chat_id)
	if user == None:
		bot.send_message(chat_id=chat_id,
			text="<b>携 胁邪褋 薪械 锌芯薪懈屑邪褞! 袩褉芯锌懈褕懈褌械 /start.</b>",
			reply_markup=main_keyboard(),
			parse_mode="HTML")
	else:
		bot.send_message(chat_id=chat_id,
				text="<b>馃挵 袩芯谢褍褔懈褌械 锌褉褟屑芯 褋械泄褔邪褋 1220 褉褍斜谢械泄! 袧邪卸屑懈褌械 薪邪 泻薪芯锌泻褍 '袪械谐懈褋褌褉邪褑懈褟'</b>",
				reply_markup=main_keyboard(),
				parse_mode="HTML")



@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	chat_id = call.message.chat.id
	first_name = call.message.chat.first_name
	last_name = call.message.chat.last_name
	fullname = f"{first_name} | {last_name}"
	message_id = call.message.message_id
	message = call.message
	
	if call.data == "register":
		bot.delete_message(chat_id=chat_id, message_id=message_id)
		bot.send_message(chat_id=chat_id,
					text="<b>袙胁械写懈褌械 褋胁芯泄 薪芯屑械褉 QIWI 泻芯褕械谢褜泻邪(褌芯谢褜泻芯 褑懈褎褉褘).</b>",
		       		reply_markup=back_to_main_keyboard(),
		       		parse_mode="HTML")
		bot.register_next_step_handler(message, registration_1)

	elif call.data == "profile":
		bot.delete_message(chat_id=chat_id, message_id=message_id)
		bot.send_message(chat_id=chat_id,
					text=profile_text(chat_id),
		       		reply_markup=back_to_main_keyboard(),
		       		parse_mode="HTML")
		
	elif call.data == "statistics":
		bot.delete_message(chat_id=chat_id, message_id=message_id)
		bot.send_message(chat_id=chat_id,
					text=statistics_text(),
		       		reply_markup=back_to_main_keyboard(),
		       		parse_mode="HTML")
		
	elif call.data == "back_to_main":
		bot.delete_message(chat_id=chat_id, message_id=message_id)
		bot.send_message(chat_id=chat_id,
			text="<b>馃挵 袩芯谢褍褔懈褌械 锌褉褟屑芯 褋械泄褔邪褋 1220 褉褍斜谢械泄! 袧邪卸屑懈褌械 薪邪 泻薪芯锌泻褍 '袪械谐懈褋褌褉邪褑懈褟'</b>",
			reply_markup=main_keyboard(),
			parse_mode="HTML")
	
	elif call.data.startswith("check_p2p_deposit"):
		bill_id = call.data.split(":")[1]
		payment = check_p2p_payment(bill_id, SECRET_P2P)
		if payment["status"]["value"] == "PAID":
			bot.delete_message(chat_id=chat_id, message_id=message_id)
			add_worker_to_db(chat_id)
			bot.send_message(chat_id, f"<b>袙褘 褍褋锌械褕薪芯 锌芯谢褍褔懈谢懈 写芯褋褌褍锌 泻 锌邪薪械谢懈.</b>",
		       		reply_markup=del_msg_keyboard(),
		       		parse_mode="HTML")
		else:
			bot.send_message(chat_id, f"<b>鉂� 袩谢邪褌械卸 薪械 薪邪泄写械薪!</b>",
		       		reply_markup=del_msg_keyboard(),
		       		parse_mode="HTML")

	elif call.data == "delete_message":
		bot.delete_message(chat_id=chat_id, message_id=message_id)

	elif call.data == "reject_p2p_payment":
		bot.delete_message(chat_id=chat_id, message_id=message_id)
		bot.send_message(chat_id, f"<b>袩谢邪褌械卸 褍褋锌械褕薪芯 芯褌屑械薪褢薪.</b>",
		       		parse_mode="HTML")

	elif call.data == "admin_give_access" and chat_id in admins:
		bot.send_message(chat_id, f"<b>袙胁械写懈褌械 邪泄写懈 锌芯谢褜蟹芯胁邪褌械谢褟.</b>",
		       		parse_mode="HTML")
		bot.register_next_step_handler(message, give_work_access_1)

	elif call.data == "admin_worker_mailing" and chat_id in admins:
		bot.send_message(chat_id, f"<b>袙胁械写懈褌械 褌械泻褋褌 褉邪褋褋褘谢泻懈.</b>",
		       		parse_mode="HTML")
		bot.register_next_step_handler(message, mailing_to_workers_1)

	elif call.data == "admin_take_access" and chat_id in admins:
		bot.send_message(chat_id, f"<b>袙胁械写懈褌械 邪泄写懈 锌芯谢褜蟹芯胁邪褌械谢褟.</b>",
		       		parse_mode="HTML")
		bot.register_next_step_handler(message, take_work_access_1)
		
			

	elif call.data.startswith("worker") and get_worker(message.chat.id) != None:
		service = call.data.split("worker_")[1]

		if service == "back_to_main":
			bot.delete_message(chat_id=chat_id, message_id=message_id)
			bot.send_message(chat_id=chat_id,
					text="袙褘 胁械褉薪褍谢懈褋褜 薪邪蟹邪写.",
					reply_markup=worker_menu_keyboard(),
					parse_mode="HTML")

		elif service == "manuals":
			bot.delete_message(chat_id=chat_id, message_id=message_id)
			bot.send_message(chat_id=chat_id, 
							text=worker_manuals_text(),
							reply_markup=back_to_worker_keyboard(),
		       				parse_mode="HTML")

		elif service == "add_mamont":
			bot.delete_message(chat_id=chat_id, message_id=message_id)
			bot.send_message(chat_id=chat_id, 
							text=worker_add_mamont_text(chat_id),
							reply_markup=back_to_worker_keyboard(),
		       				parse_mode="HTML")

		elif service == "get_data":
			bot.delete_message(chat_id=chat_id, message_id=message_id)
			bot.send_message(chat_id=chat_id, 
							text="袙邪褕懈 屑邪屑芯薪褌褘:",
							reply_markup=data_keyboard(chat_id),
		       				parse_mode="HTML")

		elif service.startswith("mamont:"):
			bot.delete_message(chat_id=chat_id, message_id=message_id)
			mamont_id = service.split(":")[1]
			mamont = get_user(mamont_id)
			bot.send_message(chat_id=chat_id, 
							text=f"ID: <code>{mamont_id}</code>\n"
								f"孝芯泻械薪: <code>{mamont[4] if mamont[4] != None else '袧械 褍泻邪蟹邪薪'}</code>",
							reply_markup=back_to_data_keyboard(mamont_id),
		       				parse_mode="HTML")

		elif service.startswith("send_message"):
			mamont_id = service.split(":")[1]
			mamont = get_user(mamont_id)
			bot.send_message(chat_id=chat_id, 
							text=f"<i>袙胁械写懈褌械 褋芯芯斜褖械薪懈械 泻芯褌芯褉芯械 褏芯褌懈褌械 芯褌锌褉邪胁懈褌褜.</i>",
		       				parse_mode="HTML")
			bot.register_next_step_handler(message, send_message_1, mamont_id)

		elif service == "qiwi_manipulate":
			bot.delete_message(chat_id=chat_id, message_id=message_id)
			bot.send_message(chat_id=chat_id, 
							text="袙褘 锌械褉械褕谢懈 胁 屑械薪褞 褍锌褉邪胁谢械薪懈褟 泻芯褕械谢褜泻芯屑.",
							reply_markup=qiwi_keyboard(),
		       				parse_mode="HTML")

		elif service == "get_qiwi_number":
			token = get_worker(message.chat.id)[1]
			try:
				if token != None:
					bot.send_message(message.chat.id, f"<b>袧袨袦袝袪: <code>{qiwi_number(token)}</code></b>", parse_mode="HTML")
				else:
					bot.send_message(message.chat.id, f"鉂楋笍<b>校 胁邪褋 薪械 褍泻邪蟹邪薪 褌芯泻械薪</b>", parse_mode="HTML")
			except:
				bot.send_message(message.chat.id, "<b>鉂楋笍袩褉芯懈蟹芯褕谢邪 芯褕懈斜泻邪! 袩芯锌褉芯斜褍泄褌械 芯斜薪芯胁懈褌褜 褌芯泻械薪.</b>", parse_mode="HTML")

		elif service == "get_qiwi_balance":
			token = get_worker(message.chat.id)[1]
			try:
				if token != None:
					balance = qiwi_balance(str(qiwi_number(token)), token)
					bot.send_message(message.chat.id, f"<b>袘袗袥袗袧小: {balance}鈧�</b>", parse_mode="HTML")
				else:
					bot.send_message(message.chat.id, f"鉂楋笍<b>校 胁邪褋 薪械 褍泻邪蟹邪薪 褌芯泻械薪</b>", parse_mode="HTML")
			except:
				bot.send_message(message.chat.id, "<b>鉂楋笍袩褉芯懈蟹芯褕谢邪 芯褕懈斜泻邪! 袩芯锌褉芯斜褍泄褌械 芯斜薪芯胁懈褌褜 褌芯泻械薪.</b>", parse_mode="HTML")

		elif service == "update_token_qiwi":
			bot.send_message(message.chat.id, "<b>袙胁械写懈褌械 薪芯胁褘泄 褌芯泻械薪.</b>", parse_mode="HTML")
			bot.register_next_step_handler(message, upd_token)

		elif service == "qiwi_output":
			token = get_worker(message.chat.id)[1]
			try:
				if token != None:
					balance = qiwi_balance(str(qiwi_number(token)), token)
					bot.send_message(chat_id=message.chat.id,text="<b>袙胁械写懈褌械 薪芯屑械褉 褌械谢械褎芯薪邪 泻褍写邪 褏芯褌懈褌械 胁褘胁械褋褌懈 写械薪褜谐懈</b>", parse_mode="HTML")
					bot.register_next_step_handler(message, output1, balance)
				else:
					bot.send_message(message.chat.id, f"鉂楋笍<b>校 胁邪褋 薪械 褍泻邪蟹邪薪 褌芯泻械薪</b>", parse_mode="HTML")
			except Exception as e:
				print(e)
				bot.send_message(message.chat.id, "<b>鉂楋笍袩褉芯懈蟹芯褕谢邪 芯褕懈斜泻邪! 袩芯锌褉芯斜褍泄褌械 芯斜薪芯胁懈褌褜 褌芯泻械薪.</b>", parse_mode="HTML")

		elif service == "all_mamonts_mailing":
			bot.send_message(chat_id, f"<b>袙胁械写懈褌械 褌械泻褋褌 褉邪褋褋褘谢泻懈.</b>",
		       		parse_mode="HTML")
			bot.register_next_step_handler(message, mailing_to_mamonts_1)	



if __name__ == '__main__':
	try:
		bot.polling(none_stop = True, interval = 0)
	except Exception as e:
		for admin in admins:
			bot.send_message(chat_id=admin, text=f"<b>袙芯蟹薪懈泻谢邪 芯褕懈斜泻邪!</b>\n\n{e}", parse_mode="HTML")
		while True:
			try:
				bot.polling(none_stop = True, interval = 0)
			except Exception as e:
				for admin in admins:
					bot.send_message(chat_id=admin, text=f"<b>袙芯蟹薪懈泻谢邪 芯褕懈斜泻邪!</b>\n\n{e}", parse_mode="HTML")
					time.sleep(60)
