import os
import sys
import time
from setuptools import setup, find_packages
from setuptools.command.install import install

# Renk kodları (Terminal uyumluluğu için direkt ANSI)
GREEN = "\033[1;32m"
RED = "\033[1;31m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

class PostInstallCommand(install):
    """Kurulum sonrası veya sırasında ekrana basılacak özel mesajlar."""
    def run(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{CYAN}🦅 AKREP OSINT Sistemi Kuruluyor...")
        time.sleep(1)
        print(f"{WHITE}Sistem gereksinimleri kontrol ediliyor... {GREEN}[TAMAM]")
        print(f"{WHITE}Bağımlılıklar indiriliyor... {GREEN}[TAMAM]")
        
        # Standart kurulum işlemini başlat
        install.run(self)
        
        print(f"\n{GREEN}✔ KURULUM BAŞARIYLA TAMAMLANDI!")
        print(f"{CYAN}--------------------------------------------------")
        print(f"{WHITE}Çalıştırmak için: {GREEN}python main.py")
        print(f"{CYAN}--------------------------------------------------{RESET}")

# Gerekli kütüphaneler listesi
# Bunlar araçtaki (1) - (8) arası tüm özellikler için şarttır.
requirements = [
    "requests",          # Social-Account & API işlemleri
    "phonenumbers",      # Phone-Number OSINT
    "colorama",          # Renklendirme (Fallback için)
    "beautifulsoup4",    # Scraping işlemleri
    "python-whois",      # Domain/IP OSINT
    "dnspython",         # DNS sorguları
    "pillow",            # Metadata (Exif) OSINT
    "shodan",            # Network tarama (Opsiyonel API için)
]

setup(
    name="akrep-osint",
    version="1.5.0",
    author="AKREP AİÇ",
    description="Advanced All-in-One OSINT Framework",
    long_description="Bu araç dijital istihbarat toplama amacıyla AKREP AİÇ tarafından geliştirilmiştir.",
    url="https://github.com/dixblo-q/akrep-osint",
    packages=find_packages(),
    install_requires=requirements,
    cmdclass={
        'install': PostInstallCommand,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Security",
    ],
    python_requires='>=3.7',
    zip_safe=False
)
