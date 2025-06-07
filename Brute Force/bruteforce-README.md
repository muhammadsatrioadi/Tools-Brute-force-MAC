# SATHack MikroTik Winbox Bruteforcer

## Deskripsi Program
Program ini adalah tool bruteforce untuk autentikasi Winbox pada perangkat MikroTik. Program ini menggunakan pendekatan multi-threading dan memiliki fitur logging yang komprehensif. Program ini dikembangkan oleh SATHack Team dengan versi 2.0.

## Fitur Utama

1. **Antarmuka Visual**
   - Banner animasi dengan nama "SATHack"
   - Animasi loading
   - Banner sukses yang informatif
   - Output berwarna

2. **Fungsionalitas Bruteforce**
   - Multi-threading untuk performa optimal
   - Dukungan wordlist
   - Delay yang dapat dikonfigurasi
   - Raw socket untuk komunikasi Layer 2

3. **Logging dan Monitoring**
   - Logging ke file (bruteforce.log)
   - Output ke console
   - Tracking waktu dan jumlah percobaan
   - Format timestamp yang detail

## Komponen Program

### 1. Fungsi Utilitas
```python
def print_slow(str)
def loading_animation()
def show_banner()
def show_success_banner(password, elapsed, attempts)
```
- Fungsi-fungsi untuk tampilan visual dan animasi
- Menampilkan informasi status dan hasil

### 2. Kelas Bruteforcer
```python
class Bruteforcer:
    def __init__(self, mac_target, username, wordlist, threads=5, delay=0.2)
    def send_mac_login(self, password)
    def try_password(self, password)
    def start(self)
```
- Kelas utama untuk operasi bruteforce
- Mengelola koneksi dan percobaan login
- Menangani multi-threading

## Cara Penggunaan

### Prasyarat
1. Python 3.x
2. Hak akses root/sudo (untuk raw socket)
3. File wordlist (default: passwords.txt)

### Command Line Arguments
```bash
python bruteforce.py [options]

Options:
  -m, --mac       Target MAC address (default: 4C:5E:0C:12:34:56)
  -u, --username  Username (default: admin)
  -w, --wordlist  Wordlist file (default: passwords.txt)
  -t, --threads   Number of threads (default: 5)
  -d, --delay     Delay between attempts (default: 0.2)
```

### Contoh Penggunaan
```bash
sudo python bruteforce.py -m 00:11:22:33:44:55 -u admin -w mypasswords.txt -t 10 -d 0.1
```

## Penjelasan Teknis

### 1. Protokol dan Koneksi
- Menggunakan raw socket (IPPROTO_RAW)
- Port target: 20561
- Format paket: `\x01\x00` + padding

### 2. Multi-threading
- Menggunakan ThreadPoolExecutor
- Jumlah thread dapat dikonfigurasi
- Thread sharing untuk tracking percobaan

### 3. Logging System
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bruteforce.log'),
        logging.StreamHandler()
    ]
)
```
- Logging ke file dan console
- Format timestamp yang detail
- Level logging: INFO

## Keamanan dan Pembatasan

1. **Persyaratan Keamanan**
   - Membutuhkan hak akses root/sudo
   - Hanya untuk tujuan edukasi
   - Gunakan hanya pada sistem yang Anda miliki

2. **Pembatasan Teknis**
   - Delay minimum: 0.2 detik
   - Thread default: 5
   - Format MAC: XX:XX:XX:XX:XX:XX

## Output dan Logging

1. **File Log**
   - Nama file: bruteforce.log
   - Format: timestamp - level - message
   - Mencatat semua percobaan dan hasil

2. **Console Output**
   - Banner animasi
   - Status percobaan
   - Banner sukses dengan detail

## Penanganan Error

1. **Error Handling**
   - PermissionError untuk raw socket
   - FileNotFoundError untuk wordlist
   - KeyboardInterrupt untuk user stop

2. **Logging Error**
   - Error dicatat ke file log
   - Pesan error yang informatif
   - Exit code yang sesuai

## Pengembangan Selanjutnya

1. **Fitur yang Dapat Ditambahkan**
   - Progress bar
   - Resume capability
   - Multiple target support
   - Custom protocol options
   - Rate limiting

2. **Peningkatan Keamanan**
   - Enkripsi wordlist
   - Timeout handling
   - Rate limiting
   - Error recovery

## Penulis
- Team: SATHack
- Versi: 2.0
- Tujuan: Edukasi dan Pengujian Keamanan

## Catatan
Program ini membutuhkan hak akses root/sudo karena menggunakan raw socket. Pastikan untuk menggunakan program ini dengan bertanggung jawab dan hanya pada sistem yang Anda miliki atau memiliki izin. 