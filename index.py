import aiml
import pyttsx
from gtts import gTTS
import subprocess
import time




def process_output(output):
	if output[0:8] == '@COMMAND':
		return True
	
def command_process(command):
	if command[9:16] == 'GSEARCH':
		bash_command("firefox http://www.google.com?q="+command[17:].replace(' ','+')+" &")
		say("information about "+command[17:]+" is being displayed on screen ... anything else sir ?")
		
	if command[9:16] == 'FBOPENX':
		bash_command("firefox http://www.facebook.com")
		say("facebook is opened ... now enter your username and password and press submit , to continiue ... anything else sir ?")
	if command[9:16] == 'CURTIME':
		say("sir ... time is "+time.strftime("%H %M"))

def say(word):
	tts = gTTS(text=word,lang='en')
	tts.save("word.mp3")
		
	bashCommand = 'play word.mp3'
	bash_command(bashCommand)	

def bash_command(bashCommand):
	process = subprocess.Popen(bashCommand.split(),stdout=subprocess.PIPE)
	output = process.communicate()[0]

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")
while True:
	message = raw_input(">>>")
	respond = kernel.respond(message)
	if process_output(respond) == True:
		print 'processing command'
		command_process(respond)
		print 'command processed'
	else:
		say(respond)
		print respond
