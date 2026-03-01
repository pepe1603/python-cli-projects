import subprocess
import os
import sys

DOWNLOAD_PATH = "/storage/emulated/0/Download/FacebookVideos"


def ensure_download_folder():
    if not os.path.exists(DOWNLOAD_PATH):
        os.makedirs(DOWNLOAD_PATH)


def download_video(url):
    try:
        print("\n📥 Descargando video...")
        subprocess.run([
            "yt-dlp",
            "-f", "mp4",
            "-o", f"{DOWNLOAD_PATH}/%(title)s.%(ext)s",
            url
        ], check=True)
        print("✅ Descarga completada\n")
    except subprocess.CalledProcessError:
        print("❌ Error al descargar el video")
        print("⚠️ Verifica que el video sea público\n")


def download_multiple():
    print("\nPega las URLs (una por línea).")
    print("Escribe 'FIN' para comenzar la descarga:\n")

    urls = []
    while True:
        url = input("> ")
        if url.upper() == "FIN":
            break
        urls.append(url)

    for url in urls:
        download_video(url)


def show_menu():
    print("""
====================================
📹 Facebook Video Downloader (Termux)
====================================
1️⃣ Descargar un video
2️⃣ Descargar varios videos
3️⃣ Salir
""")


def main():
    ensure_download_folder()

    while True:
        show_menu()
        option = input("Selecciona una opción: ")

        if option == "1":
            url = input("\nPega la URL del video: ")
            download_video(url)

        elif option == "2":
            download_multiple()

        elif option == "3":
            print("\n👋 Saliendo...")
            sys.exit(0)

        else:
            print("\n❌ Opción inválida\n")


if __name__ == "__main__":
    main()

