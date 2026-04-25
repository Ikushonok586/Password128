import telebot
from utils import generate_password, check_strength, add_to_history

bot = telebot.TeleBot('YOUR_BOT_TOKEN_HERE')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для генерации паролей. Используй команду /password, чтобы получить новый пароль. Ты можешь указать длину пароля, например: /password 16")


@bot.message_handler(commands=['password'])
def simple_password(message):
    try:
        parts = message.text.split()
        length = int(parts[1]) if len(parts) > 1 else 10
        if length > 30:
            length = 30
        if length < 4:
            length = 4
        
        password = generate_password(length)
        add_to_history(message.chat.id, password)
        
        bot.reply_to(message, 
            f"🔑 *Пароль:* `{password}`\n\n💪 *Сложность:* {check_strength(password)}", 
            parse_mode='Markdown')
        bot.reply_to(message, "❌ Используй: /password или /password 16")


@bot.message_handler(commands=['multi'])
def multi(message):
    bot.send_message(message.chat.id, "Сколько паролей?")
    bot.register_next_step_handler(message, ask_count)

def ask_count(message):
    count = int(message.text)
    bot.send_message(message.chat.id, "Сколько символов?")
    bot.register_next_step_handler(message, lambda m: generate(m, count))
def generate(message, count):
    length = int(message.text)
    text = ""
    for i in range(count):
        pwd = generate_password(length)[0]
        text += f"{i+1}. {pwd}\n"
    bot.send_message(message.chat.id, text)