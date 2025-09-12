# Struktur Kontrol pada Python

## Pendahuluan

Struktur kontrol merupakan konsep dasar dalam pemrograman yang memungkinkan developer mengontrol alur eksekusi program. Dalam Python, terdapat dua jenis struktur kontrol utama: **struktur percabangan** (menggunakan if, elif, dan else) dan **struktur perulangan** (menggunakan while dan for).

Pemahaman yang baik tentang struktur kontrol sangat penting karena memungkinkan kita membuat program yang dapat mengambil keputusan berdasarkan kondisi tertentu serta melakukan tugas berulang secara efisien. Bab ini akan membahas kedua struktur kontrol tersebut secara mendalam dengan contoh-contoh praktis.

## Struktur Percabangan

Struktur percabangan adalah mekanisme dimana program akan menjalankan bagian kode yang berbeda tergantung pada nilai dari variabel kontrol atau kondisi tertentu. Dalam kehidupan sehari-hari, kita sering membuat keputusan berdasarkan kondisi - jika hujan, maka kita membawa payung; jika tidak, kita tidak membawanya. Konsep serupa diterapkan dalam pemrograman melalui struktur percabangan.

### Percabangan dengan `if`

Percabangan paling sederhana menggunakan statement `if`. Syntax dasarnya adalah:

```python
if kondisi:
    # kode yang dijalankan jika kondisi True
```

Kondisi biasanya berupa ekspresi yang menghasilkan nilai boolean (True atau False). Jika kondisi bernilai True, maka blok kode di dalam if akan dieksekusi.

Contoh:

```python
a = int(input('masukkan angka: '))
if a > 0:
    print(a, 'adalah bilangan positif')
```

**Penjelasan:**

- Program meminta user memasukkan sebuah angka
- Jika angka tersebut lebih besar dari 0 (positif), program akan menampilkan pesan bahwa angka tersebut positif
- Jika kondisi tidak terpenuhi (angka ≤ 0), program tidak akan melakukan apa-apa

**Output yang diharapkan:**

```text
masukkan angka: 5
5 adalah bilangan positif
```

```text
masukkan angka: -3
# Tidak ada output
```

### Percabangan dengan `if-else`

Percabangan if-else digunakan ketika kita memiliki dua kemungkinan keluaran yang berbeda. Syntax dasarnya:

```python
if kondisi:
    # kode jika kondisi True
else:
    # kode jika kondisi False
```

Contoh:

```python
a = int(input('masukkan angka: '))
if a > 0:
    print(a, 'adalah bilangan positif')
else:
    print(a, 'bukan bilangan positif')
```

**Penjelasan:**

- Jika angka lebih besar dari 0, program menampilkan pesan "bilangan positif"
- Jika tidak (angka ≤ 0), program menampilkan pesan "bukan bilangan positif"

**Output yang diharapkan:**

```text
masukkan angka: 5
5 adalah bilangan positif
```

```text
masukkan angka: -3
-3 bukan bilangan positif
```

```text
masukkan angka: 0
0 bukan bilangan positif
```

### Percabangan dengan `if-elif-else`

Ketika kita memiliki lebih dari dua kemungkinan keluaran, kita menggunakan kombinasi if-elif-else. Statement `elif` merupakan kependekan dari "else if". Syntax dasarnya:

```python
if kondisi1:
    # kode jika kondisi1 True
elif kondisi2:
    # kode jika kondisi2 True
else:
    # kode jika semua kondisi False
```

Kita bisa menambahkan elif sebanyak yang diperlukan.

Contoh:

```python
a = int(input('masukkan angka: '))
if a > 0:
    print(a, 'adalah bilangan positif')
elif a < 0:
    print(a, 'adalah bilangan negatif')
else:
    print('bilangan nol, atau zero')
```

**Penjelasan:**

- Program memeriksa kondisi secara berurutan
- Jika a > 0, tampilkan pesan positif dan selesai
- Jika tidak, periksa apakah a < 0, jika ya tampilkan pesan negatif
- Jika kedua kondisi tidak terpenuhi, jalankan kode di else (a harus sama dengan 0)

