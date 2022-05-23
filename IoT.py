#!/usr/bin/env python

# A konfigurációs fájlunknak ugyanabban a könyvtárban kell lennie, mint a programunknak!
# 
# Linux szerverünkön kiadott parancs:
# --------------
# Config fájl létrehozása:
# $ cat config_Admin_Router_running-config_changes.txt
# --------------
# Pufferméret beállítása:
# logging buffered 100000
# --------------
# Nincs logging console:
# no logging console
# --------------

# A "netmiko" névtérből beinportáljuk a "ConnectHandler" elemet a futtatandó programunk névterébe.
from netmiko import ConnectHandler

# A "getpass" környezet "getpass" elemét szintén importáljuk a névtérbe.
from getpass import getpass

# Ezután definiáljuk az eszközt, majd az eléréshez szükséges paramétereket:
device1 = {
    "device_type": "cisco_ios",
    "host": "Admin_Router",
    "username": "SSH_ADMIN",
    "password": getpass(),
}

# Definiáljuk, hogy mi az a config fájl, amit fel akarunk tölteni az eszközünkre.
# Majd egy függvénnyel kapcsolódunk az eszközünkre és elküldjük neki a config fájlunkat.
# Menti a beállításokat.
cfg_file = "config_Admin_Router_running-config_changes.txt" 
with ConnectHandler(**device1) as net_connect:
    output = net_connect.send_config_from_file(cfg_file)
    output += net_connect.save_config()

# Hibák kiíratása, ha van.
print()
print(output)
print()

# Belépés privilegizált módba.
def enable(self, cmd='enable', pattern='')

# Elmentjük a beállításokat.
def save_config(self, cmd='copy running-config startup-config', confirm=True)

# Újrainditjuk az eszközt, így a már meglévő beállításainkkal tölt be.
def save_config(self, cmd='reload', confirm=True)

# Kilépés.
print()
