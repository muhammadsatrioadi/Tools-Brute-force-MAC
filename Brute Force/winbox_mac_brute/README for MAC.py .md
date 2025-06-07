# Winbox MAC Bruteforce Tool

## Deskripsi Program
Winbox MAC Bruteforce Tool adalah sebuah program Python yang dirancang untuk melakukan brute force pada alamat MAC untuk autentikasi Winbox. Program ini menggunakan pendekatan multi-threading untuk meningkatkan efisiensi proses brute force.

## Fitur Utama
1. **Antarmuka Pengguna yang Interaktif**
   - Banner animasi dengan nama "Satri0x"
   - Animasi loading
   - Input interaktif untuk IP target dan MAC address
   - Output berwarna untuk memudahkan pembacaan

2. **Fungsionalitas Brute Force**
   - Generasi alamat MAC acak
   - Dukungan untuk input MAC address awal
   - Validasi format MAC address
   - Multi-threading untuk performa yang lebih baik

3. **Keamanan dan Stabilitas**
   - Timeout pada koneksi
   - Penanganan error yang baik
   - Pencegahan overload pada target
   - Kemampuan untuk menghentikan proses dengan Ctrl+C

## Komponen Program

### 1. Fungsi Utama
- `generate_mac()`: Menghasilkan alamat MAC acak
- `validate_mac()`: Memvalidasi format MAC address
- `create_winbox_packet()`: Membuat paket autentikasi Winbox
- `try_mac()`: Mencoba autentikasi dengan MAC address tertentu
- `bruteforce()`: Fungsi utama untuk proses brute force

### 2. Komponen UI
- `print_banner()`: Menampilkan banner program
- `loading_animation()`: Menampilkan animasi loading
- `clear_screen()`: Membersihkan layar terminal

## Cara Penggunaan

### Prasyarat
1. Python 3.x
2. Library yang dibutuhkan:
   ```bash
   pip install colorama
   ```

### Langkah Penggunaan
1. Jalankan program:
   ```bash
   python Mac.py
   ```
2. Masukkan IP target saat diminta
3. Opsional: Masukkan MAC address awal (format: XX:XX:XX:XX:XX:XX)
4. Program akan mulai melakukan brute force
5. Tekan Ctrl+C untuk menghentikan proses

## Penjelasan Teknis

### 1. Protokol Winbox
- Program menggunakan port 8291 untuk koneksi Winbox
- Paket autentikasi dibuat dengan format khusus
- Response dari server digunakan untuk menentukan validitas MAC address

### 2. Multi-threading
- Menggunakan ThreadPoolExecutor untuk parallel processing
- Maksimal 10 thread berjalan bersamaan
- Delay 0.1 detik antara percobaan untuk mencegah overload

### 3. Validasi MAC Address
- Format: XX:XX:XX:XX:XX:XX
- Validasi karakter hexadecimal
- Pengecekan panjang dan format

## Keamanan dan Etika
- Program ini hanya untuk tujuan edukasi
- Hanya gunakan pada sistem yang Anda miliki atau memiliki izin
- Perhatikan hukum dan regulasi yang berlaku di wilayah Anda

## Pembatasan
1. Timeout koneksi: 2 detik
2. Maksimal thread: 10
3. Delay antar percobaan: 0.1 detik
4. Format MAC address harus valid

## Pengembangan Selanjutnya
1. Penambahan opsi konfigurasi
2. Peningkatan kecepatan brute force
3. Penambahan fitur logging
4. Dukungan untuk protokol tambahan

## Penulis
- Nama: Satri0x
- Versi: 1.0

## Catatan
Program ini dibuat untuk tujuan edukasi dan pengujian keamanan. Pengguna bertanggung jawab penuh atas penggunaan program ini. 