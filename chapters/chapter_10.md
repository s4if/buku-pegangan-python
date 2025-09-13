# Struktur Data di Python

## Pendahuluan

Dalam pemrograman, data merupakan elemen fundamental yang menjadi pondasi pembangunan aplikasi. Data dalam pemrograman secara umum dapat dibagi menjadi dua kategori utama: tipe data primitif dan tipe data non-primitif. Pemahaman yang baik tentang kedua kategori ini sangat penting untuk menjadi programmer Python yang efektif.

**Tipe data primitif** adalah tipe data dasar yang hanya dapat menyimpan satu nilai pada satu waktu. Mereka seperti atom dalam dunia pemrograman - unit terkecil yang tidak dapat dibagi lagi. Contoh tipe data primitif meliputi:

- **Integer**: merepresentasikan bilangan bulat (contoh: 5, -10, 1000)
- **Float**: merepresentasikan bilangan pecahan (contoh: 3.14, -0.5, 2.0)
- **Boolean**: merepresentasikan nilai kebenaran (True atau False)
- **Character**: merepresentasikan satu karakter (seperti 'a', 'B', '?')

Di sisi lain, **tipe data non-primitif** adalah struktur yang lebih kompleks yang dapat menyimpan multiple nilai atau kumpulan data. Mereka seperti molekul yang terdiri dari berbagai atom. Tipe data non-primitif mencakup string, collection, array, dan objek.

Python memiliki pendekatan yang unik dalam hal tipe data. Berbeda dengan bahasa pemrograman lain, Python tidak memiliki tipe data char secara terpisah. Sebagai gantinya, Python menggunakan string (yang merupakan kumpulan karakter) bahkan untuk karakter tunggal. Python juga tidak memiliki tipe data array tradisional seperti bahasa C atau Java, tetapi menyediakan struktur data yang lebih fleksibel seperti list, tuple, dictionary, dan set.

Pada bab ini, kita akan menjelajahi struktur data non-primitif utama dalam Python: list, tuple, dan dictionary. Kita akan mempelajari karakteristik, operasi, dan penggunaan praktis masing-masing struktur data.

## List

List adalah salah satu struktur data paling serbaguna dan banyak digunakan dalam Python. Bayangkan sebuah list seperti lemari dengan banyak laci. Setiap laci dapat menyimpan item yang berbeda, dan setiap laci memiliki nomor identifikasi (indeks) yang memungkinkan kita mengakses item di dalamnya.

### Deklarasi dan Akses List

Membuat list dalam Python sangat sederhana. Kita cukup menempatkan elemen-elemen yang ingin disimpan di antara kurung siku [], dipisahkan dengan koma:

```python
lemari = ['a', 2, 2.2, 2==2, 'akhir']
```

Salah satu keunikan list Python adalah kemampuannya menyimpan berbagai tipe data dalam satu list. Dalam contoh di atas, kita memiliki string ('a'), integer (2), float (2.2), boolean (2==2 yang menghasilkan True), dan string lagi ('akhir').

Untuk mengakses elemen dalam list, kita menggunakan notasi indeks:

```python
print(lemari[0])  # Output: 'a'
print(lemari[3])  # Output: True
print(lemari[-1]) # Output: 'akhir' (mengakses dari akhir list)
```

Indeks list selalu dimulai dari 0, bukan 1. Ini adalah konvensi yang konsisten di hampir semua bahasa pemrograman. Indeks negatif memungkinkan kita mengakses elemen dari akhir list (-1 untuk elemen terakhir, -2 untuk kedua terakhir, dan seterusnya).

### Memodifikasi List

Salah satu karakteristik utama list adalah bersifat mutable, yang berarti kita dapat mengubah elemen-elemennya setelah list dibuat:

```python
lemari = ['a', 2, 2.2, True, 'akhir']
print(lemari)  # Output: ['a', 2, 2.2, True, 'akhir']

lemari[4] = 4000  # Mengganti elemen ke-4
print(lemari)  # Output: ['a', 2, 2.2, True, 4000]

lemari.append('tambahan1')  # Menambah elemen di akhir
print(lemari)  # Output: ['a', 2, 2.2, True, 4000, 'tambahan1']

lemari.insert(3, 'tambahan2')  # Menyisipkan elemen di indeks ke-3
print(lemari)  # Output: ['a', 2, 2.2, 'tambahan2', True, 4000, 'tambahan1']

lemari.remove(2)  # Menghapus elemen dengan nilai 2
print(lemari)  # Output: ['a', 2.2, 'tambahan2', True, 4000, 'tambahan1']

lemari.pop()  # Menghapus elemen terakhir
print(lemari)  # Output: ['a', 2.2, 'tambahan2', True, 4000]

lemari.clear()  # Menghapus semua elemen
print(lemari)  # Output: []
```

