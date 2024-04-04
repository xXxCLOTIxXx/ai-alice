from g4f.client import Client
from helpers.config import (
	initial_prompt,
	max_history_length,
	cnn_model
)

from helpers.utils import check_internet

initial_promt = 'Отвечай в стиле девушки-голосового ассистента по имени Алиса на русском языке.'

class cnn:
	client = Client()
	history = list()

	def trim_history(self, history, max_length=max_history_length-1):
		current_length = sum(len(message["content"]) for message in history)
		while history and current_length > max_length:
			removed_message = history.pop(0)
			current_length -= len(removed_message["content"])
		return history




	def send_response(self, message: str):
		if message is None or message == '' or message == ' ':return
		if check_internet() is False:
			return None, "Простите, но подключение к интернету отсутствует. Разговорные функции недоступны."
		self.history.append(
			{"role": "user", "content": message}
		)
		self.history = self.trim_history(self.history)
		
		response = self.client.chat.completions.create(
			model=cnn_model,
			messages=[
				{"role": "user", "content": initial_prompt}
			]+self.history,
		)
		gpt_response = response.choices[0].message.content
		gpt_response=gpt_response.replace("####", "").replace("*", "")
		temp = gpt_response.split("\n\n")
		emotion = temp[0] if len(temp)!=1 else None
		message = '\n\n'.join(temp[1:] if len(temp)!=1 else temp)
		self.history.append({"role": "assistant", "content": gpt_response})
		self.call("on_cnn_response", message=message, emotion=emotion)
		return emotion, message
