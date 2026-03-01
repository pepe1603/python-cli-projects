import os
import sys
import json

NOTES_FILE = "notes.json"


def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return json.load(file)


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)


def add_note():
    title = input("Título: ")
    content = input("Contenido: ")

    notes = load_notes()
    notes.append({"title": title, "content": content})
    save_notes(notes)

    print("✅ Nota guardada\n")


def list_notes():
    notes = load_notes()

    if not notes:
        print("📭 No hay notas guardadas\n")
        return

    for i, note in enumerate(notes, 1):
        print(f"{i}. {note['title']}")
    print()


def view_note():
    notes = load_notes()
    list_notes()

    if not notes:
        return

    try:
        index = int(input("Selecciona número de nota: ")) - 1
        print("\n📝", notes[index]["title"])
        print(notes[index]["content"], "\n")
    except (ValueError, IndexError):
        print("❌ Selección inválida\n")


def delete_note():
    notes = load_notes()
    list_notes()

    if not notes:
        return

    try:
        index = int(input("Número de nota a eliminar: ")) - 1
        deleted = notes.pop(index)
        save_notes(notes)
        print(f"🗑 Nota '{deleted['title']}' eliminada\n")
    except (ValueError, IndexError):
        print("❌ Selección inválida\n")


def show_menu():
    print("""
=========================
📝 Notes CLI App
=========================
1️⃣ Agregar nota
2️⃣ Listar notas
3️⃣ Ver nota
4️⃣ Eliminar nota
5️⃣ Salir
""")


def main():
    while True:
        show_menu()
        option = input("Selecciona opción: ")

        if option == "1":
            add_note()
        elif option == "2":
            list_notes()
        elif option == "3":
            view_note()
        elif option == "4":
            delete_note()
        elif option == "5":
            print("👋 Saliendo...")
            sys.exit(0)
        else:
            print("❌ Opción inválida\n")


if __name__ == "__main__":
    main()
