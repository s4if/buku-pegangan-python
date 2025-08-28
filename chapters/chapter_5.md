# Dasar Pemrograman Python

## Pendahuluan

Python adalah bahasa pemrograman tingkat tinggi yang mudah dipelajari dan banyak digunakan untuk berbagai keperluan seperti pengembangan web, analisis data, kecerdasan buatan, dan automasi. Bab ini akan membahas konsep-konsep dasar pemrograman Python yang perlu dikuasai oleh pemula.

## Statement (Pernyataan)

**Statement** adalah instruksi atau perintah yang diberikan kepada Python untuk melakukan suatu tindakan. Setiap statement biasanya ditulis dalam satu baris kode.

```python
print("ini adalah statement")
nama = "Saiful"
print(nama)
```

**Penjelasan:**

- Baris pertama menggunakan fungsi `print()` untuk menampilkan teks "ini adalah statement"
- Baris kedua membuat variabel `nama` dan menyimpan nilai "Saiful" di dalamnya
- Baris ketiga menampilkan nilai yang disimpan dalam variabel `nama`

**Output :**

```text
ini adalah statement
Saiful
```

Setiap statement dalam Python dieksekusi secara berurutan dari atas ke bawah. Python membaca dan menjalankan kode baris demi baris, sehingga urutan penulisan kode sangat penting.

## Indentasi dan Scope

**Indentasi** (penulisan menjorok ke dalam) dalam Python bukan hanya masalah estetika, tetapi memiliki makna penting yang menentukan **scope** (ruang lingkup) suatu blok kode.

```python
print("Halo")
for i in range(3):
    print(i)  # bagian dari loop for

x = 5
if x < 4:
    print("kecil")  # bagian dari if
    print(x)        # masih bagian dari if
print("selesai")    # sudah di luar blok if
```

**Penjelasan:**

- Statement yang sejajar dengan margin kiri (tanpa indentasi) adalah main scope
- Statement yang memiliki indentasi (biasanya 4 spasi) adalah bagian dari blok kode di atasnya
- Loop `for` dan percabangan `if` memerlukan indentasi untuk menandai blok kode yang menjadi bagiannya

**Output :**

```text
Halo
0
1
2
selesai
```

Python menggunakan indentasi untuk mengetahui kode mana yang termasuk dalam blok tertentu. Ini berbeda dengan bahasa pemrograman lain yang menggunakan kurung kurawal `{}` untuk menandai blok kode. Konsistensi dalam penggunaan indentasi sangat penting agar kode dapat berjalan dengan benar.

## Komentar

**Komentar** adalah teks dalam kode yang tidak dieksekusi oleh Python. Komentar digunakan untuk memberikan penjelasan, dokumentasi, atau menonaktifkan sementara bagian kode.

```python
# komentar adalah teks yang tidak akan dibaca oleh python
print("setelah ini komentar")  # komentar bisa ditulis setelah statement
```

**Penjelasan:**

- Komentar diawali dengan tanda `#`
- Teks setelah tanda `#` tidak akan diproses oleh Python
- Komentar dapat ditulis di baris tersendiri atau setelah statement

Komentar sangat penting untuk membuat kode yang mudah dipahami, baik oleh diri sendiri maupun orang lain. Dengan komentar yang baik, kita dapat menjelaskan logika atau tujuan dari suatu bagian kode.

## Fungsi Dasar: print()

Fungsi `print()` digunakan untuk menampilkan output ke terminal atau konsol. Fungsi ini sangat penting untuk debugging dan menampilkan informasi kepada pengguna.

### Penggunaan Dasar print()

```python
print("Halo Dunia")
x = "Bumi"
print("Selamat datang di", x)
```

**Output :**

```text
Halo Dunia
Selamat datang di Bumi
```

### Mengubah Karakter Akhir (end)

Secara default, `print()` akan menambahkan newline (`\n`) di akhir output, tetapi kita dapat mengubahnya dengan parameter `end`.

```python
print("Perkenalkan, nama saya", end=" ")
print("Saiful Habib")

print("Kab. Magelang", end="__--__")
print("Jawa", end="-->><<--")
print("Tengah")
```

**Output :**

```text
Perkenalkan, nama saya Saiful Habib
Kab. Magelang__--__Jawa-->><<--Tengah
```

### Mengubah Pemisah Nilai (sep)

Secara default, `print()` memisahkan multiple values dengan spasi, tetapi kita dapat mengubahnya dengan parameter `sep`.

```python
a = 3
b = "kali"
c = "3 sama dengan"
print(a, b, c, 9)  # default separator

print(a, b, c, 9, sep=")]>-<[(")  # custom separator
```

**Output :**

```text
3 kali 3 sama dengan 9
3)]>-<[(kali)]>-<[(3 sama dengan)]>-<[(9
```

Fungsi `print()` sangat fleksibel dan dapat disesuaikan dengan kebutuhan output yang diinginkan.

## Fungsi Dasar: input()

Fungsi `input()` digunakan untuk menerima masukan dari pengguna melalui keyboard. Input tersebut kemudian dapat diproses lebih lanjut dalam program.

```python
nama = input()  # input tanpa petunjuk
print("halo", nama)

kelas = input("masukkan kelas: ")  # input dengan petunjuk
print("kamu kelas", kelas)
```

**Contoh interaksi dan output:**

```text
(users mengetik: Ihsan)
halo Ihsan
masukkan kelas: 10 TJTK1
kamu kelas 10 TJKT1
```

Fungsi `input()` selalu mengembalikan nilai dalam bentuk string, meskipun pengguna memasukkan angka. Jika membutuhkan tipe data lain, kita perlu mengkonversinya.

## Variabel dan Aturan Penamaan

