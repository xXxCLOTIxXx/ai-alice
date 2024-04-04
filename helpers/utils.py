from requests import get

def check_internet():
	try:
		get("https://www.google.com")
		return True
	except Exception as e:
		return False