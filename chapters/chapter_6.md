# Operator pada Python

## Pendahuluan

Dalam pemrograman Python, operator merupakan simbol-simbol khusus yang digunakan untuk melakukan operasi tertentu pada nilai dan variabel. Memahami berbagai jenis operator merupakan hal fundamental dalam belajar pemrograman, karena operator memungkinkan kita melakukan manipulasi data, perbandingan, dan operasi logika yang menjadi dasar pembuatan program yang kompleks.

Pada bab ini, kita akan membahas empat jenis operator utama dalam Python: operator aritmatika, operator perbandingan, operator logika, dan operator gabungan. Setiap jenis operator memiliki fungsi dan kegunaan spesifik yang akan kita pelajari dengan detail.

## Operator Aritmatika

Operator aritmatika adalah operator yang digunakan untuk melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, dan pembagian. Operator-operator ini bekerja pada nilai numerik (integer dan float) dan menghasilkan hasil sesuai operasi yang dilakukan.

Berikut adalah contoh implementasi operator aritmatika dalam Python:

```python
# Meminta input dari pengguna
a = int(input("a: "))
b = int(input("b: "))

# Operasi aritmatika dasar
c = a + b  # Penjumlahan
d = a - b  # Pengurangan
e = a * b  # Perkalian (menggunakan * bukan x)
f = a / b  # Pembagian biasa (hasilnya float)

# Menampilkan hasil operasi
print(a, "+", b, "=", c)
print(a, "-", b, "=", d)
print(a, "*", b, "=", e)
print(a, "/", b, "=", f)
print("tipe dari f:", type(f))  # Menunjukkan tipe data hasil pembagian

# Pembagian bulat (floor division)
g = a // b  # Membulatkan hasil pembagian ke bawah
print(a, "//", b, "=", g)
print("tipe dari g:", type(g))

# Modulus (sisa hasil bagi)
h = a % b  # Menghasilkan sisa dari pembagian
print(a, "%", b, "=", h)

# Pemangkatan
i = a ** b  # Memangkatkan a dengan b
print(a, "**", b, "=", i)
```

**Interaksi dan Output:**

```text
(user memasukkan nilai 7 dan 3)
a: 7
b: 3
7 + 3 = 10
7 - 3 = 4
7 * 3 = 21
7 / 3 = 2.3333333333333335
tipe dari f: <class 'float'>
7 // 3 = 2
tipe dari g: <class 'int'>
7 % 3 = 1
7 ** 3 = 343
```

**Penjelasan Detail:**

Operator aritmatika adalah dasar dari semua operasi matematika dalam pemrograman. Python menyediakan berbagai operator aritmatika yang fungsinya mirip dengan matematika biasa, tetapi dengan beberapa penyesuaian sintaks.

- **Penjumlahan (+)**: Menambahkan dua nilai. Contoh: `5 + 3` menghasilkan `8`
- **Pengurangan (-)**: Mengurangi nilai kedua dari nilai pertama. Contoh: `5 - 3` menghasilkan `2`
- **Perkalian (\*)**: Mengalikan dua nilai. Dalam pemrograman, simbol yang digunakan adalah asterisk (*) bukan huruf x. Contoh: `5 * 3` menghasilkan `15`
- **Pembagian (/)**: Membagi nilai pertama dengan nilai kedua. Hasilnya selalu bertipe float meskipun kedua operand adalah integer. Contoh: `5 / 2` menghasilkan `2.5`

Python juga menyediakan operator aritmatika khusus:

- **Pembagian Bulat (//)**: Juga disebut floor division, operator ini membagi dua bilangan dan membulatkan hasilnya ke bilangan bulat terdekat yang lebih kecil. Contoh: `5 // 2` menghasilkan `2` (bukan 2.5)
- **Modulus (%)**: Menghasilkan sisa dari pembagian dua bilangan. Operator ini sangat berguna untuk menentukan apakah sebuah bilangan genap atau ganjil, atau untuk operasi siklus. Contoh: `5 % 2` menghasilkan `1`
- **Pemangkatan (**)**: Memangkatkan bilangan pertama dengan bilangan kedua. Contoh: `2 ** 3` menghasilkan `8` (2 pangkat 3)

Penting untuk memahami tipe data hasil dari setiap operasi. Operasi pembagian biasa (/) selalu menghasilkan nilai float, bahkan jika hasilnya adalah bilangan bulat. Sementara operasi pembagian bulat (//) akan menghasilkan integer jika kedua operand adalah integer, tetapi bisa menghasilkan float jika salah satu operand adalah float.

## Operator Perbandingan

Operator perbandingan digunakan untuk membandingkan dua nilai dan menghasilkan nilai boolean (True atau False). Operator ini sangat penting dalam pengambilan keputusan dalam program, seperti dalam struktur percabangan (if-else) dan perulangan.

```python
# Operator perbandingan menghasilkan nilai boolean (True/False)
a = 3 == 3  # Sama dengan: True jika kedua nilai sama
b = 4 < 2   # Kurang dari: True jika nilai pertama kurang dari nilai kedua
c = 5 != 7  # Tidak sama dengan: True jika kedua nilai berbeda
d = 9 >= 10 # Lebih besar atau sama dengan: True jika nilai pertama lebih besar atau sama dengan nilai kedua

print(a, b, c, d)  # Menampilkan hasil perbandingan

# Perbedaan antara < dan <=
e = 7 < 7   # Kurang dari: False karena 7 tidak kurang dari 7
f = 7 <= 7  # Kurang dari atau sama dengan: True karena 7 sama dengan 7

print(e, f)  # Menampilkan hasil perbandingan
```

**Output:**

```text
True False True False
False True
```

**Penjelasan Detail:**

Operator perbandingan memungkinkan kita membuat keputusan dalam program dengan membandingkan nilai-nilai. Hasil dari operasi perbandingan selalu berupa boolean (True atau False), yang kemudian dapat digunakan untuk mengontrol alur program.

Berikut adalah operator perbandingan dalam Python:

- **Sama dengan (==)**: Mengecek apakah dua nilai sama. Contoh: `5 == 5` menghasilkan `True`, `5 == 3` menghasilkan `False`
- **Tidak sama dengan (!=)**: Mengecek apakah dua nilai berbeda. Contoh: `5 != 3` menghasilkan `True`, `5 != 5` menghasilkan `False`
- **Lebih besar dari (>)**: Mengecek apakah nilai pertama lebih besar dari nilai kedua. Contoh: `5 > 3` menghasilkan `True`, `3 > 5` menghasilkan `False`
- **Lebih kecil dari (<)**: Mengecek apakah nilai pertama lebih kecil dari nilai kedua. Contoh: `3 < 5` menghasilkan `True`, `5 < 3` menghasilkan `False`
- **Lebih besar atau sama dengan (>=)**: Mengecek apakah nilai pertama lebih besar atau sama dengan nilai kedua. Contoh: `5 >= 5` menghasilkan `True`, `5 >= 3` menghasilkan `True`, `3 >= 5` menghasilkan `False`
- **Lebih kecil atau sama dengan (<=)**: Mengecek apakah nilai pertama lebih kecil atau sama dengan nilai kedua. Contoh: `3 <= 3` menghasilkan `True`, `3 <= 5` menghasilkan `True`, `5 <= 3` menghasilkan `False`

Perhatikan perbedaan antara operator `=` dan `==`. Operator `=` adalah operator penugasan (assignment) yang digunakan untuk memberikan nilai ke variabel, sementara `==` adalah operator perbandingan yang digunakan untuk mengecek kesamaan dua nilai.

## Operator Logika

Operator logika digunakan untuk menggabungkan atau memanipulasi nilai boolean (True dan False). Operator ini sangat penting untuk membuat kondisi yang lebih kompleks dalam struktur kendali program.

```python
# Operator logika bekerja dengan nilai boolean
a = True and True   # AND: True jika kedua nilai True
b = True and False  # AND: False jika salah satu False
c = True or False   # OR: True jika salah satu True
d = False or False  # OR: False jika kedua nilai False

# Menampilkan hasil dengan separator khusus
print(a, b, c, d, sep='__--__')

# Operator NOT untuk membalik nilai boolean
e = not True  # NOT: Membalik nilai True menjadi False
print(e)
```

**Output:**

```text
True__--__False__--__True__--__False
False
```

**Penjelasan Detail:**

Operator logika memungkinkan kita menggabungkan beberapa kondisi menjadi satu ekspresi yang lebih kompleks. Terdapat tiga operator logika utama dalam Python:

- **AND**: Operator ini menghasilkan True hanya jika kedua operand bernilai True. Jika salah satu atau kedua operand False, hasilnya akan False. Bayangkan seperti syarat yang sangat ketat dimana semua kondisi harus terpenuhi.
  
  | A | B | A AND B |
  |---|---|---------|
  | True | True | True |
  | True | False | False |
  | False | True | False |
  | False | False | False |

- **OR**: Operator ini menghasilkan True jika setidaknya satu operand bernilai True. Hasilnya hanya False jika kedua operand False. Bayangkan seperti syarat yang longgar dimana hanya perlu satu kondisi yang terpenuhi.
  
  | A | B | A OR B |
  |---|---|--------|
  | True | True | True |
  | True | False | True |
  | False | True | True |
  | False | False | False |

- **NOT**: Operator ini membalik nilai boolean dari operandnya. Jika operand True, hasilnya False, dan sebaliknya. Operator ini hanya bekerja pada satu operand (unary operator).
  
  | A | NOT A |
  |---|-------|
  | True | False |
  | False | True |

Operator logika sering digunakan dalam struktur percabangan untuk membuat kondisi yang kompleks. Misalnya: `if age >= 18 and has_id:` akan menghasilkan True hanya jika kedua kondisi terpenuhi (usia minimal 18 tahun DAN memiliki kartu identitas).

## Operator Gabungan

Operator gabungan (atau compound operators) adalah operator yang menggabungkan operasi aritmatika atau operasi lainnya dengan operasi penugasan. Operator ini memberikan cara yang lebih singkat untuk melakukan operasi dan penugasan nilai pada variabel yang sama.

```python
# Operator gabungan menggabungkan operasi dengan penugasan
a = 0
a += 1  # Sama dengan: a = a + 1
print(a)  # Menampilkan hasil

b = 2
b -= 1  # Sama dengan: b = b - 1
print(b)  # Menampilkan hasil
```

**Output:**

```text
1
1
```

**Penjelasan Detail:**

Operator gabungan menyederhanakan ekspresi yang melibatkan operasi pada variabel dan penugasan kembali hasilnya ke variabel yang sama. Daripada menulis `a = a + 1`, kita dapat menulis `a += 1` yang lebih ringkas dan mudah dibaca.

Berikut adalah berbagai operator gabungan dalam Python:

- **+= (Penugasan Penjumlahan)**: Menambahkan nilai ke variabel dan menugaskan hasilnya kembali ke variabel tersebut. Contoh: `a += 5` setara dengan `a = a + 5`
- **-= (Penugasan Pengurangan)**: Mengurangi nilai variabel dan menugaskan hasilnya kembali. Contoh: `a -= 3` setara dengan `a = a - 3`
- ***= (Penugasan Perkalian)**: Mengalikan variabel dengan nilai dan menugaskan hasilnya kembali. Contoh: `a *= 2` setara dengan `a = a * 2`
- **/= (Penugasan Pembagian)**: Membagi variabel dengan nilai dan menugaskan hasilnya kembali. Contoh: `a /= 4` setara dengan `a = a / 4`
- **//= (Penugasan Pembagian Bulat)**: Membagi bulat variabel dengan nilai dan menugaskan hasilnya kembali. Contoh: `a //= 2` setara dengan `a = a // 2`
- **%= (Penugasan Modulus)**: Melakukan operasi modulus pada variabel dan menugaskan hasilnya kembali. Contoh: `a %= 3` setara dengan `a = a % 3`
- ****= (Penugasan Pemangkatan)**: Memangkatkan variabel dengan nilai dan menugaskan hasilnya kembali. Contoh: `a **= 2` setara dengan `a = a ** 2`

Operator gabungan tidak hanya membuat kode lebih ringkas, tetapi juga dapat meningkatkan performa dalam beberapa kasus, karena variabel hanya diakses sekali saja.

## Kesimpulan

Operator adalah komponen fundamental dalam Python yang memungkinkan kita melakukan manipulasi data, perbandingan, dan operasi logika. Dalam bab ini, kita telah mempelajari empat jenis operator utama:

1. **Operator aritmatika** untuk melakukan operasi matematika dasar
2. **Operator perbandingan** untuk membandingkan nilai dan menghasilkan boolean
3. **Operator logika** untuk bekerja dengan nilai boolean dan membuat kondisi kompleks
4. **Operator gabungan** untuk menyederhanakan operasi dan penugasan nilai

Pemahaman yang solid tentang berbagai jenis operator ini sangat penting untuk membangun program Python yang efektif dan efisien. Dengan menguasai operator-operator ini, kita telah melangkah lebih jauh dalam perjalanan belajar pemrograman Python.

Pada bab-bab selanjutnya, kita akan melihat bagaimana operator-operator ini digunakan dalam konteks yang lebih praktis, seperti dalam struktur kontrol percabangan dan perulangan, yang merupakan fondasi dari pembuatan program yang dinamis dan interaktif.

## Tugas

**Buatlah Program untuk:**

- Mengkonversi suhu dari Celcius ke Fahrenheit! (input: suhu)
- Menhitung Luas Sisi dari sebuah Silinder (input: jari-jari dan tinggi)
- Menghitung Volume dari Bola (input: jari2) rumus: `4/3 pi * r * pangkat 3`
- Menghitung Energi Kinetik dari suatu benda (input: massa(m) dan kecepatan(v), rumus: e = setengah m kali v kuadrat)
