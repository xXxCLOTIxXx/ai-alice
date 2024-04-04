

#stt
stt_model: str = "helpers/vosk_model"
samplerate: int = 16000
device: int = 7


#tts
language: str = 'ru'
model_id: str = 'ru_v3'
sample_rate: int = 48000
speaker: str = 'kseniya' # aidar, baya, kseniya, xenia, random
put_accent: bool = True
put_yo: bool = True
device_type: str = "cpu" # cpu или gpu
tts_repo_or_dir: str = 'snakers4/silero-models'
tts_model: str = 'silero_tts'


#logger
save_path: str = "logs"


#cnn
initial_prompt: str = 'Отвечай в стиле девушки-голосового ассистента по имени Алиса на русском языке.'
max_history_length: int = 4096
cnn_model="gpt-3.5-turbo"