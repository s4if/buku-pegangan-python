# String di Python

## Apa itu String?

**String** adalah tipe data yang digunakan untuk menyimpan teks.
String ditulis dengan tanda kutip tunggal `'...'` atau ganda `"..."`.

Contoh:

```python
teks1 = "Halo"
teks2 = 'Python'
print(teks1, teks2)
```

Output:

```text
Halo Python
```

## Operasi Dasar pada String

### Menggabungkan String (Concatenation)

Dua string bisa digabung dengan operator `+`.

```python
nama = "Andi"
sapaan = "Halo " + nama
print(sapaan)
```

Output:

```text
Halo Andi
```

### Mengulang String

String bisa dikalikan dengan integer (`*`).

```python
print("Hi! " * 3)
```

Output:

```text
Hi! Hi! Hi!
```

## String sebagai Array (Indexing & Slicing)

String di Python bisa diakses seperti array, yaitu berdasarkan **indeks** (dimulai dari 0).

### Indexing

```python
teks = "Python"
print(teks[0])   # P
print(teks[3])   # h
```

Output:

```text
P
h
```

### Slicing

Mengambil bagian tertentu dari string.

```python
teks = "Informatika"
print(teks[0:5])   # Infor
print(teks[5:])    # matika
print(teks[:4])    # Info
```

Output:

```text
Infor
matika
Info
```

## Fungsi Penting untuk String

### `len()`

Menghitung panjang string.

```python
teks = "Python"
print(len(teks))   # 6
```

Output:

```text
6
```

### Ubah ke huruf besar / kecil

* `upper()` -> jadi huruf besar semua
* `lower()` -> jadi huruf kecil semua
* `title()` -> huruf pertama tiap kata besar

```python
teks = "belajar python"
print(teks.upper())   # BELAJAR PYTHON
print(teks.lower())   # belajar python
print(teks.title())   # Belajar Python
```

Output:

```text
BELAJAR PYTHON
belajar python
Belajar Python
```

### Menghapus spasi di awal/akhir

* `strip()` -> hapus spasi di kiri dan kanan
* `lstrip()` -> hapus spasi kiri
* `rstrip()` -> hapus spasi kanan

```python
teks = "   Halo Dunia   "
print(teks.strip())   # "Halo Dunia"
```

Output:

```text
Halo Dunia
```

### Memecah string (`split()`)

Digunakan untuk memecah string berdasarkan pemisah (default: spasi).

```python
kalimat = "Saya suka Python"
kata = kalimat.split()
print(kata)   # ['Saya', 'suka', 'Python']
```

Output:

```text
['Saya', 'suka', 'Python']
```

Dengan pemisah lain:

```python
data = "apel,jeruk,mangga"
buah = data.split(",")
print(buah)   # ['apel', 'jeruk', 'mangga']
```

Output:

```text
['apel', 'jeruk', 'mangga']
```

### Menggabungkan list jadi string (`join()`)

Kebalikan dari `split()`.

```python
kata = ["Belajar", "Python", "Menyenangkan"]
kalimat = " ".join(kata)
print(kalimat)
```

Output:

```text
Belajar Python Menyenangkan
```

### Mengganti teks (`replace()`)

```python
teks = "Saya suka Java"
print(teks.replace("Java", "Python"))
```

Output:

```text
Saya suka Python
```

### Mengecek isi string

* `startswith()` -> cek apakah string diawali teks tertentu
* `endswith()` -> cek apakah string diakhiri teks tertentu
* `isdigit()` -> cek apakah isinya angka
* `isalpha()` -> cek apakah isinya huruf

```python
teks = "12345"
print(teks.isdigit())   # True
print(teks.isalpha())   # False
```

Output:

```text
True
False
```

## Format String

Kadang kita ingin menampilkan teks yang berisi variabel.
Gunakan `f-string` (format string).

```python
nama = "Budi"
umur = 16
print(f"Halo, nama saya {nama}, umur saya {umur} tahun.")
```

Output:

```text
Halo, nama saya Budi, umur saya 16 tahun.
```

## Multi-line String

String pada umumnya terdiri dari 1 baris saja, akan tetapi saat butuh strng multibars, string bisa dibuat dengan tiga tanda kutip (`'''...'''` atau `"""..."""`).

Contoh:

```python
teks = """Ini adalah
string dengan
beberapa baris."""
print(teks)
```

Output:

```text
Ini adalah
string dengan
beberapa baris.
```

## Escape Character pada String

Kadang kita perlu menampilkan karakter khusus dalam string, seperti tanda kutip, baris baru, atau tab. Untuk itu, gunakan **escape character** dengan tanda backslash (`\`).

### Macam-macam Escape Character

| Escape | Fungsi                        |
|--------|-------------------------------|
| `\'`   | Menampilkan tanda `'`         |
| `\"`   | Menampilkan tanda `"`         |
| `\n`   | Baris baru                    |
| `\t`   | Tab                           |
| `\\`   | Garis miring terbalik (`\`)   |

### Contoh Penggunaan

Menampilkan tanda kutip di dalam string:

```python
print('Abdullah ibnu Mas\'ud')
print("Dia berkata: \"Python itu mudah!\"")
```

Output:

```text
Abdullah ibnu Mas'ud
Dia berkata: "Python itu mudah!"
```

Membuat baris baru dengan `\n`:

```python
print('baris_satu\nbaris_dua\nbaris_tiga')
```

Output:

```text
baris_satu
baris_dua
baris_tiga
```

Membuat tabel sederhana dengan tab (`\t`):

```python
print('|\tno\t|\tNama\t|\tKelas\t|')
print('|\t1\t|\tAdin\t|\tTKJ1\t|')
print('|\t2\t|\tJack\t|\tTKJ1\t|')
```

Output:

```text
|   no  | Nama | Kelas |
|   1   | Adin | TKJ1  |
|   2   | Jack | TKJ1  |
```
