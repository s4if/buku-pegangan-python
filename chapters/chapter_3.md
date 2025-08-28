# Bahasa Pemrograman

## Cara Kerja Komputer

Komputer pada dasarnya adalah sebuah mesin elektronik yang hanya dapat menjalankan operasi-operasi sederhana, seperti penjumlahan, pengurangan, perbandingan, atau pemindahan data. Namun, dengan kecepatan pemrosesan yang sangat tinggi, operasi sederhana ini dapat dirangkai menjadi tugas-tugas yang kompleks.

Komputer tidak memiliki kecerdasan alami. Tanpa instruksi dari manusia, komputer hanyalah perangkat keras yang tidak dapat melakukan apa pun. Oleh karena itu, diperlukan **program** untuk mengarahkan komputer melakukan tugas tertentu. Program inilah yang menjadikan komputer bermanfaat, baik untuk perhitungan matematika, pengolahan teks, pengendalian robot, hingga menjalankan aplikasi sehari-hari.

## Bahasa Natural vs Bahasa Pemrograman

Sebelum membahas bahasa pemrograman, mari kita pahami terlebih dahulu apa itu bahasa.

**Bahasa** adalah sarana untuk mengekspresikan atau menyampaikan pemikiran, ide, maupun instruksi. Manusia menggunakan bahasa alami (natural language) seperti Bahasa Indonesia atau Bahasa Inggris untuk berkomunikasi.

Komputer pun memiliki "bahasanya" sendiri. Bahasa komputer paling dasar disebut **bahasa mesin (machine language)**, yaitu kumpulan instruksi biner berupa angka 0 dan 1.

Bahasa mesin sangat sulit dipahami manusia karena terlalu sederhana dan tidak menyerupai bahasa alami. Komputer dapat diibaratkan seperti hewan sirkus: ia hanya bisa melakukan apa yang diperintahkan, tanpa inisiatif. Semua kemampuan yang terlihat "pintar" pada komputer sebenarnya adalah hasil dari instruksi yang dibuat oleh manusia.

Kumpulan instruksi yang dapat dijalankan oleh sebuah komputer disebut **Instruction Set** (daftar instruksi).

## Komponen Bahasa

Setiap bahasa, baik bahasa manusia maupun bahasa pemrograman, memiliki komponen penting yang serupa:

| Komponen      | Penjelasan                                                                                                                                    |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Alphabet**  | Simbol-simbol dasar yang digunakan untuk membentuk bahasa. Dalam bahasa pemrograman, alphabet bisa berupa huruf, angka, maupun simbol khusus. |
| **Lexis**     | Kumpulan kata atau istilah dalam sebuah bahasa. Dalam pemrograman, ini berupa kata kunci (keyword) dan identifier.                            |
| **Syntax**    | Aturan penyusunan simbol atau kata sehingga membentuk pernyataan yang valid.                                                                  |
| **Semantics** | Aturan yang menentukan makna dari susunan kata atau instruksi yang dibuat.                                                                    |

Contohnya, dalam Python kita menuliskan:

```python
print("Halo Dunia")
```

* **Alphabet**: huruf `p`, `r`, `i`, `n`, `t`, tanda kurung, dan tanda kutip.
* **Lexis**: kata `print` adalah keyword bawaan Python.
* **Syntax**: penulisan fungsi harus menggunakan tanda kurung.
* **Semantics**: instruksi ini bermakna “tampilkan teks Halo Dunia ke layar”.

## Evolusi Bahasa Pemrograman

Awalnya, manusia berinteraksi langsung dengan komputer menggunakan **bahasa mesin**. Namun, bahasa ini sulit dipahami dan rawan kesalahan.

Untuk mempermudah, dibuatlah **bahasa rakitan (assembly language)** yang menggunakan singkatan (mnemonic) seperti `MOV`, `ADD`, atau `JMP` sebagai pengganti kode biner.

Meski assembly lebih mudah dipahami daripada bahasa mesin, tetap saja terlalu teknis. Maka kemudian berkembanglah **bahasa pemrograman tingkat tinggi** yang lebih dekat dengan bahasa manusia, seperti C, Java, Python, atau PHP.

Kode yang ditulis oleh manusia dalam bahasa pemrograman disebut **source code**, dan disimpan dalam sebuah **source file** (misalnya: `program.py`, `main.cpp`). Source code ini tidak bisa langsung dijalankan komputer, tetapi harus diterjemahkan terlebih dahulu ke dalam bahasa mesin.