**Variabel** adalah tempat penyimpanan data dalam memori yang memiliki nama dan nilai. Nama variabel digunakan untuk mengakses nilai yang disimpan.

```python
a = 1
b = 2
c = a + b
print(a, "+", b, "=", c)
```

**Output :**

```text
1 + 2 = 3
```

### Aturan Penamaan Variabel

Python memiliki aturan tertentu dalam penamaan variabel:

1. **Hanya boleh mengandung huruf, angka, dan underscore (_)**

   ```python
   nama = "ihsan"
   Nama2 = "upin"
   nama_3 = "ipin"
   # $nama4 = "fizi"  # Error: simbol $ tidak diperbolehkan
   ```

2. **Tidak boleh diawali dengan angka**

   ```python
   3serangkai = "Douwes Dekker"  # Error: tidak boleh diawali angka
   ```

3. **Tidak boleh mengandung spasi**

   ```python
   smk it = "Ihsanul Fikri"  # Error: spasi tidak diperbolehkan
   ```

4. **Tidak boleh menggunakan kata kunci Python (reserved words)**

   ```python
   for = 3  # Error: for adalah kata kunci Python
   ```

Python adalah case-sensitive, artinya variabel `Nama` dan `nama` dianggap sebagai dua variabel yang berbeda.

## Tipe Data

Setiap nilai dalam Python memiliki tipe data tertentu. Pemahaman tentang tipe data penting untuk operasi dan pengolahan data yang benar dalam program.

### Tipe Data Dasar

Python memiliki beberapa tipe data dasar yang penting untuk dipahami:

1. **Integer (bilangan bulat)**:

   ```python
   a = 4  # integer (bilangan bulat)
   ```

   - Digunakan untuk menyimpan bilangan bulat positif/negatif
   - Contoh: 0, 10, -5, 1000
   - Tidak memiliki batasan ukuran (kecuali memori sistem)

2. **Float (bilangan pecahan)**:

   ```python
   b = 4.4  # float (bilangan pecahan)
   ```

   - Digunakan untuk menyimpan bilangan real/pecahan
   - Contoh: 3.14, -0.001, 2.0
   - Memiliki presisi sekitar 15-17 digit desimal

3. **String (teks)**:

   ```python
   c = "4"  # string (teks)
   ```

   - Digunakan untuk menyimpan data teks
   - Diapit tanda kutip (bisa tunggal ' atau ganda ")
   - Contoh: "hello", '123', "Python"
   - Meskipun berisi angka, jika diapit kutip maka tipe datanya string

4. **Boolean (True/False)**:

   ```python
   d = (4 == 4)  # boolean (True/False)
   ```

   - Hanya memiliki dua nilai: True atau False
   - Sering digunakan dalam percabangan dan perulangan
   - Hasil dari operasi perbandingan (==, !=, >, <, dll)

Untuk mengecek tipe data suatu variabel, kita bisa menggunakan fungsi `type()`:

```python
print("variable a bertipe", type(a), "dengan nilai", a)
print("variable b bertipe", type(b), "dengan nilai", b)
print("variable c bertipe", type(c), "dengan nilai", c)
print("variable d bertipe", type(d), "dengan nilai", d)
```

**Output :**

```text
variable a bertipe <class 'int'> dengan nilai 4
variable b bertipe <class 'float'> dengan nilai 4.4
variable c bertipe <class 'str'> dengan nilai 4
variable d bertipe <class 'bool'> dengan nilai True
```

Fungsi `type()` mengembalikan objek tipe data dari variabel yang diperiksa. Dalam Python, semua tipe data sebenarnya adalah objek (kelas), sehingga outputnya berupa `<class 'tipe_data'>`.

**Output :**

```text
variable a bertipe <class 'int'> dengan nilai 4
variable b bertipe <class 'float'> dengan nilai 4.4
variable c bertipe <class 'str'> dengan nilai 4
variable d bertipe <class 'bool'> dengan nilai True
```

### Konversi Tipe Data

Kadang kita perlu mengubah tipe data dari satu bentuk ke bentuk lain, seperti mengubah string menjadi integer:

```python
# Mengubah input string menjadi integer
a = int(input("masukkan a: "))
b = int(input("masukkan b: "))
c = a + b
print(a, "+", b, "=", c)
```

**Contoh interaksi dan output:**

```text
masukkan a: 5
masukkan b: 3
5 + 3 = 8
```

Fungsi konversi tipe data yang umum digunakan:

- `int()`: mengubah menjadi integer
- `float()`: mengubah menjadi float
- `str()`: mengubah menjadi string
- `bool()`: mengubah menjadi boolean

## Kesimpulan

Dalam bab ini, kita telah mempelajari dasar-dasar pemrograman Python meliputi statement, indentasi, komentar, fungsi dasar `print()` dan `input()`, variabel, dan tipe data. Konsep-konsep ini merupakan fondasi penting untuk mempelajari topik-topik yang lebih advanced dalam Python.

Pemahaman yang kuat tentang dasar-dasar ini akan memudahkan kita dalam mempelajari struktur kontrol, fungsi, modul, dan konsep pemrograman lainnya yang akan dibahas dalam bab-bab selanjutnya.

## Latihan

1. Buat program yang meminta nama dan usia pengguna, kemudian tampilkan pesan sambutan yang menyertakan informasi tersebut
2. Buat program kalkulator sederhana yang meminta dua angka dan menampilkan hasil penjumlahan, pengurangan, perkalian, dan pembagian
3. Coba berbagai variasi parameter `sep` dan `end` pada fungsi `print()` untuk memahami fungsinya dengan lebih baik

Dengan berlatih secara konsisten, kemampuan pemrograman Python Anda akan semakin terasah dan berkembang.
