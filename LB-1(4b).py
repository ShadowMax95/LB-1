import requests

bot_token = ''# Токен бота
chat_id = ''# ID чату або користувача

message = 'Привіт! Це повідомлення через Telegram Bot API.'

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
params = {
    'chat_id': chat_id,
    'text': message
}

response = requests.post(url, params=params)
if response.status_code == 200:
    print("Повідомлення надіслано успішно!")
else:
    print(f"Помилка: {response.status_code}")
