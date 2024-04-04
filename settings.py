from os import listdir, makedirs
from json import dump, load

settings_path: str = "data"


voice_communication: bool = True
cnn_answering: bool = True
command_module_enabled: bool = True
dialogue_names: list = [
	"алис", "alice"
]
name: str = "Alice"
initial_prompt: str = 'Отвечай в стиле девушки-голосового ассистента по имени Алиса на русском языке.'

default_config: dict = dict(
	voice_communication=voice_communication,
	cnn_answering=cnn_answering,
	command_module_enabled=command_module_enabled,
	dialogue_names=dialogue_names,
	name=name,
	initial_prompt=initial_prompt
)


try:makedirs(settings_path)
except FileExistsError: pass


def create_settings():
	with open(f"{settings_path}/settings.json", "w", encoding="utf-8") as file:
		dump(default_config, file)
		return default_config

def load_settings():
	with open(f"{settings_path}/settings.json") as json_file:
		return load(json_file)
	

if "settings.json" not in listdir(settings_path):
	settings=create_settings()
else:
	try:
		settings=load_settings()
	except:
		settings=create_settings()
