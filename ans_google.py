import subprocess
import julius_cli
from datetime import datetime
from time import sleep
import os
import codecs

global host


greeting = ""
guest = ""
host = "hello"

greetings =["こんにちは","こんばんは","おはようございます"]
hosts = ["貴恵","翔太","剛"]
hostsvoca = ["たかえ","しょうた","つよし"]
guests = ["クロネコ","郵便屋","佐川","けいじ","みつえ","清水","遠山","六本木","内田","瀬間","小林","島田","はが"]

ttBefore = 0

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
	
	phrase_in = ''
	phrase_out = ''
	print(words)

	#構文解析

	i=0

	for i in range(len(greetings)):
		if(greetings[i] in words):
			greeting = greetings[i]
			guest = ""
			host = ""
			phrase_out += greeting

	print("hhh:",host)
	print("ggg:",guest)
	if host == "":
		i = 0
		for i in range(len(hosts)):
			if(hosts[i] in words):
				host = hostsvoca[i]
	i = 0
	for i in range(len(guests)):
		if(guests[i] in words):
			guest = guests[i]


	phrase_in = "      "
	phrase_out = "      "

	if greeting == "":
		phrase_out += "何か御用でしょうか、ご主人様。"
		guest = ""
		host = ""
		greeting = "  "
	else:
		if guest == "":
			phrase_out += "どちらさまですか"
		else:
			if host == "":
				phrase_out += guest+"さん。誰に取り次ぎますか"
			else:
				phrase_out += '  少々おまちください。'
				if host == "剛": host = "ご主人"
				phrase_in += "   "+host+"さま、"+guest+"さまがお見えです"


				
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


