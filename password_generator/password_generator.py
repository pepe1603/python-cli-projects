from utils.crypto import get_master_key, save_password, load_passwords
from utils.generator import generate_password

def main():
    fernet = get_master_key()
    while True:
        print("\n1. Generar contraseña")
        print("2. Ver contraseñas")
        choice = input("Elige: ")
        if choice == '1':
            name = input("Nombre para la contraseña: ")
            pwd = generate_password()
            save_password(name, pwd, fernet)
            print(f"Contraseña para '{name}' guardada.")
        elif choice == '2':
            data = load_passwords(fernet)
            for name, info in data.items():
                date = info.get('date', 'Sin fecha')
                print(f"{name}: {info['password']} (Guardada: {date})")
        else:
            break
