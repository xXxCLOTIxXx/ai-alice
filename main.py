from helpers.STT import stt as sr
from helpers.TTS import tts as speech
from event_handler import event_register
from helpers.logger import logger
from helpers.timers import timers as tm
from settings import settings

from cnn import cnn


from os import system



class ALICE(event_register, logger, cnn, sr, speech):
	timers = tm()

	def __init__(self):
		self.log("Запуск ассистента...\n")
		event_register.__init__(self)
		logger.__init__(self)
		cnn.__init__(self)
		speech.__init__(self)
		sr.__init__(self)


	def on_recognize(self, text: str):
		if settings.get("voice_communication") is False: return
		if self.timers.obsolescence(self.timers.last_voice_answer) is False:return
		self.call("on_recognize", message=text)
		self.call("on_message", message=text)
	

	def send_message(self, text: str):
		if text is None or text in ("", " "): return
		self.call("on_message", message=text)

	def run(self):
		self.call("on_startup")
		self.listen(self.on_recognize)
"""		while True:
			resp = self.send_response(input("\nmessage#~ "))
			message = resp[1]
			emotion = resp[0]
			#print(emotion)
			print(f"\n**ALICE**: {message}")
"""

app = ALICE()
@app.on_startup()
def on_start():
	system("cls || clear")
	app.log("Ассистент запущен.")


@app.on_message()
def on_message(message: str):
	print(f"\n**YOU**: {message}")
	resp = app.send_response(message)
	if resp is None: return
	message = resp[1]
	emotion = resp[0]
	#print(emotion)
	print(f"\n**ALICE**: {message}")
	app.say(message)


if __name__ == "__main__":
	app.run()