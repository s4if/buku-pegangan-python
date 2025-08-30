# Fungsi pada Python

## Pendahuluan tentang Fungsi

Dalam pemrograman Python, **fungsi** merupakan blok kode terorganisir yang dapat digunakan kembali untuk melakukan tugas tertentu. Konsep fungsi sangat fundamental dalam pemrograman karena memungkinkan kita menerapkan prinsip **Code Reuse** (Penggunaan Kembali Kode).

Bayangkan Anda ingin membuat program yang harus menampilkan pesan yang sama berulang-ulang dengan variasi kecil. Tanpa fungsi, Anda harus menulis ulang kode yang hampir sama berulang kali. Ini tidak hanya tidak efisien tetapi juga rentan kesalahan. Dengan fungsi, Anda cukup menulis kode sekali dan memanggilnya kapan saja diperlukan.

### Keuntungan Menggunakan Fungsi

1. **Mengurangi Duplikasi Kode**: Menghindari penulisan kode yang sama berulang kali.
2. **Meningkatkan Keterbacaan**: Memecah program menjadi bagian-bagian kecil yang lebih mudah dipahami.
3. **Memudahkan Pemeliharaan**: Perubahan cukup dilakukan di satu tempat (dalam fungsi) dan akan berlaku untuk semua pemanggilan fungsi.
4. **Modularitas**: Memungkinkan pengembangan program secara modular dengan membagi tugas besar menjadi sub-tugas kecil.

### Contoh Tanpa Fungsi

Perhatikan kode berikut yang menampilkan pesan perkenalan untuk tiga orang berbeda:

```python
print('Halo!')
print('Nama Saya Saiful,')
print('apa kabarmu hari ini?')

print('Halo!')
print('Nama Saya Ihsanul,')
print('apa kabarmu hari ini?')

print('Halo!')
print('Nama Saya Fikri,')
print('apa kabarmu hari ini?')
```

**Output:**

```text
Halo!
Nama Saya Saiful,
apa kabarmu hari ini?
Halo!
Nama Saya Ihsanul,
apa kabarmu hari ini?
Halo!
Nama Saya Fikri,
apa kabarmu hari ini?
```

Meskipun kode ini bekerja dengan benar, terdapat banyak duplikasi kode. Jika kita ingin mengubah format pesan, kita harus mengubahnya di tiga tempat berbeda.

### Contoh dengan Fungsi

Sekarang perhatikan implementasi yang sama menggunakan fungsi:

```python
def halo(nama):
    print('Halo!')
    print('Nama Saya {},'.format(nama))
    print('apa kabarmu hari ini?')

halo('Saiful')
halo('Ihsanul')
halo('Fikri')
```

**Output:**

```text
Halo!
Nama Saya Saiful,
apa kabarmu hari ini?
Halo!
Nama Saya Ihsanul,
apa kabarmu hari ini?
Halo!
Nama Saya Fikri,
apa kabarmu hari ini?
```

Output yang dihasilkan sama persis, tetapi kode jauh lebih efisien. Jika kita ingin mengubah format pesan, cukup ubah dalam fungsi `halo` dan perubahan akan berlaku untuk semua pemanggilan.

## Mendefinisikan dan Memanggil Fungsi

### Struktur Dasar Fungsi

Fungsi dalam Python didefinisikan menggunakan kata kunci `def` diikuti nama fungsi dan tanda kurung yang berisi parameter (jika ada). Blok kode fungsi ditandai dengan indentasi.

```python
def nama_fungsi(parameter1, parameter2):
    """
    Docstring (opsional) - penjelasan tentang fungsi
    """
    # Blok kode fungsi
    # Bisa berisi logika, perhitungan, dll.
    return hasil  # Opsional - nilai yang dikembalikan
```

### Komponen Fungsi

1. **def**: Kata kunci untuk mendefinisikan fungsi
2. **nama_fungsi**: Identifier yang mengikuti aturan penamaan Python
3. **Parameter**: Variabel yang menerima nilai dari pemanggil (opsional)
4. **Docstring**: String dokumentasi yang menjelaskan fungsi (opsional)
5. **Blok kode**: Inti fungsi yang dieksekusi saat dipanggil
6. **return**: Pernyataan untuk mengembalikan nilai (opsional)

### Memanggil Fungsi

Fungsi dipanggil dengan menyebutkan namanya diikuti argumen dalam tanda kurung:

```python
nama_fungsi(argumen1, argumen2)
```

**Contoh Praktis:**

```python
def sapa(nama):
    """Fungsi untuk menyapa pengguna"""
    print(f"Halo {nama}! Selamat datang di program Python.")

sapa("Budi")
```

