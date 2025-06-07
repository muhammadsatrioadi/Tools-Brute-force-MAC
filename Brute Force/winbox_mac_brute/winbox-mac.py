import time
import random

def try_mac_login(mac_addr, username, password):
    """
    Fungsi simulasi untuk mencoba login via MAC Winbox.
    Harusnya ini mengirim paket raw Layer 2 ke port 20561.
    """
    print(f"[+] Mencoba login ke {mac_addr} dengan user={username} pass={password}")
    time.sleep(0.3)

    # Simulasi keberhasilan hanya pada satu password
    if password == "admin123":
        return True
    return False

def main():
    mac_target = "4C:5E:0C:12:34:56"  # Ganti dengan MAC address router Mikrotik
    username = "admin"

    with open("wordlist.txt", "r") as f:
        passwords = [line.strip() for line in f]

    for pwd in passwords:
        if try_mac_login(mac_target, username, pwd):
            print(f"[✓] Berhasil login! Password: {pwd}")
            return
        else:
            print(f"[✗] Gagal: {pwd}")

    print("[!] Semua kombinasi gagal.")

if __name__ == "__main__":
    main()
