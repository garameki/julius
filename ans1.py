import subprocess
import julius_cli
from datetime import datetime
from time import sleep
import os
import codecs


greet_morning = "おはようございます"                                        
greet_day     = "こんにちは"
greet_evening = "こんばんは"

greeting = ""
guest = ""
host = ""
guestBefore ="***"
start = False
flag_greeted = False 

greetings =["こんにちは","こんばんは","おはようございます","ごめんください"]
hosts = ["貴恵","翔太","剛"]
hostsvoca = ["たかえ","しょうた","つよし"]
guests = ["岡田","クロネコ","郵便屋","佐川","けいじ","みつえ","清水","遠山","六本木","内田","瀬間","小林","島田","芳賀"]
whs = ["遅い"]



ttBefore = 0
nn = 0

def answer(words):
	global ttBefore
	global host
	global guest
	global greeting
	global greetings
	global hosts
	global hostsvoca
	global guests
	global guestBefore
	global whs
	global nn
	global start
	global flag_greeted
	global greet_morning
	global greet_evening
	global greet_day

	phrase_in = ''
	phrase_out = ''
	print(words)

	i=0
	for i in range(len(greetings)):
		if(greetings[i] in words):
			greeting = greetings[i]
			guest = ""
			guestBefore = "***"
			start = False
			host = ""
			flag_greeted = False 

	i = 0
	for i in range(len(hosts)):
		if(hosts[i] in words):
			host = hostsvoca[i]

	i = 0
	for i in range(len(guests)):
		if(guests[i] in words):
			guest = guests[i]


	if guestBefore == "":
		print("aisatu{} host{} guest{} guestBeforeなし".format(greeting,host,guest))
	else:
		print("aisatu{} host{} guest{} guestBefore".format(greeting,host,guest,ord(guestBefore[0])))


	if guestBefore == "***":
		if guest == "":
			if host == "":
				if greeting == "" :
					phrase_out += "いらっしゃいませ。お名前をどうぞ？"
				else:
					if flag_greeted:
						phrase_out += "お名前をどうぞ？"
					else:
						if greeting == "ごめんください":
							iHour = int(datetime.now().strftime('%H'))
							if   iHour < 3:greeting = greet_evening
							elif iHour < 9:greeting = greet_morning
							elif iHour <17:greeting = greet_day
							elif iHour <24:greeting = greet_evening
						phrase_out += greeting+"お名前をどうぞ？"
						flag_greeted = True 
			else:
				phrase_out += "少々お待ちください。"
				phrase_in += "お客様です。至急玄関まで来てください。"
		else:
			phrase_out += "少々お待ちください。"
			phrase_in += guest+"さまがお見えです。至急玄関まで来てください"
			start = True
	else:
		if guest == "":
			nn += 1
			if host == "":
				if nn > 2:
					phrase_out += "本当に申し訳ございません。お名前が良く聞き取れません。"
				else:
					phrase_out += "お名前をどうぞ"
			else:
				phrase_out += "しょうしょうお待ちください。"
				phrase_in += "お客様です。至急玄関まで来てください。"
		else:
			nn = 0
			if host == "":
				if guest == guestBefore:


					for i in range(0,len(whs)):
						if(whs[i] in words):
							phrase_out += "遅いですね。"		
							phrase_in += "早くしてください。"


					phrase_in += guest+"さまが、お見えです。はやく玄関まで来てください。"
				else:
					phrase_in += guest+"さんが、お待ちです。至急玄関まで来てください。"
					phrase_out += guestBefore+"さんではなく、"+guest+"さんですね。すみませんでした。"
			else:
				if guest == guestBefore:
					phrase_in += "お客様です。至急玄関まで来てください。"
				else:
					phrase_out += guestBefore+"さんではなく、"+guest+"さんですね。すみませんでした。"
					phrase_in += guest+"さんが、お待ちです。至急玄関まで来てください。"

	if start:guestBefore = guest

	
				
	cmd_in = '/home/pi/src/aquestalkpi/AquesTalkPi -s 100 "     {0}" | aplay'.format(phrase_in)
	cmd_out = '/home/pi/src/aquestalkpi/AquesTalkPi -s 100 "     {0}" | aplay'.format(phrase_out)
	#subprocess.check_output(cmd,shell=True)

	cmd = cmd_out+";"+cmd_in
	print('in : {0}'.format(phrase_in))
	print('out : {0}'.format(phrase_out))
	os.system(cmd)
	return True
while True:
	tt = os.path.getmtime("hear.txt")
	if(tt != ttBefore):
		ttBefore = tt
		words = []
		for line in codecs.open("hear.txt","r","shift_jis"):
			words.append(line.strip())
		answer(words)
	sleep(1)