**Output:**

```text
Halo Budi! Selamat datang di program Python.
```

## Parameter dan Argumen Fungsi

Parameter adalah variabel yang ditentukan dalam definisi fungsi, sedangkan argumen adalah nilai aktual yang diteruskan ke fungsi saat dipanggil.

### Parameter Biasa

Parameter biasa mengharuskan pemanggil menyediakan argumen sesuai dengan jumlah dan urutan yang ditentukan.

```python
def perkenalan(nama, asal):
    print("Perkenalkan, nama saya {}, asal saya dari {}".format(nama, asal))

perkenalan("Ihsan Fikri", "Magelang")
```

**Output:**

```teks
Perkenalkan, nama saya Ihsan Fikri, asal saya dari Magelang
```

Jika jumlah argumen tidak sesuai dengan parameter, akan terjadi error:

```python
perkenalan("Ihsan")  # Error: kurang satu argumen
```

**Output:**

```teks
TypeError: perkenalan() missing 1 required positional argument: 'asal'
```

### Parameter dengan Nilai Default

Parameter dapat memiliki nilai default yang digunakan jika argumen tidak disediakan.

```python
def print_nama(n_depan, n_keluarga="-"):
    print("Perkenalkan, nama saya {} {}.".format(n_depan, n_keluarga))

print_nama('Saiful', 'Habib')
print_nama(n_keluarga='Hizutome', n_depan='Rakuro')
print_nama('Sutardjo')
```

**Output:**

```text
Perkenalkan, nama saya Saiful Habib.
Perkenalkan, nama saya Rakuro Hizutome.
Perkenalkan, nama saya Sutardjo -.
```

### Parameter Arbitrary (*args)

Parameter `*args` memungkinkan fungsi menerima sejumlah argumen variabel yang diakses sebagai tuple.

```python
def print_anak(*data_anak):
    for anak in data_anak:
        print('nama: {}'.format(anak))
    print('----<<')

print_anak()
print_anak('Muhammad')
print_anak('Ismail', 'Ishaq')
print_anak('Ihsan', 'Fikri', 'Fiki')
```

**Output:**

```text
----<<
nama: Muhammad
----<<
nama: Ismail
nama: Ishaq
----<<
nama: Ihsan
nama: Fikri
nama: Fiki
----<<
```

### Keyword Arbitrary Parameter (**kwargs)

Parameter `**kwargs` memungkinkan fungsi menerima sejumlah argumen dengan keyword yang diakses sebagai dictionary.

```python
def pesanan(**items):
    total = 0
    print('<--- Pesanan : Harga --->')
    for key in items.keys():
        print('{} : {}'.format(key, items[key]))
        total += items[key]
        
    print('Total: {}\n'.format(total))

pesanan(es_teh=3000, bakso=10000, krupuk=1000)
print('>--------<')
pesanan(es_jeruk=4000, mie_ayam=8000, tempe=500)
```

**Output:**

```text
<--- Pesanan : Harga --->
es_teh : 3000
bakso : 10000
krupuk : 1000
Total: 14000

>--------<
<--- Pesanan : Harga --->
es_jeruk : 4000
mie_ayam : 8000
tempe : 500
Total: 12500
```

## Nilai Kembali (Return Value)

### Konsep Return

Fungsi dapat mengembalikan nilai menggunakan pernyataan `return`. Nilai yang dikembalikan dapat digunakan dalam ekspresi atau disimpan dalam variabel.

```python
def fahrenheit(c):
    offset = 32  # Geser di suhu 0
    f = c * 9 / 5 + offset
    return f

suhu_dieng = fahrenheit(9)
print('Suhu nang Dieng ki {} derajat fahrenheit.'.format(suhu_dieng))
print('Temperature in Singapore now is {} degree fahrenheit'.format(fahrenheit(21)))
print('Suhu di Jakarta sekarang {} fahrenheit'.format(fahrenheit(40)))
```

**Output:**

```text
Suhu nang Dieng ki 48.2 derajat fahrenheit.
Temperature in Singapore now is 69.8 degree fahrenheit
Suhu di Jakarta sekarang 104.0 fahrenheit
```

### Fungsi dengan Multiple Return

Fungsi dapat memiliki beberapa pernyataan return yang dieksekusi berdasarkan kondisi.

```python
def cek_angka(x):
    if x > 0:
        return "Positif"
    elif x < 0:
        return "Negatif"
    else:
        return "Nol"

print(cek_angka(5))   # Positif
print(cek_angka(-3))  # Negatif
print(cek_angka(0))   # Nol
```

