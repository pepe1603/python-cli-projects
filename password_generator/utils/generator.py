import secrets
import string

def generate_password(length=12, symbols=True, digits=True):
    chars = string.ascii_letters
    if symbols:
        chars += string.punctuation
    if digits:
        chars += string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))


