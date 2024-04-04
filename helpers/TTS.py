from .config import (
	language, model_id, sample_rate,
	speaker, put_accent, put_yo, device_type, tts_model, tts_repo_or_dir
)

import torch
import sounddevice as sd
import time
from threading import Thread

class audio_buffer:
	a_list: list = list()



class tts:
	device = torch.device(device_type)
	torch_model, _ = torch.hub.load(repo_or_dir=tts_repo_or_dir, model=tts_model, language=language, speaker=model_id)
	torch_model.to(device)

	a_buffer = audio_buffer()



	def tts_convertor(self, text: str):

		return self.torch_model.apply_tts(text=text+"..",
			speaker=speaker,
			sample_rate=sample_rate,
			put_accent=put_accent,
			put_yo=put_yo)

	def add_to_buffer(self, text):
		self.a_buffer.a_list.append("START")
		for text in self.string_division(text=text):
			try:
				self.a_buffer.a_list.append(self.tts_convertor(text=text))
			except Exception as e:
				self.warn(f"Не удалось озвучить сообщение. {e}")
				self.a_buffer.a_list.append(self.tts_convertor(text="Не удалось озвучить сообщение.."))
		self.a_buffer.a_list.append("END")
			

	def say(self, text: str) -> None:		
		Thread(target=self.add_to_buffer, args=(text,)).start()
		while True:
			if "START" in self.a_buffer.a_list and len(self.a_buffer.a_list) not in (0, 1):
				self.a_buffer.a_list.remove("START")
				break
		while True:
			audio = self.a_buffer.a_list[0]
			if audio == "END":
				self.a_buffer.a_list.clear()
				break
			self.a_buffer.a_list.remove(audio)
			sd.play(audio, sample_rate * 1.05)
			time.sleep((len(audio) / sample_rate) + 0.5)
			sd.stop()
		self.timers.last_voice_answer = time.time()
	


	def stop(self):
		pass

	def string_division(self, text: str, lenght: int = 500) -> list:
		return [text[i:i+lenght] for i in range(0, len(text), lenght)]
	