**Output:**

```text
Positif
Negatif
Nol
```

### Multiple Return Values

Python mendukung pengembalian multiple values dalam bentuk tuple.

```python
def hitung(a, b):
    tambah = a + b
    kali = a * b
    return tambah, kali

x, y = hitung(3, 4)
print("Jumlah:", x)
print("Perkalian:", y)

# Alternatif: menerima sebagai tuple
hasil = hitung(5, 6)
print("Hasil sebagai tuple:", hasil)
```

**Output:**

```text
Jumlah: 7
Perkalian: 12
Hasil sebagai tuple: (11, 30)
```

## Best Practices dalam Penulisan Fungsi

### Penamaan Fungsi yang Baik

Gunakan nama yang deskriptif dan konsisten:

- Gunakan lowercase dengan underscore untuk pemisah kata
- Pilih nama yang mencerminkan tujuan fungsi

**Contoh Baik:**

```python
def hitung_rata_rata(nilai_list):
    # kode fungsi
```

**Contoh Kurang Baik:**

```python
def hr(nl):
    # kode fungsi
```

### Fungsi yang Terfokus

Setiap fungsi sebaiknya melakukan satu tugas tertentu. Ini membuat fungsi lebih mudah dipahami, diuji, dan dipelihara.

**Contoh Baik:**

```python
def hitung_rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)

def tentukan_kelulusan(rata_rata):
    return rata_rata >= 75
```

**Contoh Kurang Baik:**

```python
def proses_nilai(nilai_list):
    # Menghitung rata-rata dan menentukan kelulusan
    rata_rata = sum(nilai_list) / len(nilai_list)
    if rata_rata >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"
```

### Dokumentasi Fungsi

Gunakan docstring untuk menjelaskan tujuan, parameter, dan nilai kembali fungsi.

```python
def hitung_pangkat(angka, pangkat=2):
    """
    Menghitung pangkat dari sebuah angka.
    
    Parameters:
    angka (float/int): Angka yang akan dipangkatkan
    pangkat (float/int): Nilai pangkat (default 2)
    
    Returns:
    float/int: Hasil perpangkatan
    """
    return angka ** pangkat

# Mengakses docstring
print(hitung_pangkat.__doc__)
```

## 6. Studi Kasus: Aplikasi Kalkulator Sederhana

Mari terapkan konsep fungsi untuk membuat kalkulator sederhana:

```python
def tambah(a, b):
    """Menambahkan dua bilangan"""
    return a + b

def kurang(a, b):
    """Mengurangi a dengan b"""
    return a - b

def kali(a, b):
    """Mengalikan dua bilangan"""
    return a * b

def bagi(a, b):
    """Membagi a dengan b"""
    if b == 0:
        return "Error: Pembagian dengan nol"
    return a / b

def kalkulator(operasi, a, b):
    """Fungsi utama kalkulator"""
    if operasi == '+':
        return tambah(a, b)
    elif operasi == '-':
        return kurang(a, b)
    elif operasi == '*':
        return kali(a, b)
    elif operasi == '/':
        return bagi(a, b)
    else:
        return "Error: Operasi tidak valid"

# Testing kalkulator
print("10 + 5 =", kalkulator('+', 10, 5))
print("10 - 5 =", kalkulator('-', 10, 5))
print("10 * 5 =", kalkulator('*', 10, 5))
print("10 / 5 =", kalkulator('/', 10, 5))
print("10 / 0 =", kalkulator('/', 10, 0))
print("10 % 5 =", kalkulator('%', 10, 5))  # Operasi tidak valid
```

**Output:**

```text
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2.0
10 / 0 = Error: Pembagian dengan nol
10 % 5 = Error: Operasi tidak valid
```

## Kesimpulan

Fungsi adalah blok bangunan fundamental dalam pemrograman Python yang memungkinkan:

- Pengorganisasian kode yang lebih baik
- Penggunaan kembali kode (code reuse)
- Pemecahan masalah kompleks menjadi sub-masalah kecil
- Pemeliharaan dan debugging yang lebih mudah

Dengan memahami berbagai jenis parameter (biasa, default, *args, **kwargs) dan cara mengembalikan nilai (return), Anda dapat membuat fungsi yang fleksibel dan powerful. Praktik terbaik seperti penamaan yang jelas, fungsi yang terfokus, dan dokumentasi yang baik akan membuat kode Anda lebih profesional dan mudah dipahami.

Penguasaan fungsi adalah langkah penting menuju pemrograman yang lebih advanced termasuk pemrograman berorientasi objek dan pengembangan aplikasi yang kompleks.
