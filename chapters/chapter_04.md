# Bahasa Pemrograman Python

## Apa itu Python?

**Python** adalah bahasa pemrograman interpretatif yang bersifat **multiguna (general-purpose programming language)**. Artinya, Python dapat digunakan untuk berbagai macam kebutuhan, mulai dari pengembangan aplikasi desktop, aplikasi web, hingga pengolahan data dan kecerdasan buatan.

Python memiliki filosofi utama: **fokus pada kejelasan kode**. Bahasa ini dirancang agar mudah dipelajari, mudah dibaca, dan mudah digunakan kembali. Karena sifatnya yang sederhana namun kuat, Python menjadi salah satu bahasa pemrograman yang paling populer di dunia saat ini.

Python pertama kali diciptakan oleh **Guido van Rossum** pada akhir tahun 1980-an di Centrum Wiskunde & Informatica (CWI), Belanda. Nama "Python" bukan berasal dari ular, melainkan terinspirasi dari acara komedi Inggris **“Monty Python's Flying Circus”**.

Rilis resmi pertama Python terjadi pada tahun **1991**. Sejak itu Python terus berkembang dengan komunitas yang sangat aktif. Saat ini, versi terbaru Python yang stabil adalah **Python 3.x** (per Agustus 2025, versi stabil terbaru adalah **Python 3.13**). Versi Python 2 sudah **tidak lagi didukung (end of life)** sejak Januari 2020.

## Tujuan dan Filosofi Python

Pada tahun 1999, Guido van Rossum merumuskan tujuan utama Python sebagai berikut:

1. Python harus **mudah dan intuitif**, tetapi tetap **powerful**.
2. Python harus **open source**, sehingga dapat digunakan dan dikembangkan oleh siapa pun.
3. Kode Python harus mudah dibaca dan dipahami, layaknya bahasa Inggris sederhana.
4. Python harus cocok untuk menyelesaikan **tugas sehari-hari**.

Prinsip dasar ini kemudian dituangkan dalam filosofi Python yang dikenal dengan **The Zen of Python**, yang dapat dilihat langsung di interpreter Python dengan mengetik:

```python
import this
```

## Penggunaan Python

Python digunakan secara luas di berbagai bidang, antara lain:

* **Aplikasi Desktop (GUI):**
  Menggunakan pustaka seperti Tkinter, PyQt, atau Kivy.

* **Pengembangan Web:**
  Framework populer seperti **Flask** dan **Django** memungkinkan pembuatan aplikasi web modern dengan cepat.

* **Pengolahan Data & Analisis Ilmiah:**
  Pustaka seperti **NumPy**, **Pandas**, dan **Matplotlib** menjadikan Python bahasa utama dalam data science.

* **Kecerdasan Buatan (Artificial Intelligence) & Machine Learning:**
  Dengan pustaka seperti **TensorFlow**, **PyTorch**, dan **scikit-learn**, Python mendominasi bidang AI.

* **Internet of Things (IoT):**
  Python dapat dijalankan pada perangkat kecil seperti **Raspberry Pi** atau **MicroPython** pada mikrokontroler.

* **Automasi & Scripting:**
  Python banyak digunakan untuk menulis skrip otomatisasi di sistem operasi, server, maupun jaringan.

## Kelebihan dan Kekurangan Python

**Kelebihan Python:**

* **Mudah dipelajari:** Sintaks Python sederhana dan mirip bahasa manusia.
* **Mudah diajarkan:** Sangat cocok sebagai bahasa pertama untuk pemula.
* **Mudah digunakan:** Banyak pustaka bawaan dan eksternal yang siap pakai.
* **Mudah dipahami:** Kode lebih ringkas, lebih sedikit tanda baca dibanding C/C++ atau Java.
* **Mudah didapatkan & diinstal:** Python gratis, tersedia di berbagai platform (Windows, macOS, Linux).
* **Komunitas besar:** Dukungan dokumentasi dan forum sangat banyak.

**Kekurangan Python:**

* **Lebih lambat dibanding bahasa kompilasi** (misalnya C atau Rust), karena merupakan bahasa interpretatif.
* **Kurang cocok untuk aplikasi yang membutuhkan performa sangat tinggi** (misalnya game engine atau sistem real-time kritis).
* **Manajemen memori otomatis (garbage collection)** kadang membuat performa tidak stabil untuk tugas tertentu.

## Python 2 vs Python 3

Sebelum 2008, Python yang banyak digunakan adalah Python 2. Namun, pada tahun 2008, Python 3 dirilis dengan banyak perubahan besar yang tidak sepenuhnya kompatibel dengan Python 2.

Sejak **Januari 2020**, Python 2 **tidak lagi didukung**. Semua pengembangan Python berfokus pada **Python 3**.

Dalam pembelajaran dan praktikum pemrograman dasar, **Python 3** selalu digunakan karena:

* Mendapatkan dukungan penuh.
* Lebih aman.
* Lebih banyak pustaka modern yang kompatibel.

## Persiapan Menggunakan Python

Untuk menggunakan Python, kita perlu menginstal **Python Runtime**.

* **Windows:**
  Python dapat diunduh dari [python.org](https://www.python.org/downloads/) dan dipasang langsung.

* **Linux & macOS:**
  Umumnya Python sudah tersedia bawaan, namun bisa diperbarui melalui package manager.

Setelah instalasi, Python dapat dijalankan melalui:

* **IDLE (Integrated Development and Learning Environment)** bawaan Python.
* **Terminal/Command Prompt** dengan mengetik:

```bash
python
```

atau

```bash
python3
```

## Contoh Program Sederhana

Berikut contoh program Python untuk menerima input nama dan menampilkan sapaan:

```python
nama = input("Masukkan nama: ")
print("Halo", nama)
```

**Penjelasan kode:**

* `input()` digunakan untuk membaca input dari pengguna.
* `print()` digunakan untuk menampilkan output ke layar.

Jika pengguna mengetik **Budi**, maka hasilnya:

```text
Masukkan nama: Budi
Halo Budi
```
