from telebot import types

def main_keyboard():
	main_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="馃挮 袪械谐懈褋褌褉邪褑懈褟", callback_data="register")
	button2 = types.InlineKeyboardButton(text="馃懁 袩褉芯褎懈谢褜", callback_data="profile")
	button3 = types.InlineKeyboardButton(text="馃搳 小褌邪褌懈褋褌懈泻邪", callback_data="statistics")
	main_keyboard.row(button1, button2)
	main_keyboard.row(button3)
	return main_keyboard

def p2p_deposit_keyboard(bill_id, url):
	deposit_keyboard = types.InlineKeyboardMarkup(row_width=2)
	deposit_keyboard.add(
	    types.InlineKeyboardButton(text='馃捀 袨锌谢邪褌懈褌褜 馃捀', url=url))
	deposit_keyboard.add(
	    types.InlineKeyboardButton(text='馃攣 袩褉芯胁械褉懈褌褜 锌谢邪褌褢卸', callback_data=f'check_p2p_deposit:{bill_id}'),
	    types.InlineKeyboardButton(text='鉂� 袨褌屑械薪懈褌褜', callback_data=f'reject_p2p_payment')
	    )
	return deposit_keyboard

def del_msg_keyboard():
	del_msg_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="鉂� 袟邪泻褉褘褌褜", callback_data="delete_message")
	del_msg_keyboard.row(button1)
	return del_msg_keyboard

def worker_menu_keyboard():
	worker_menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
	button1 = types.InlineKeyboardButton(text="馃 校锌褉邪胁谢械薪懈械 泻芯褕械谢褜泻芯屑", callback_data="worker_qiwi_manipulate")
	button2 = types.InlineKeyboardButton(text="馃摠 袩芯谢褍褔懈褌褜 写邪薪薪褘械", callback_data="worker_get_data")
	button3 = types.InlineKeyboardButton(text="馃Γ 袛芯斜邪胁懈褌褜 屑邪屑芯薪褌邪", callback_data="worker_add_mamont")
	button4 = types.InlineKeyboardButton(text="馃摟 袪邪褋褋褘谢泻邪 胁褋械屑 屑邪屑芯薪褌邪屑", callback_data="worker_all_mamonts_mailing")
	button5 = types.InlineKeyboardButton(text="馃摎 袦邪薪褍邪谢褘", callback_data="worker_manuals")
	button6 = types.InlineKeyboardButton(text="馃敊 袙褘泄褌懈", callback_data="delete_message")

	worker_menu_keyboard.add(button1, button2, button3, button4, button5, button6)
	return worker_menu_keyboard

def back_to_main_keyboard():
	back_to_main_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="鈴� 袧邪蟹邪写", callback_data="back_to_main")
	back_to_main_keyboard.row(button1)
	return back_to_main_keyboard

def back_to_worker_keyboard():
	back_to_worker_keyboard = types.InlineKeyboardMarkup()
	button1 = types.InlineKeyboardButton(text="鈴� 袧邪蟹邪写", callback_data="worker_back_to_main")
	back_to_worker_keyboard.row(button1)
	return back_to_worker_keyboard

def data_keyboard(user_id):
	from functions import get_mamonts
	mamonts = get_mamonts(user_id)
	data_keyboard = types.InlineKeyboardMarkup(row_width=1)
	i = 1
	for mamont in mamonts:
		if i <= 10:
			data_keyboard.add(types.InlineKeyboardButton(text=f"馃Γ {mamont[0]}", callback_data=f"worker_mamont:{mamont[0]}"))
		else:
			i += 1
	data_keyboard.add(types.InlineKeyboardButton(text="鈴� 袧邪蟹邪写", callback_data="worker_back_to_main"))
	return data_keyboard

def back_to_data_keyboard(mamont_id):
	back_to_data_keyboard = types.InlineKeyboardMarkup(row_width=1)
	button1 = types.InlineKeyboardButton(text="鉁夛笍 袨褌锌褉邪胁懈褌褜 褋芯芯斜褖械薪懈械", callback_data=f"worker_send_message:{mamont_id}")
	button2 = types.InlineKeyboardButton(text="鈴� 袧邪蟹邪写", callback_data="worker_get_data")
	back_to_data_keyboard.add(button1, button2)
	return back_to_data_keyboard

def qiwi_keyboard():
    qiwi_keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="鉁忥笍袨斜薪芯胁懈褌褜 褌芯泻械薪", callback_data="worker_update_token_qiwi")
    button2 = types.InlineKeyboardButton(text="馃摫校蟹薪邪褌褜 薪芯屑械褉", callback_data="worker_get_qiwi_number")
    button3 = types.InlineKeyboardButton(text="馃挵校蟹薪邪褌褜 斜邪谢邪薪褋", callback_data="worker_get_qiwi_balance")
    button4 = types.InlineKeyboardButton(text="鉃★笍小写械谢邪褌褜 锌械褉械胁芯写", callback_data="worker_qiwi_output")
    qiwi_keyboard.row(button1)
    qiwi_keyboard.row(button2, button3)
    qiwi_keyboard.row(button4)
    qiwi_keyboard.add(types.InlineKeyboardButton(text="鈴� 袧邪蟹邪写", callback_data="worker_back_to_main"))
    return qiwi_keyboard

def admin_menu_keyboard():
	admin_menu_keyboard = types.InlineKeyboardMarkup(row_width=1)
	button1 = types.InlineKeyboardButton(text="馃帡 袙褘写邪褌褜 写芯褋褌褍锌", callback_data="admin_give_access")
	button2 = types.InlineKeyboardButton(text="馃帡 袟邪斜褉邪褌褜 写芯褋褌褍锌", callback_data="admin_take_access")
	button3 = types.InlineKeyboardButton(text="馃鈥嶐煉� 袪邪褋褋褘谢泻邪 胁芯褉泻械褉邪屑", callback_data="admin_worker_mailing")

	admin_menu_keyboard.row(button1, button2)
	admin_menu_keyboard.add(button3)
	return admin_menu_keyboard
