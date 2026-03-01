import os
from cryptography.fernet import Fernet
import getpass
import json
from datetime import datetime


MASTER_KEY_FILE = os.path.expanduser('~/.pass_master.key')

def get_master_key():
    if not os.exists(MASTER_KEY_FILE):
        print("Creando clave maestra...")
        key = Fernet.generate_key()
        with open(MASTER_KEY_FILE, 'wb') as f:
            f.write(key)
        os.chmod(MASTER_KEY_FILE, 0o600)  # Solo lectura/escritura por el dueño
        print(f"Clave guardada en {MASTER_KEY_FILE}")
    else:
        key = open(MASTER_KEY_FILE, 'rb').read()
    return Fernet(key)

def encrypt_data(data, fernet):
    return fernet.encrypt(data.encode())

def decrypt_data(encrypted, fernet):
    return fernet.decrypt(encrypted).decode()

def save_password(name, password, fernet, file='data/passwords.enc'):
    try:
        data = json.load(open(file, 'r'))
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}
    data[name] = {
        'password': fernet.encrypt(password.encode()).decode(),
        'date': datetime.now().isoformat()  # Fecha opcional
    }
    with open(file, 'w') as f:
        json.dump(data, f)

def load_passwords(fernet, file='data/passwords.enc'):
    try:
        data = json.load(open(file, 'r'))
        for name, info in data.items():
            data[name]['password'] = fernet.decrypt(info['password'].encode()).decode()
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

