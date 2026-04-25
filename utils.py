import random
import string

_history = {}


def generate_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return "".join(random.choice(chars) for _ in range(length))


def check_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+" for c in password):
        score += 1

    if score <= 2:
        return "Слабый 🔴"
    if score <= 3:
        return "Средний 🟡"
    return "Сильный 🟢"


def add_to_history(chat_id, password):
    _history.setdefault(chat_id, []).append(password)
    if len(_history[chat_id]) > 20:
        _history[chat_id] = _history[chat_id][-20:]


def get_history(chat_id):
    return _history.get(chat_id, [])