**Output yang diharapkan:**

```text
masukkan angka: 5
5 adalah bilangan positif
```

```text
masukkan angka: -3
-3 adalah bilangan negatif
```

```text
masukkan angka: 0
bilangan nol, atau zero
```

### Studi Kasus: Menentukan Bentuk Air Berdasarkan Suhu

Mari terapkan pengetahuan tentang percabangan untuk membuat program yang menentukan bentuk air berdasarkan suhu:

```python
suhu = float(input('Masukkan suhu air dalam Celsius: '))

if suhu <= 0:
    print('Pada suhu', suhu, 'C, air berada dalam bentuk padat (es)')
elif suhu > 0 and suhu < 100:
    print('Pada suhu', suhu, 'C, air berada dalam bentuk cair')
else:
    print('Pada suhu', suhu, 'C, air berada dalam bentuk gas (uap)')
```

**Output yang diharapkan:**

```text
Masukkan suhu air dalam Celsius: -5
Pada suhu -5.0 C, air berada dalam bentuk padat (es)
```

```text
Masukkan suhu air dalam Celsius: 25
Pada suhu 25.0 C, air berada dalam bentuk cair
```

```text
Masukkan suhu air dalam Celsius: 105
Pada suhu 105.0 C, air berada dalam bentuk gas (uap)
```

### Studi Kasus: Konversi Nilai Angka ke Huruf

Berikut contoh program untuk mengkonversi nilai angka menjadi nilai huruf:

```python
nilai = float(input('Masukkan nilai angka: '))

if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B'
elif nilai >= 70:
    grade = 'C'
elif nilai >= 60:
    grade = 'D'
else:
    grade = 'E'

print('Nilai huruf untuk', nilai, 'adalah', grade)
```

**Output yang diharapkan:**

```text
Masukkan nilai angka: 85
Nilai huruf untuk 85.0 adalah B
```

```text
Masukkan nilai angka: 72.5
Nilai huruf untuk 72.5 adalah C
```

```text
Masukkan nilai angka: 55
Nilai huruf untuk 55.0 adalah E
```

### Studi Kasus: Perhitungan Gaji Karyawan

Struktur percabangan tidak hanya untuk kondisi sederhana, tetapi juga dapat digunakan dalam perhitungan yang lebih kompleks, contoh:

```python
jam_kerja = int(input('Input jam kerja: '))
gaji_pokok = 1000000
posisi = input('Masukkan posisi (karyawan/manajer): ').lower()

if posisi == 'karyawan':
    gaji = gaji_pokok + jam_kerja * 10000
    print('Gaji {} tersebut: Rp. {:,}'.format(posisi, gaji))
elif posisi == 'manajer':
    gaji = gaji_pokok + jam_kerja * 15000
    print('Gaji {} tersebut: Rp. {:,}'.format(posisi, gaji))
else:
    print('Error, posisi tidak tersedia')
```

**Output yang diharapkan:**

```text
Input jam kerja: 40
Masukkan posisi (karyawan/manajer): karyawan
Gaji karyawan tersebut: Rp. 1,400,000
```

```text
Input jam kerja: 45
Masukkan posisi (karyawan/manajer): manajer
Gaji manajer tersebut: Rp. 1,675,000
```

```text
Input jam kerja: 35
Masukkan posisi (karyawan/manajer): supervisor
Error, posisi tidak tersedia
```

## Struktur Perulangan

Struktur perulangan memungkinkan kita mengeksekusi blok kode berulang kali tanpa harus menulis kode yang sama berulang-ulang. Python menyediakan dua jenis perulangan: `while` dan `for`.

### Perulangan `while`

Perulangan while digunakan untuk mengeksekusi blok kode selama kondisi tertentu terpenuhi (True). Perulangan ini cenderung digunakan ketika jumlah iterasi tidak pasti sebelumnya.

Syntax dasar:

