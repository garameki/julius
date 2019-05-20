import subprocess
import julius_cli
from datetime import datetime
from time import sleep

import codecs

def hear(words):

	file = codecs.open("hear.txt","w","shift_jis")
	i=0
	for i in range(len(words)):
		file.write(words[i])
		file.write("\n")
	file.close()
	return True

greet_morning = "おはようございます"
greet_day     = "こんにちは"
greet_evening = "こんばんは"

words_init = []

iHour = int(datetime.now().strftime("%H"))
if   iHour < 3:words_init.append(greet_evening)
elif iHour < 9:words_init.append(greet_morning)
elif iHour <17:words_init.append(greet_day)
elif iHour <24:words_init.append(greet_evening)

hear(words_init)
sleep(2)

try:
	julius_cli.julius_connect()
	julius_cli.julius_recv(hear)
except KeyboardInterrupt:
	julius_cli.julius_close()
