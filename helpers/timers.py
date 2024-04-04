from time import time

class timers:

	last_voice_answer: int = time()


	def obsolescence(self, value: float, lifetime: float = 2.5) -> bool:
		if time() - value >= lifetime: return True
		return False