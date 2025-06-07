# Winbox MAC Login Bruteforce Tool

## Deskripsi Program
Program ini adalah simulasi tool untuk melakukan brute force login pada perangkat Mikrotik melalui protokol Winbox menggunakan MAC address. Program ini menggunakan pendekatan wordlist-based untuk mencoba kombinasi username dan password.

## Komponen Program

### 1. Fungsi Utama
```python
def try_mac_login(mac_addr, username, password):
```
- Fungsi ini mensimulasikan proses login ke perangkat Mikrotik
- Parameter:
  - `mac_addr`: Alamat MAC target
  - `username`: Username yang akan dicoba
  - `password`: Password yang akan dicoba
- Return: `True` jika login berhasil, `False` jika gagal

### 2. Fungsi Main
```python
def main():
```
- Mengatur parameter bruteforce:
  - MAC target: "4C:5E:0C:12:34:56"
  - Username: "admin"
  - Password: Diambil dari file "wordlist.txt"

## Cara Kerja Program

1. **Inisialisasi**
   - Program membaca daftar password dari file "wordlist.txt"
   - Menentukan MAC address target dan username

2. **Proses Bruteforce**
   - Membaca password satu per satu dari wordlist
   - Mencoba login dengan kombinasi username dan password
   - Menampilkan hasil setiap percobaan

3. **Output**
   - `[+]` : Menunjukkan percobaan login
   - `[✓]` : Menunjukkan login berhasil
   - `[✗]` : Menunjukkan login gagal
   - `[!]` : Menunjukkan semua percobaan gagal

## Penggunaan Program

### Prasyarat
1. File `wordlist.txt` yang berisi daftar password
2. Python 3.x

### Format Wordlist
- Satu password per baris
- Tidak ada karakter khusus atau spasi
- Contoh isi wordlist.txt:
  ```
  admin
  admin123
  password
  123456
  ```

### Cara Menjalankan
```bash
python winbox-mac.py
```

## Catatan Penting

1. **Simulasi**
   - Program ini adalah simulasi dan tidak melakukan koneksi nyata
   - Dalam implementasi nyata, perlu menggunakan raw socket untuk Layer 2
   - Port yang digunakan seharusnya 20561

2. **Keamanan**
   - Program ini hanya untuk tujuan edukasi
   - Hanya gunakan pada perangkat yang Anda miliki
   - Perhatikan hukum dan regulasi yang berlaku

3. **Pembatasan**
   - Delay 0.3 detik antara setiap percobaan
   - Hanya mensimulasikan keberhasilan untuk password "admin123"
   - Tidak melakukan pengecekan format MAC address

## Pengembangan Selanjutnya

1. **Fitur yang Dapat Ditambahkan**
   - Implementasi koneksi Layer 2 yang sebenarnya
   - Validasi format MAC address
   - Dukungan untuk multiple username
   - Progress bar
   - Opsi untuk mengatur delay
   - Logging ke file

2. **Peningkatan Keamanan**
   - Enkripsi wordlist
   - Rate limiting
   - Timeout handling
   - Error handling yang lebih baik

## Penulis
- Versi: 1.0
- Tujuan: Edukasi dan Pengujian Keamanan

## Catatan
Program ini adalah simulasi dan tidak melakukan koneksi nyata ke perangkat. Untuk implementasi nyata, diperlukan modifikasi untuk menggunakan raw socket dan protokol Layer 2 yang sesuai. 