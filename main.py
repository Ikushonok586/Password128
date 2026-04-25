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
    except:
        bot.reply_to(message, "❌ Используй: /password или /password 16")
