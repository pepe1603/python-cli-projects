import os
import subprocess
import sys

PROJECTS = {
    "1": {
        "name": "Facebook Downloader",
        "path": "fb_downloader",
        "entry": "downloader.py"
    },
    "2": {
        "name": "Notes CLI",
        "path": "notes_cli",
        "entry": "main.py"
    },
    "3": {
        "name": "Password Generator",
        "path": "password_generator",
        "entry": "password_generator.py"
    }
}


def show_menu():
    print("""
==============================
🚀 Python CLI Projects Launcher
==============================
1️⃣ Facebook Downloader
2️⃣ Notes CLI
3️⃣ Password Generator
4️⃣ Salir
""")


def run_project(choice):
    project = PROJECTS.get(choice)

    if not project:
        print("❌ Opción inválida\n")
        return

    project_path = project["path"]
    entry_file = project["entry"]

    venv_python = os.path.join(project_path, "venv", "bin", "python")

    if not os.path.exists(venv_python):
        print(f"⚠️ No se encontró entorno virtual en {project_path}")
        return

    print(f"\n🚀 Ejecutando {project['name']}...\n")

    subprocess.run([venv_python, os.path.join(project_path, entry_file)])


def main():
    while True:
        show_menu()
        choice = input("Selecciona una opción: ")

        if choice == "4":
            print("👋 Saliendo del launcher...")
            sys.exit(0)

        run_project(choice)


if __name__ == "__main__":
    main()