```python
while kondisi:
    # kode yang diulang
```

Contoh:

```python
i = 1  # variabel kontrol
while i < 10:
    print(i)
    i += 1  # increment variabel kontrol
```

**Penjelasan:**

- Variabel i diinisialisasi dengan nilai 1
- Selama i < 10, blok kode dalam while akan dieksekusi
- Setiap iterasi, nilai i dicetak kemudian ditambah 1 (i += 1 sama dengan i = i + 1)
- Ketika i mencapai 10, kondisi i < 10 menjadi False dan perulangan berhenti

**Output yang diharapkan:**

```text
1
2
3
4
5
6
7
8
9
```

**Peringatan:** Dalam menggunakan while, kita harus berhati-hati terhadap infinite loop (perulangan tak berhingga) yang terjadi ketika kondisi selalu True dan tidak pernah menjadi False. Contoh infinite loop:

```python
# HATI-HATI: Jangan jalankan kode ini karena akan terjadi infinite loop
i = 1
while i < 10:
    print(i)
    # lupa menambah nilai i, sehingga i selalu < 10
```

### Perulangan `for`

Perulangan for digunakan untuk mengiterasi melalui sequence (seperti list, tuple, string) atau objek yang dapat diiterasi lainnya. For loop juga digunakan ketika jumlah iterasi sudah diketahui sebelumnya.

Syntax dasar:

```python
for variabel in sequence:
    # kode yang diulang
```

Contoh dengan list:

```python
arr = [1, 9, 4, 5]
for i in arr:
    print(i)
```

**Output yang diharapkan:**

```text
1
9
4
5
```

### Fungsi `range()` dalam Perulangan

Fungsi `range()` sangat berguna untuk menghasilkan deret angka dalam perulangan for. Fungsi ini memiliki tiga bentuk:

**Bentuk 1:** `range(stop)` - menghasilkan deret dari 0 hingga stop-1

```python
for i in range(5):
    print(i)
```

**Output:**

```text
0
1
2
3
4
```

**Bentuk 2:** `range(start, stop)` - menghasilkan deret dari start hingga stop-1

```python
for i in range(1, 6):
    print(i)
```

**Output:**

```text
1
2
3
4
5
```

**Bentuk 3:** `range(start, stop, step)` - menghasilkan deret dari start hingga stop-1 dengan increment step

```python
for i in range(1, 21, 4):
    print(i)
```

**Output:**

```text
1
5
9
13
17
```

Kita juga bisa menggunakan nilai negatif untuk step untuk menghitung mundur:

```python
for i in range(10, 0, -1):
    print(i)
```

**Output:**

```text
10
9
8
7
6
5
4
3
2
1
```

### Contoh Praktis: Countdown Timer

Mari gabungkan perulangan for dengan modul time untuk membuat countdown timer:

```python
from time import sleep

print("Countdown dimulai!")
for i in range(10, 0, -1):
    print(i)
    sleep(1)  # jeda 1 detik

print('Selamat Milad SMK!')
```

**Output yang diharapkan:**

```text
Countdown dimulai!
10
9
8
7
6
5
4
3
2
1
Selamat Milad SMK!
```

Program akan menampilkan angka dari 10 hingga 1 dengan jeda 1 detik antar angka, kemudian menampilkan pesan "Selamat Milad SMK!".

### Perulangan Bersarang (Nested Loop)

Kita dapat menempatkan perulangan di dalam perulangan lainnya, yang disebut nested loop. Teknik ini berguna untuk menangani data multidimensi atau membuat pola.

Contoh:

```python
for i in range(5):
    for j in range(1, 6):
        print(j, end=" ")
    print()
```

**Penjelasan:**

- Loop luar (variabel i) diulang 5 kali (i dari 0 hingga 4)
- Untuk setiap iterasi loop luar, loop dalam (variabel j) diulang 5 kali (j dari 1 hingga 5)
- Loop dalam mencetak nilai j diikuti spasi (end=" " membuat output tetap pada baris yang sama)
- Setelah loop dalam selesai, print() pindah ke baris baru

