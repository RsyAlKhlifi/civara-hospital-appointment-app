# CIVARA HOSPITAL Aplikasi Pendaftaran & Janji Temu Dokter

Aplikasi desktop untuk pendaftaran pasien dan pembuatan janji temu dokter secara online, dibangun dengan **Python** dan **Tkinter/CustomTkinter**. Dilengkapi panel admin terpisah untuk mengelola data booking dan rating.

Proyek akhir mata kuliah **Pemrograman Dasar**, Program Studi S1 Sains Data, Universitas Negeri Surabaya (Kelompok 7).

---

## Latar Belakang

Proses pendaftaran dan janji temu dokter di rumah sakit umumnya masih dilakukan secara manual/offline, menyebabkan antrean panjang, ketidakpastian jadwal praktik dokter, dan kesulitan akses bagi pasien di daerah terpencil. **CIVARA HOSPITAL** dibuat untuk memudahkan pasien melakukan pendaftaran dan booking jadwal dokter secara online, lengkap dengan nomor antrean berbentuk QR code.
## Fitur

**Sisi Pasien**
- Login & registrasi akun
- Dashboard (sejarah, visi misi, tentang, penghargaan)
- Menu navigasi (home, poli, fasilitas, FAQ, rating)
- **6 Poli**: gigi, umum, anak, jantung, penyakit dalam, mata — masing-masing dengan beberapa pilihan dokter
- **Fasilitas rumah sakit**: rawat inap, ICU, ruang bayi, radiologi, laboratorium, farmasi, gizi, ruang bersalin, rehabilitasi medik
- FAQ (pertanyaan umum)
- Rating pelayanan & tempat
- Riwayat pesanan (nama pemesan, dokter, jadwal, nomor antrean, dan **QR code** untuk dicetak di rumah sakit)

**Sisi Admin** (`admin_apk_7.py`)
- Login admin terpisah
- Melihat & mengelola data booking per poli (gigi, anak, jantung, mata, penyakit dalam, umum)
- Melihat data rating dari pasien

## Tech Stack

- **Python 3**
- **Tkinter** & **CustomTkinter** — UI
- **Pillow (PIL)** — pengolahan gambar
- **tkcalendar** — widget kalender untuk pemilihan jadwal
- **JSON** — penyimpanan data (tanpa database eksternal)

## Struktur Repo

```
.
├── PROJEK_AKHIR_PEMDAS_KELOMPOK_7.py   # Aplikasi utama (sisi pasien)
├── admin_apk_7.py                       # Panel admin
├── assets/                              # Gambar UI (lihat catatan di bawah)
├── data/                                # File JSON (dibuat otomatis saat aplikasi dijalankan)
└── README.md
```

> **Catatan tentang asset gambar**: Aplikasi ini menggunakan banyak file gambar (background, dashboard, foto dokter, ikon fasilitas, dll). Foto profil dokter dalam repo ini **tidak disertakan** karena merupakan foto stock yang hanya dipakai sebagai data dummy demo, dan tidak pantas didistribusikan ulang tanpa izin. Ikon, logo, dan gambar generik (background, panah navigasi, ikon fasilitas) boleh tetap ada di `assets/`.
>
> Untuk menjalankan aplikasi secara utuh, siapkan sendiri gambar dengan nama file berikut dan letakkan pada direktori kerja aplikasi:
> - `background.png`, `rumahsakit.png`, `rumahsakit3.jpg`, `contact.png`, `logoprofil.jpg`, `profil.jpg`, `menu.jpg`, `menu2.jpg`, `panah.png`, `panah2.png`, `hide_image.png`, `show_image.png`, `barcode.jpg`
> - Dashboard: `dasboard5.jpg`, `dashboard6.jpg`, `dashboard7.jpg`, `dashboard9.jpg`, `komponen1-4.png`, `sertif1.jpg`, `sertif2.jpg`
> - Fasilitas: `farmasi.png`, `icu.png`, `laboratorium.png`, `radiologi.png`, `rawat inap .png`, `rehabilitas medik.png`, `ruang bayi.png`, `ruang bersalin.png`
> - Ikon poli: `gbr poli anak.png`, `gbr poli gigi.png`, `gbr poli jantung.png`, `gbr poli mata.png`, `gbr poli penyakit dalam.png`, `gbr poli umum.png`
> - Foto dokter (nama file sesuai kode, contoh): `dr. celine.png`, `dr. david.png`, `drg.Johnson, Sp.Ort.png`, dll — bisa diganti avatar generik atau inisial
> - Admin: `admin.jpg`, `admin2.jpg`

## Cara Menjalankan

1. **Clone repo**
```bash
   git clone https://github.com/<username>/civara-hospital-tkinter.git
   cd civara-hospital-tkinter
```

2. **Install dependensi**
```bash
   pip install customtkinter pillow tkcalendar
```
   > `tkinter` biasanya sudah bawaan Python. Jika belum ada (umumnya di Linux), install lewat package manager, mis. `sudo apt install python3-tk`.

3. **Siapkan gambar** sesuai daftar di atas pada direktori yang sama dengan file `.py` (atau sesuaikan path di kode).

4. **Jalankan aplikasi pasien**
```bash
   python civara-hospital-appointment-app_main code.py
```

5. **Jalankan panel admin** (terpisah)
```bash
   python admin_apk_7.py
```

## Penyimpanan Data

Aplikasi ini **tidak menggunakan database**, melainkan menyimpan data ke file JSON yang dibuat/dibaca otomatis saat aplikasi berjalan:

| File | Isi |
|---|---|
| `accounts5.json` | Akun pasien (username, password) |
| `additional_info.json` | Informasi tambahan profil pasien |
| `poli_gigi2.json`, `poli_anak2.json`, `poli_jantung2.json`, `poli_mata2.json`, `poli_penyakit_dalam2.json`, `poli_umum2.json` | Data booking per poli |
| `pesanan user.json` | Riwayat pesanan pasien (untuk fitur QR code & nomor antrean) |
| `rating2.json` | Data rating pelayanan & tempat |

File-file ini akan otomatis dibuat saat aplikasi pertama kali dijalankan, sehingga **tidak perlu diupload ke repo** (lihat `.gitignore`).

## Saran Pengembangan

- Migrasi penyimpanan dari JSON ke database (SQLite/PostgreSQL) untuk skalabilitas dan mencegah *race condition* saat banyak proses membaca/menulis file yang sama
- Hash password (mis. dengan `bcrypt`) — saat ini akun disimpan sebagai teks biasa
- Refactor kode: pisahkan tiap poli/dokter (yang saat ini banyak fungsi berulang seperti `poli_gigi_jhonson()`, `poli_gigi_Alicia()`, dst.) menjadi satu fungsi generik dengan parameter
- Validasi input pada form registrasi dan booking

## Tim (Kelompok 7)

1. Moh. Rasya Al Khalifi (24031554132) 
2. Dewanggi Erchinta Dwi Putri (24031554034) 
3. Variesa Sabita Mumtaza Habib (24031554083)

Program Studi S1 Sains Data, Fakultas Matematika dan Ilmu Pengetahuan Alam, Universitas Negeri Surabaya

## Lisensi

Proyek ini dibuat untuk keperluan akademik.
