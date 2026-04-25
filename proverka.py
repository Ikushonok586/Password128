def check_strength(password):
    ball = 0
    if len(password) >= 8:
        ball += 1
    if any(c.isupper() for c in password):
        ball += 1
    if any(c.islower() for c in password):
        ball += 1
    if any(c.isdigit() for c in password):
        ball += 1
    if any(c in '!@#$%' for c in password):
        ball += 1
    
    if ball <= 2:
        return "слабый"
    elif ball <= 3:
        return "средний"
    else:
        return "сильный"

@bot.message_handler(commands=['check'])
def check(message):
    pwd = message.text.replace('/check', '').strip()
    if not pwd:
        bot.reply_to(message, "Напиши: /check пароль")
        return
    result = check_strength(pwd)
    bot.reply_to(message, f"Сложность: {result}")