### Operasi pada List

List mendukung berbagai operasi seperti penggandaan dan penggabungan:

```python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst3 = lst1.copy()  # Membuat salinan lst1
print(lst3)  # Output: [1, 2, 3]

lst3.extend(lst2)  # Menggabungkan lst2 ke lst3
print(lst3)  # Output: [1, 2, 3, 4, 5, 6]
```

### Contoh Penggunaan List dalam Program

List sangat berguna dalam berbagai skenario pemrograman. Berikut adalah contoh praktis penggunaan list:

```python
# Contoh 1: Menggunakan list untuk menyimpan hari dalam seminggu
hari = ['senin', 'selasa', 'rabu', 'kamis', 'jum\'at', 'sabtu', 'ahad']
idx_hari = int(input("Masukkan Index Hari (1-7): "))
if 1 <= idx_hari <= 7:
    print('Hari ini adalah hari {}!'.format(hari[idx_hari-1]))

# Contoh 2: Program pemesanan makanan
pesanan = []
control = 'y'
print('Program Pesan Online Warung bang Mail')
nama = input('Masukkan Identitas: ')
while control == 'y':
    item = input('Masukkan Makanan/Minuman yang Dipesan! ')
    pesanan.append(item)
    control = input('Apakah anda ingin memesan makanan/minuman lagi? (y/n) ')

print('>>>Pelanggan bernama {} memesan:'.format(nama))
for i in pesanan:
    print('->> ', i)
```

### List Multi-Dimensi

List dapat berisi list lainnya, menciptakan struktur data multi-dimensi seperti matriks:

```python
# Membuat matriks 3x3 (seperti papan sudoku)
sudoku = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(sudoku[0][0])  # Output: 1 (baris 0, kolom 0)
print(sudoku[1][2])  # Output: 6 (baris 1, kolom 2)

# Iterasi melalui list multi-dimensi
for baris in sudoku:
    for nilai in baris:
        print(nilai, end=" ")
    print()  # Pindah baris setelah mencetak satu baris
```

## Tuple

Tuple sangat mirip dengan list dalam hal penyimpanan data terurut, tetapi dengan satu perbedaan penting: tuple bersifat immutable (tidak dapat diubah). Setelah tuple dibuat, kita tidak dapat menambah, menghapus, atau mengubah elemennya.

### Deklarasi dan Akses Tuple

Tuple dibuat dengan mengapit elemen-elemennya dengan tanda kurung ():

```python
tup = (1, 2, 3, 'a', 'b', 'c', True, 3.14)
```

Akses elemen tuple mirip dengan list:

```python
print(tup[0])  # Output: 1
print(tup[3])  # Output: 'a'
print(tup[-1]) # Output: 3.14
```

### Keuntungan Menggunakan Tuple

Mengapa menggunakan tuple jika lebih terbatas daripada list? Tuple memiliki beberapa keunggulan:

1. **Lebih cepat**: Operasi pada tuple umumnya lebih cepat daripada list
2. **Lebih aman**: Data tidak dapat diubah secara tidak sengaja
3. **Digunakan sebagai kunci dictionary**: Karena immutable, tuple dapat digunakan sebagai kunci dictionary
4. **Menggunakan memori lebih efisien**: Tuple mengonsumsi lebih sedikit memori daripada list

Mari bandingkan performa dan penggunaan memori antara list dan tuple:

```python
import sys
import timeit

lst = [1, 2, 3, 'a', 'b', 'c', True, 3.14]
tup = (1, 2, 3, 'a', 'b', 'c', True, 3.14)

print("Ukuran dalam memory dari List:", sys.getsizeof(lst), 'byte')
print("Ukuran dalam memory dari Tuple:", sys.getsizeof(tup), 'byte')

# Mengukur waktu pembuatan list vs tuple
lst_tst = timeit.timeit(stmt="a = [1,2,3,4,5,True,3.14]", number=1000000)
tup_tst = timeit.timeit(stmt="b = (1,2,3,4,5,True,3.14)", number=1000000)

print("Waktu pembuatan List: ", lst_tst)
print("Waktu pembuatan Tuple: ", tup_tst)
```

Pada kebanyakan kasus, perbedaan performa ini tidak signifikan untuk aplikasi kecil, tetapi dapat menjadi penting pada aplikasi yang menangani data dalam skala besar.

### Kapan Menggunakan Tuple

Gunakan tuple ketika:

- Data tidak perlu diubah setelah dibuat
- Anda ingin memastikan integritas data (data tidak dapat diubah)
- Anda perlu menggunakan koleksi sebagai kunci dalam dictionary
- Anda bekerja dengan data dalam volume besar dan perlu optimasi performa

## Dictionary

