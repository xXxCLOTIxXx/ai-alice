from helpers.types import event_methods as methods


class event_register:
	events = {}


	def on_event(self, type: str):
		def register(callback):
			if type not in self.events: self.events[type] = list()
			self.events[type].append(callback)
		return register

	def on_message(self):
		def register(callback):
			if "on_message" not in self.events: self.events["on_message"] = list()
			self.events["on_message"].append(callback)
		return register


	def on_recognize(self):
		def register(callback):
			if "on_recognize" not in self.events: self.events["on_recognize"] = list()
			self.events["on_recognize"].append(callback)
		return register

	def on_startup(self):
		def register(callback):
			if "on_startup" not in self.events: self.events["on_startup"] = list()
			self.events["on_startup"].append(callback)
		return register
	

	def on_cnn_response(self):
		def register(callback):
			if "on_startup" not in self.events: self.events["on_startup"] = list()
			self.events["on_startup"].append(callback)
		return register
	


	def call(self, method: str, **kwargs):
		if method not in self.events:
			return
		for func in self.events[method]:
			func(**kwargs)


	def checker(self):
		for method in methods:
			self.warn(message=f"Обработчик ивента {method} отсутствует.")

