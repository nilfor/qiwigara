import telebot

main_token = '1722494528:AAEq2Qm_W8tM1YLVoZXcW52d38RBg-U0An8'
BOT_NAME = "VerdTeam_robot"

P2P_COMMENT = "袨锌谢邪褌邪 写芯褋褌褍锌邪 泻 锌邪薪械谢懈"
WORKER_ACCESS = 250

SECRET_P2P = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InpvejhkdS0wMCIsInVzZXJfaWQiOiI3OTYxNzg0MTY0NyIsInNlY3JldCI6IjQ2MmIzOTBhMzA4Y2IxYmZiMmNlOWM2NjI1MGZmMTliMWIwNzNmOTJhYjYwOGNiNmFjODZhY2IyZjRiZThlZTkifX0="
PUBLIC_P2P = "48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPzNKUdLfaCGLSoRGrJ6Qij7Udr6Bmgis6AwX6t6WQT1LG8WP71oH6RwbsaEHVzqhDfnpHD9P8o71gwGX2jRdyZXGbDGuaud79s6fSmWFVg"

admins = [915888204]

bot = telebot.TeleBot(main_token, threaded=True, num_threads=300)

manual_1 = "https://telegra.ph/Kak-snyat-dengi-tmeQIWIDENIGU-ROBOT-03-21"
manual_2 = "https://telegra.ph/Gde-najti-mamonta-03-21"
manual_3 = "https://telegra.ph/BEZOPASNOST-NASHE-VSE-03-21"
manual_4 = "https://telegra.ph/Kak-ubedit-mamonta-03-21"

phone_regex = "^[7|8|380](\d{10,11})$"

def worker_p2p_text():
	text = \
	"<b>袩芯褋谢械 芯锌谢邪褌褘 胁褘 锌芯谢褍褔邪械褌械\n"\
	"+ 袥懈褔薪褘泄 泻懈胁懈 屑邪薪懈锌褍谢褟褌芯褉 馃\n"\
	"+ 效邪褌 胁芯褉泻械褉芯胁 馃挰\n"\
	"+ 校薪懈泻邪谢褜薪褍褞 褋褘谢谢泻褍 写谢褟 锌褉懈谐谢邪褕械薪懈泄 屑邪屑芯薪褌芯胁 馃Γ\n" \
	"+ 袦邪薪褍邪谢褘 锌芯 锌芯懈褋泻褍 懈 斜械蟹芯锌邪褋薪芯褋褌懈 馃摎\n"\
	"+ 袛褉褍卸薪褘泄 泻芯谢谢械泻褌懈胁 懈 褏芯褉芯褕褍褞 邪褌屑芯褋褎械褉褍馃帀\n"\
	"+ 袣邪泻 褍斜械写懈褌褜 屑邪屑芯薪褌邪 胁 褉邪斜芯褌械 斜芯褌邪馃\n\n"\
	"袨锌谢邪褌懈褌褜 写芯褋褌褍锌 BTC 效袝袣袨袦  https://t.me/admricker</b>"
	return text

def statistics_text():
	text = \
	"<b>袙蝎袩袥袗效袝袧袨 袘袨袥袝袝 270000鈧� 馃\n\n"\
	"校褔邪褋褌薪懈泻芯胁 胁 斜芯褌械: 29000馃懃</b>\n"

	return text

def profile_text(user_id):
	text = \
	f"<b>馃懁 袩褉芯褎懈谢褜: {user_id}\n\n"\
	"馃挵 袘邪谢邪薪褋: 0 褉褍斜.\n"\
	"鉂� 袙褘 薪械 蟹邪褉械谐懈褋褌褉懈褉芯胁邪薪褘\n"\
	"馃搯 袟邪褉邪斜芯褌薪芯 蟹邪 胁褋械 胁褉械屑褟: 0 褉褍斜.\n\n"\
	"馃挸 袙褘胁芯写 褋褉械写褋褌胁 斜褍写械褌 写芯褋褌褍锌械薪 泻邪泻 褌芯谢褜泻芯 斜邪谢邪薪褋 褋褌邪薪械褌 胁褘褕械 1 褉褍斜.</b>"

	return text

def worker_manuals_text():
	text = \
	f"袣邪泻 褋薪褟褌褜 写械薪褜谐懈 褋 泻懈胁懈 馃 <a href='{manual_1}'>孝蝎袣</a>\n\n"\
	f"袣邪泻 薪邪泄褌懈 屑邪屑芯薪褌邪 馃Γ <a href='{manual_2}'>孝蝎袣</a>\n\n"\
	f"袘械蟹芯锌邪褋薪芯褋褌褜 薪邪褕械 胁褋械 馃敟 <a href='{manual_3}'>孝蝎袣</a>\n\n"\
	f"袣邪泻 褍斜械写懈褌褜 屑邪屑芯薪褌邪 馃巻 <a href='{manual_4}'>孝蝎袣</a>\n\n"

	return text

def worker_add_mamont_text(worker_id):
	text = \
	"<b>袛谢褟 锌芯谢褍褔械薪懈褟 写邪薪薪褘褏 屑邪屑芯薪褌邪 薪械芯斜褏芯写懈屑芯 褔褌芯斜褘 芯薪 蟹邪褉械谐械褋褌褉懈褉芯胁邪谢褋褟 胁 斜芯褌械 锌芯 胁邪褕械泄 褋褋褘谢泻械 猬囷笍\n"\
	f"<code>https://t.me/{BOT_NAME}?start={worker_id}</code></b>"

	return text