Dictionary adalah struktur data yang sangat powerful dalam Python yang menyimpan data sebagai pasangan key-value. Berbeda dengan list dan tuple yang menggunakan indeks numerik, dictionary menggunakan kunci (key) unik untuk mengakses nilai (value).

### Deklarasi dan Akses Dictionary

Dictionary dibuat dengan mengapit pasangan key-value dengan kurung kurawal {}, dengan key dan value dipisahkan oleh titik dua:

```python
dct = {'assasin': 'dave', 'tank': 'nino'}
print(dct)  # Output: {'assasin': 'dave', 'tank': 'nino'}
```

Kita dapat mengakses, menambah, dan memodifikasi nilai menggunakan key:

```python
# Mengakses nilai
print(dct['assasin'])  # Output: 'dave'

# Memodifikasi nilai
dct['tank'] = 'naufal'
print(dct)  # Output: {'assasin': 'dave', 'tank': 'naufal'}

# Menambah pasangan key-value baru
dct['mage'] = 'lemon'
dct['toplaner'] = 'alief'
print(dct)  # Output: {'assasin': 'dave', 'tank': 'naufal', 'mage': 'lemon', 'toplaner': 'alief'}

# Menghapus pasangan key-value
dct.pop('tank')
print(dct)  # Output: {'assasin': 'dave', 'mage': 'lemon', 'toplaner': 'alief'}
```

### Metode Alternatif untuk Mengakses Dictionary

Python menyediakan metode .get() untuk mengakses nilai dengan lebih aman:

```python
dct = {'ketua': 'Prima', 'bendahara': 'Ziyad'}

# Menggunakan .get() untuk menghindari error jika key tidak ditemukan
print(dct.get('sekertaris'))  # Output: None (tidak error)
print(dct.get('sekertaris', 'Sekertaris belum diputuskan'))  # Output: 'Sekertaris belum diputuskan'
print(dct.get('bendahara', 'Bendahara belum diputuskan'))  # Output: 'Ziyad'

# Menghapus dengan del
del dct['bendahara']
print(dct.get('bendahara', 'Bendahara belum diputuskan'))  # Output: 'Bendahara belum diputuskan'
```

Metode .get() sangat berguna karena tidak akan menyebabkan error meskipun key yang diminta tidak ada dalam dictionary.

### Contoh Penggunaan Dictionary

Dictionary sangat cocok untuk merepresentasikan objek dunia nyata yang memiliki atribut-atribut tertentu. Berikut contoh penggunaannya dalam program pemesanan:

```python
# Program Pesan Online Warung Bang Mail dengan dictionary
pesanan = []
nama = input('Masukkan Identitas: ')

while True:
    item = {
        'nama': input('Masukkan Makanan/Minuman yang Dipesan: '),
        'jumlah': int(input('Masukkan Jumlah: ')),
        'harga': int(input('Masukkan Harga per Item: '))
    }
    pesanan.append(item)
    control = input('Apakah Anda ingin memesan lagi? (y/n): ')
    if control != 'y':
        break

print(f'\n>>> Pelanggan bernama {nama} memesan:')
total_harga = 0
for item in pesanan:
    subtotal = item['harga'] * item['jumlah']
    total_harga += subtotal
    print(f'->> {item["nama"]}')
    print(f'   - jml: {item["jumlah"]}')
    print(f'   - harga: {item["harga"]}')

print(f'\nTotal Harga: {total_harga}')
```

Dalam contoh ini, setiap item pesanan adalah sebuah dictionary yang memiliki tiga key: 'nama', 'jumlah', dan 'harga'. Pendekatan ini lebih terstruktur dan mudah dikelola dibandingkan menggunakan list sederhana.

## Kesimpulan

Dalam bab ini, kita telah mempelajari tiga struktur data fundamental dalam Python: list, tuple, dan dictionary. Masing-masing memiliki karakteristik dan penggunaan yang berbeda:

1. **List**: Koleksi terurut yang dapat diubah (mutable). Ideal untuk menyimpan kumpulan data yang mungkin perlu dimodifikasi.
2. **Tuple**: Koleksi terurut yang tidak dapat diubah (immutable). Cocok untuk data yang tetap dan tidak berubah, serta lebih efisien dalam penggunaan memori dan performa.
3. **Dictionary**: Koleksi asosiatif yang tidak terurut, menyimpan data sebagai pasangan key-value. Sangat powerful untuk merepresentasikan objek dengan atribut.

Pemahaman yang baik tentang kapan dan bagaimana menggunakan masing-masing struktur data ini sangat penting untuk menulis kode Python yang efisien, mudah dibaca, dan mudah dipelihara. Dalam prakteknya, seringkali kita menggunakan kombinasi dari ketiganya untuk memecahkan masalah pemrograman yang kompleks.
