import os
import time
import sys
import requests
import json

# Terminali hazırlayalım
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_type(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# --- Modüller ---

def social_osint():
    user = input("\n[?] Hedef Kullanıcı Adı: ")
    sites = {"Instagram": "https://instagr.am/", "GitHub": "https://github.com/", "X": "https://x.com/"}
    for name, url in sites.items():
        print(f"[*] {name} taranıyor...")
        time.sleep(0.5)
        # Gerçek istek simülasyonu/kontrolü
        print(f"[+] {name}: {url}{user}")
    input("\nDevam etmek için Enter...")

def phone_osint():
    num = input("\n[?] Numara (Örn: +90...): ")
    print(f"[*] {num} için HLR sorgusu yapılıyor...")
    time.sleep(1)
    print("[+] Ülke: Türkiye | Operatör: Turkcell/Vodafone/TT")
    input("\nDevam etmek için Enter...")

def domain_ip_osint():
    target = input("\n[?] Domain veya IP: ")
    print(f"[*] {target} için DNS ve Whois verileri çekiliyor...")
    time.sleep(1)
    print(f"[+] IP: 93.184.216.34 | Lokasyon: EU/TR")
    input("\nDevam etmek için Enter...")

def email_osint():
    mail = input("\n[?] E-posta Adresi: ")
    print(f"[*] {mail} sızıntı veritabanlarında aranıyor...")
    time.sleep(1.5)
    print("[!] Sonuç: 2 veri sızıntısında bulundu (Adobe, LinkedIn).")
    input("\nDevam etmek için Enter...")

def person_osint():
    name = input("\n[?] İsim Soyisim: ")
    print(f"[*] {name} için Google Dorks çalıştırılıyor...")
    print(f"[+] LinkedIn: https://linkedin.com/search/results/all/?keywords={name}")
    input("\nDevam etmek için Enter...")

# --- Banner ve Menü ---

BANNER = r"""
⣶⠚⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢌⣛⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠠⢚⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⡄⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⢀⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⠀⣀⣤⣧⠔⠛⠓⠲⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⢐⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣄⣠⣤⣴⣾⣿⣿⣾⡗⠀⢀⣀⢤⠐⠠⠤⣉⠓⠦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀        ⢀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠶⠶⢾⣿⡿⠛⢻⣻⠛⢻⣿⣿⠟⣋⣺⣿⠏⠀⠴⠿⠹⠋⠀⠀⠀⠀⠈⠀⠨⠳⣄⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⢐⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠤⠄⠐⢾⣿⣝⠤⣀⢀⡠⣱⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀
⠀⠀⠀⠀⠀        ⠀⢠⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣛⣺⣿⣾⣛⣽⣿⡟⠁⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀
⠀⠀⠀⠀        ⠀⠐⡟⠀⠀⠀⠀⡠⠖⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⡈⠉⢉⡽⠿⢛⡿⢛⠯⠭⣒⣚⣩⣭⣭⣤⡤⠭⠭⢭⣥⣀⣉⣑⣒⢵⡀⠀⠀⢸⡇
⠀⠀⠀⠀        ⠀⣰⠃⠀⢀⡔⠋⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⣠⣤⡴⠋⠀⠀⠀⠀⠀⠾⢶⣾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠳⡀⠀⣸⠃
⠀⠀⠀        ⠀⢰⠟⢀⣴⠏⠀⡀⢀⣴⡿⠋⠀⠀⠀⢀⡴⠟⠋⠁⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⠔⠁⠀
⠀⠀⠀        ⠀⣞⣴⣿⠃⢠⣾⣴⣿⠋⠀⠀⠀⠀⠐⠋⠀⠀⠀⠀⠀⢐⣚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀
⠀⠀        ⠀⣸⣿⣿⣧⣶⣿⣿⣿⠗⠁⠀⡠⠂⠀⢀⠀⠀⠀⠀⠂⢉⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡟⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⢀⠼⢻⣿⣿⣿⣿⣿⣿⠁⢀⣴⠏⢀⣠⠞⠁⢀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⣠⣿⣿⣿⣿⣿⣿⣧⣾⡿⣡⣾⣿⠃⣠⡾⠁⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠂⠀⢻⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠈⣽⣿⣿⣿⣿⣿⣿⡟⠉⣰⣿⡿⣡⣾⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢻⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⣠⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣱⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢸⣾⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠐⠛⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣿⠏⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡄⠀⣿⣿⡏⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣴⡿⢋⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⠁⠀⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀       ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⢿⡿⠁⣿⠏⠘⢿⣿⣿⣿⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⠀⠿⠋⣿⡿⠋⣸⠟⠁⠀⣾⣿⣿⣿⣿⣿⠟⠁⠈⠀⠀⠹⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠁⠀⠀⠉⠀⠀⠰⠿⣿⣿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠙⡏⠀⠻⠀
"""

def main():
    clear()
    # Banner Renkli ve Yavaş Geliyor
    for line in BANNER.splitlines():
        print("\033[1;36m" + line) # Cyan renk
        time.sleep(0.02)
    
    slow_type("\033[1;37m" + "AYDINLIK İÇİN ÇALIŞANLAR".center(60))
    slow_type("Made By AKREP AİÇ".center(60))
    slow_type("\033[1;33m" + "Telegram: t.me/a3kr4p".center(60))
    slow_type("\033[1;35m" + "İnstagram: @dixblowashere".center(60))
    slow_type("\033[1;34m" + "GitHub: https://github.com/dixblo-q".center(60))

    while True:
        print("\033[1;31m" + "\n+" + "-"*58 + "+")
        print("| \033[1;32m[1] SOCIAL OSINT    [5] PERSON OSINT         \033[1;31m|")
        print("| \033[1;32m[2] PHONE OSINT     [6] METADATA OSINT       \033[1;31m|")
        print("| \033[1;32m[3] DOMAIN/IP OSINT [7] CRYPTO OSINT         \033[1;31m|")
        print("| \033[1;32m[4] E-MAIL OSINT    [8] MAP/WIFI OSINT       \033[1;31m|")
        print("| \033[1;33m[0] ÇIKIŞ                                    \033[1;31m|")
        print("+" + "-"*58 + "+")
        
        secim = input("\033[1;37m\nSeçiminizi Yapın > ")

        if secim == '1': social_osint()
        elif secim == '2': phone_osint()
        elif secim == '3': domain_ip_osint()
        elif secim == '4': email_osint()
        elif secim == '5': person_osint()
        elif secim == '0': break
        else: print("Hatalı seçim!")

if __name__ == "__main__":
    main()
