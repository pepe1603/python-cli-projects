# Notes CLI App (Termux / Linux)

Aplicación en Python para gestionar notas desde la terminal.

## 📦 Requisitos

- Python 3

## 🐍 Crear entorno virtual

```bash
python -m venv venv


## ⚡ Crear alias para activar el entorno virtual

Añadir esto a tu archivo ~/.bashrc o ~/.zshrc:

```bash
alias venv='source venv/bin/activate'

Luegk ejecitar: 

```bash
source ~/.bashrc

Ahoranpuedes activar el entorno vistual ewcribiendo:

```bash
venv

## 🚀 Uso

```bash
venv
python main.py

## 🎯 Resultado final

Tu workspace quedará así:


projects/python/
── notes_cli/
 ├── main.py
 ├── README.md
 ├── requirements.txt
 └── venv/

## En Futuras Versiones

---

Si quieres, en el siguiente version  podemos:

- 🔐 Añadir cifrado a las notas
- 📅 Agregar fecha automática
- 🔎 Añadir buscador
- 💾 Exportar a TXT
- 🧠 Convertirla en app instalable con `pip install -e .`

¿Qué nivel quieres que le demos? comenta