**Output yang diharapkan:**

```text
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
```

### Membuat Pola dengan Nested Loop

Dengan nested loop, kita bisa membuat berbagai pola menarik. Perhatikan contoh berikut:

```python
# Segitiga siku-siku
tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
```

**Output:**

```text
* 
* * 
* * * 
* * * * 
* * * * * 
```

```python
# Pola angka
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**Output:**

```text
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

### Kombinasi Percabangan dan Perulangan

Dalam pemrograman nyata, kita sering mengombinasikan percabangan dan perulangan untuk menyelesaikan masalah kompleks.

Contoh:

```python
for i in range(1, 5):
    if i % 2 == 0:
        print(i, "bilangan genap")
    else:
        print(i, "bilangan ganjil")
```

**Output:**

```text
1 bilangan ganjil
2 bilangan genap
3 bilangan ganjil
4 bilangan genap
```

Contoh lebih kompleks:

```python
# Mencari bilangan prima antara 1-20
print("Bilangan prima antara 1-20:")
for num in range(1, 21):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
```

**Output:**

```text
Bilangan prima antara 1-20:
2 3 5 7 11 13 17 19 
```

### Penggunaan `break` dan `continue`

Python menyediakan dua statement khusus untuk mengontrol alur perulangan: `break` dan `continue`.

**break:** Menghentikan paksa perulangan dan keluar dari blok perulangan

Contoh:

```python
while True:
    password = input("Masukkan password: ")
    if password == "python123":
        print("Password benar! Akses diberikan.")
        break
    else:
        print("Password salah. Coba lagi.")
```

**Output yang diharapkan:**

```text
Masukkan password: abc
Password salah. Coba lagi.
Masukkan password: 123
Password salah. Coba lagi.
Masukkan password: python123
Password benar! Akses diberikan.
```

**continue:** Melompati iterasi saat ini dan melanjutkan ke iterasi berikutnya

Contoh:

```python
for i in range(5):
    if i == 3:
        continue  # Lewati angka 3
    print(i, end=" ")
```

**Output:**

```text
0 1 2 4 
```

Contoh praktis:

```python
# Cetak bilangan ganjil antara 1-10
print("Bilangan ganjil antara 1-10:")
for num in range(1, 11):
    if num % 2 == 0:  # Jika genap, lewati
        continue
    print(num, end=" ")
```

**Output:**

```text
Bilangan ganjil antara 1-10:
1 3 5 7 9 
```

## Kesimpulan

Struktur kontrol adalah tulang punggung pemrograman yang memungkinkan kita membuat program yang cerdas dan efisien. Dalam bab ini, kita telah mempelajari:

1. **Struktur percabangan** (if, elif, else) untuk pengambilan keputusan berdasarkan kondisi
2. **Struktur perulangan** (while dan for) untuk mengeksekusi kode berulang kali
3. **Fungsi range()** untuk menghasilkan deret angka dalam perulangan
4. **Nested loop** untuk menangani masalah kompleks dan membuat pola
5. **Kombinasi percabangan dan perulangan** untuk menyelesaikan masalah dunia nyata
6. **Penggunaan break dan continue** untuk mengontrol alur perulangan

Pemahaman yang solid tentang konsep-konsep ini akan menjadi fondasi yang kuat untuk mempelajari topik pemrograman Python yang lebih advanced di bab-bab berikutnya.

## Latihan

1. Buat program yang mencetak papan catur 8x8 dengan simbol "O" dan "X"
2. Buat program yang menerima input angka dan mengecek apakah angka tersebut prima
3. Buat program yang mensimulasikan mesin ATM dengan menu untuk cek saldo, tarik tunai, dan setor tunai
4. Buat program yang menghasilkan segitiga Pascal dengan tinggi tertentu
5. Buat program game tebak angka dimana komputer memilih angka acak antara 1-9, pemain harus menebaknya dan tiap pemain diberi 3 kesempatan