## Dari Bahasa Pemrograman ke Bahasa Mesin

Agar source code dapat dieksekusi oleh komputer, ia harus diterjemahkan ke bahasa mesin. Proses ini dapat dilakukan dengan dua pendekatan utama:

1. **Kompilasi (Compilation)**
   Source code diterjemahkan sekaligus menjadi file program yang bisa dijalankan secara langsung.

2. **Interpretasi (Interpretation)**
   Source code dibaca dan dijalankan baris demi baris setiap kali program dijalankan.

Ada pula pendekatan **Hybrid** yang menggabungkan keduanya, seperti Java dan C#. Dalam bahasa ini, source code dikompilasi terlebih dahulu menjadi *bytecode*, lalu dijalankan oleh mesin virtual (misalnya Java Virtual Machine). Hal ini memungkinkan portabilitas yang lebih tinggi.

### Compilation

Dalam metode kompilasi:

* Source code diterjemahkan sekali, menghasilkan file **executable** (misalnya `program.exe` di Windows atau `program` di Linux).
* File executable ini dapat dijalankan berkali-kali tanpa perlu menerjemahkan ulang.
* Jika source code diubah, maka harus dikompilasi ulang.
* Program penerjemah yang digunakan disebut **compiler**.

**Contoh bahasa yang menggunakan kompilasi:**

* C
* C++
* Rust
* Go
* Pascal

### Interpretation

Dalam metode interpretasi:

* Kode program tidak diterjemahkan sekaligus, melainkan baris demi baris saat dijalankan.
* Proses ini dilakukan oleh **interpreter**.
* Program yang menggunakan interpretasi biasanya harus didistribusikan bersama interpreter.

**Contoh bahasa berbasis interpretasi:**

* Python
* JavaScript
* PHP
* Ruby

### Perbandingan Compilation dan Interpretation

| Aspek                    | Compilation                                                                | Interpretation                                                  |
| ------------------------ | -------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **Kecepatan Eksekusi**   | Lebih cepat karena sudah menjadi file biner.                               | Lebih lambat karena harus diterjemahkan saat runtime.           |
| **Distribusi**           | Hanya file hasil kompilasi yang perlu dibagikan.                           | Harus menyertakan interpreter di komputer pengguna.             |
| **Portabilitas**         | Harus dikompilasi ulang untuk sistem operasi atau arsitektur yang berbeda. | Cukup membutuhkan interpreter yang tersedia di berbagai sistem. |
| **Keamanan Source Code** | Source code tidak langsung terlihat.                                       | Source code biasanya terbuka bagi pengguna.                     |

## Tingkatan Bahasa Pemrograman

Bahasa pemrograman dapat diklasifikasikan menjadi tiga tingkatan:

1. **Bahasa Tingkat Rendah (Low-Level Language)**

   * Sangat dekat dengan mesin.
   * Biasanya berupa bahasa rakitan (assembly).
   * Contoh instruksi: `MOV`, `SUB`, `JMP`.
   * Digunakan untuk pemrograman sistem, driver perangkat keras, atau optimasi performa.

2. **Bahasa Tingkat Menengah (Middle-Level Language)**

   * Menggabungkan konsep bahasa rendah dan tinggi.
   * C adalah contoh klasik, karena dapat digunakan untuk mengakses hardware sekaligus menulis program aplikasi.

3. **Bahasa Tingkat Tinggi (High-Level Language)**

   * Mendekati bahasa manusia dan lebih mudah dipahami.
   * Banyak menyediakan abstraksi sehingga programmer tidak perlu memikirkan detail mesin.
   * Contoh: Python, Java, C++, PHP, Kotlin, JavaScript.

## Penutup

Bahasa pemrograman merupakan jembatan antara manusia dan komputer. Tanpa bahasa pemrograman, komputer tidak akan bisa digunakan untuk menyelesaikan tugas-tugas kompleks yang saat ini sudah menjadi bagian penting dalam kehidupan sehari-hari.

Pemahaman tentang sejarah, evolusi, serta tingkatan bahasa pemrograman membantu kita menyadari bahwa perkembangan teknologi tidak terjadi seketika, melainkan melalui proses panjang. Dari kode biner sederhana, kita kini memiliki bahasa pemrograman tingkat tinggi yang memudahkan siapa pun belajar menjadi seorang programmer.
