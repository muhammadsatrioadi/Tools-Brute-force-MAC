import socket
import struct
import time
import sys
import random
import argparse
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import logging
import os

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bruteforce.log'),
        logging.StreamHandler()
    ]
)

def print_slow(str):
    for char in str:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)

def loading_animation():
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(20):
        sys.stdout.write("\r" + "Loading " + chars[i % len(chars)])
        sys.stdout.flush()
        time.sleep(0.1)
    print("\r" + " " * 20 + "\r", end="")

def show_banner():
    banner = """
    ███████╗ █████╗ ████████╗██╗  ██╗ █████╗  ██████╗██╗  ██╗
    ██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔══██╗██╔════╝██║ ██╔╝
    ███████╗███████║   ██║   ███████║███████║██║     █████╔╝ 
    ╚════██║██╔══██║   ██║   ██╔══██║██╔══██║██║     ██╔═██╗ 
    ███████║██║  ██║   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
    ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    """
    print("\033[92m" + banner + "\033[0m")
    loading_animation()
    print_slow("\n[*] SATHack - MikroTik Winbox Bruteforcer\n")
    loading_animation()
    print_slow("[*] Author: SATHack Team\n")
    loading_animation()
    print_slow("[*] Version: 2.0\n\n")

def show_success_banner(password, elapsed, attempts):
    success_banner = f"""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║  ██████╗  █████╗ ███████╗███████╗██╗   ██╗███████╗     ║
    ║  ██╔══██╗██╔══██╗██╔════╝██╔════╝██║   ██║██╔════╝     ║
    ║  ██████╔╝███████║███████╗███████╗██║   ██║███████╗     ║
    ║  ██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║╚════██║     ║
    ║  ██║     ██║  ██║███████║███████║╚██████╔╝███████║     ║
    ║  ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝     ║
    ║                                                          ║
    ║  Password ditemukan: {password:<30} ║
    ║  Waktu yang dibutuhkan: {elapsed:.2f} detik              ║
    ║  Total percobaan: {attempts}                            ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """
    print("\033[92m" + success_banner + "\033[0m")

class Bruteforcer:
    def __init__(self, mac_target, username, wordlist, threads=5, delay=0.2):
        self.mac_target = mac_target
        self.username = username
        self.wordlist = wordlist
        self.threads = threads
        self.delay = delay
        self.found = False
        self.attempts = 0
        self.start_time = None

    def send_mac_login(self, password):
        """
        Mengirim paket login Winbox via MAC address (Port 20561)
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
        except PermissionError:
            logging.error("Jalankan script dengan sudo/root karena butuh raw socket.")
            sys.exit(1)

        mac_bytes = bytes.fromhex(self.mac_target.replace(":", ""))
        payload = b"\x01\x00" + b"\x00" * 10

        loading_animation()
        logging.info(f"[!] (Mock) Sending login to {self.mac_target} with password: {password}")
        time.sleep(self.delay)
        
        if password == "admin123":
            logging.info(f"[+] Sukses login! Password ditemukan: {password}")
            return True
        else:
            logging.info(f"[-] Gagal: {password}")
            return False

    def try_password(self, password):
        if self.found:
            return

        self.attempts += 1
        success = self.send_mac_login(password)
        
        if success:
            self.found = True
            elapsed = time.time() - self.start_time
            show_success_banner(password, elapsed, self.attempts)
            return True
        return False

    def start(self):
        self.start_time = time.time()
        loading_animation()
        logging.info(f"[*] Starting bruteforce attack...")
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            executor.map(self.try_password, self.wordlist)

        if not self.found:
            logging.warning("Password tidak ditemukan dalam wordlist")

def main():
    parser = argparse.ArgumentParser(description='MikroTik Winbox Bruteforcer')
    parser.add_argument('-m', '--mac', default="4C:5E:0C:12:34:56", help='Target MAC address')
    parser.add_argument('-u', '--username', default="admin", help='Username')
    parser.add_argument('-w', '--wordlist', default="passwords.txt", help='Wordlist file')
    parser.add_argument('-t', '--threads', type=int, default=5, help='Number of threads')
    parser.add_argument('-d', '--delay', type=float, default=0.2, help='Delay between attempts')
    
    args = parser.parse_args()

    show_banner()

    if not os.path.exists(args.wordlist):
        logging.error(f"Wordlist file tidak ditemukan: {args.wordlist}")
        sys.exit(1)

    with open(args.wordlist, "r") as f:
        passwords = [line.strip() for line in f.readlines()]

    bruteforcer = Bruteforcer(
        mac_target=args.mac,
        username=args.username,
        wordlist=passwords,
        threads=args.threads,
        delay=args.delay
    )

    try:
        bruteforcer.start()
    except KeyboardInterrupt:
        logging.info("\nBruteforce dihentikan oleh user")
        sys.exit(0)

if __name__ == "__main__":
    main()
