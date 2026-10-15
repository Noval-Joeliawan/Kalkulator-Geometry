# 📐 Kalkulator Geometri Interaktif (2D & 3D)

Aplikasi kalkulator dan visualisasi geometri terpadu berbasis antarmuka grafis (GUI) Python Tkinter. Aplikasi ini dirancang untuk mempermudah pemahaman konsep bangun datar dan ruang melalui fitur perhitungan matematis, visualisasi interaktif, serta fungsi inversi rumus.

---

## ✨ Fitur Utama

- **Dual-Mode Visualizer (2D & 3D)**:
  - **Mode 2D (Sketsa Teknis)**: Menampilkan sketsa bidang datar lengkap dengan garis bantu dimensi (tinggi, diagonal, panjang, dan alas).
  - **Mode 3D (Interaktif)**: Visualisasi proyeksi bangun ruang yang dapat diputar secara otomatis maupun digerakkan secara manual (*drag mouse*).
- **Perhitungan Lengkap Bangun Geometri**:
  - Mendukung berbagai bangun: Persegi, Persegi Panjang, Segitiga, Lingkaran, Jajar Genjang, Belah Ketupat, Layang-layang, Trapesium, Oval, dan Tabung.
  - Perhitungan Luas dan Keliling secara presisi.
- **Fungsi Invers (Perhitungan Balik)**:
  - Menghitung panjang sisi, jari-jari, alas, atau tinggi jika nilai luas atau keliling sudah diketahui.
- **Navigasi Single-Window**:
  - Perpindahan halaman yang mulus dan responsif menggunakan sistem *frame switching* tanpa membuka terminal baru.

---

## 🚀 Panduan Penggunaan

### 1. Menjalankan Melalui Python

Pastikan Python versi 3.8 ke atas telah terpasang di komputer Anda.

1. Unduh atau *clone* repositori ini:
   ```bash
   git clone https://github.com/username/kalkulator-geometri.git
   cd kalkulator-geometri
   ```

2. Jalankan file utama:
   ```bash
   python app.py
   ```
   *(Aplikasi menggunakan pustaka bawaan standar Python: `tkinter` dan `math`, sehingga tidak memerlukan instalasi pustaka eksternal untuk sekadar dijalankan).*

---

### 2. Kompilasi ke Format Executable (.exe)

Untuk membuat file aplikasi biner mandiri (.exe) di sistem operasi Windows:

1. Pasang alat build:
   ```bash
   pip install -r requirements.txt
   ```

2. Eksekusi proses kompilasi:
   ```bash
   pyinstaller --noconsole --onefile app.py
   ```

3. File siap pakai akan tersimpan di dalam folder `dist/app.exe`.

---

## 📁 Struktur Direktori

```text
├── app.py                # Skrip utama aplikasi
├── requirements.txt      # Dependensi untuk pembuatan file .exe
├── README.md             # Dokumentasi proyek
└── .gitignore            # Daftar pengecualian berkas Git
```

---

## 📝 Catatan Proyek

Dibuat sebagai proyek pembelajaran pemrograman antarmuka grafis (GUI) dan matematika terapan.