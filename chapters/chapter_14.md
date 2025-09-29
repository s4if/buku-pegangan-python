# Penanganan Kesalahan (Error Handling)

Penanganan kesalahan (Error handling) adalah proses menangani dan mengelola kesalahan yang mungkin terjadi saat menjalankan program. Ketika sebuah program dijalankan, beberapa situasi tak terduga dapat muncul, seperti sintaks error, pembagian dengan nol, masalah kegagalan jaringan atau mengakses file yang tidak eksis. Untuk menjaga agar program tetap berjalan tanpa crash dan mencegah kegagalan yang tidak diharapkan, penting untuk memahami konsep error handling.

Dalam Python, Penanganan kesalahan dapat dilakukan dengan menggunakan blok try-except. Kita menempatkan kode yang memiliki potensi kesalahan di dalam blok try. Jika kesalahan terjadi, program akan pindah ke bagian blok except, di mana dapat ditentukan tindakan yang diambil atau pesan yang ditampilkan kepada pengguna. Melalui mekanisme ini, kita dapat menangani dan memberikan tanggapan yang sesuai terhadap kesalahan yang terjadi serta memungkinkan program untuk tetap melanjutkan eksekusinya.

## Contoh Error (Operasi Pembagian)

Operasi matematika melibatkan operand dengan tipe numerik, sehingga operasi yang melibatkan data non-numerik berpotensi menyebabkan kegagalan pada program. Selain itu, pada operasi matematika seperti pembagian juga memiliki beberapa kondisi dimana dapat menyebabkan kegagalan program misalkan pembagian dengan nol.

Sebagai bagian dari ilustrasi, akan dibuat fungsi dengan dua parameter a dan b. Fungsi akan melakukan operasi sederhana yaitu pembagian a dan b dan menampilkan hasilnya pada layar.

Terdapat 3 skenario pemanggilan fungsi yang akan bisa terjadi yaitu:

1. memasukkan parameter a dan b berupa angka numerik dengan b bukan 0
2. memasukkan parameter a dan b berupa angka numerik dan b = 0
3. memasukkan parameter a dengan tipe str dan b numerik

Dari 3 skenario tersebut, skenario 2 akan menyebabkan terjadinya ZeroDivisionError dan skenario 3, dimana mungkin tidak sengaja pengguna salah mengetikkan nilai karakter non numerik yang menyebabkan terjadinya TypeError.

### Kode

```python
# Fungsi Mencetak Hasil Pembagian
# parameter a : numerator
# parameter b : denominator
def cetak_pembagian(a, b):
    output = a/b
    print(f"Hasil {a} / {b} adalah {output}\n")
```

### Skenario 1

**Kode:**

```text
cetak_pembagian(100, 2)
```

**Output:**

```text
Hasil 100 / 2 adalah 50.0
```

### Skenario 2

**Kode:**

```python
cetak_pembagian(100, 0)
```

**Output:**

```text
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Cell In[22], line 3
      1 # SKENARIO 2
----> 3 cetak_pembagian(100, 0)
Cell In[20], line 2, in cetak_pembagian(a, b)
      1 def cetak_pembagian(a, b):
----> 2     print(f"{a} / {b} adalah {a/b}")
ZeroDivisionError: division by zero
```

### Skenario 3

**Kode:**

```python
cetak_pembagian(100, "a")
```

**Output:**

```text
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[24], line 3
      1 # SKENARIO 3
----> 3 cetak_pembagian(100, "a")
Cell In[20], line 2, in cetak_pembagian(a, b)
      1 def cetak_pembagian(a, b):
----> 2     print(f"{a} / {b} adalah {a/b}")
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

## Blok try … except

Dalam Python, kita dapat menggunakan blok try-except untuk penanganan kesalahan yang mungkin terjadi saat program berjalan. Sesuai namanya, blok ini terdiri dari setidaknya 2 bagian yaitu try dan except. Berikut adalah penjelasan beberapa blok pada try-except:

- **try**: di dalam blok ini, kita menempatkan kode-kode yang berpotensi menyebabkan kesalahan
- **except**: blok ini digunakan untuk menangkap kesalahan yang terjadi di dalam blok try. Setiap try-except dapat memiliki beberapa blok except yang berbeda untuk menangkap jenis kesalahan yang berbeda. Misalnya, untuk menangani ValueError dan TypeError, maka dapat membuat blok except ValueError dan except TypeError.
- **else**: merupakan blok opsional yang dapat ditambahkan dan hanya akan dieksekusi jika tidak ada kesalahan yang terjadi dalam blok try.
- **finally**: merupakan blok opsional dan akan selalu dieksekusi, baik terjadi kesalahan maupun tidak.

Penting untuk memastikan, di dalam blok except hanya memasukkan kode-kode yang dapat berjalan dengan aman. Jangan sampai terjadi blok except dapat menciptakan kemungkinan error lainnya. Untuk itu, blok except biasanya hanya digunakan untuk menangkap error yang terjadi dan memberi alternatif solusi yang aman bukan melakukan operasi apapun.

**Kode:**

```python
try:
    # blok kode yang berpotensi terjadi kesalahan
    # ...
except ExceptionType:
    # penanganan kesalahan dari jenis tertentu
    # ...
except AnotherExceptionType:
    # penanganan kesalahan dari jenis lain
    # ...
else:
    # Blok ini dieksekusi jika tidak ada kesalahan
    # ...
finally:
    # Blok ini akan selalu dieksekusi ada atau tidak kesalahan
    # ...
```

## Solusi Fungsi Pembagian

Fungsi pembagian yang dibuat sebelumnya, dapat diperbaiki dengan menambahkan blok try-except. Pada solusi ini, fungsi akan menangani dua jenis error yaitu ZeroDivisionError dan TypeError. Untuk mengantisipasi error lainnya, kita akan menambah 1 blok except yang dapat menangkap kegagalan secara general. Diharapkan, saat kode berjalan, meskipun terdapat kesalahan yang menyebabkan error, fungsi dapat tetap menampilkan informasi yang relevan tanpa membuat program menjadi error.

Berikut implementasinya:

**Kode:**

```python
def cetak_pembagian(a, b):
    try:
        output = a / b
        print(f"Hasil {a} / {b} adalah {output}")
    except ZeroDivisionError:
        print("Error : nilai b tidak boleh 0")
    except TypeError:
        print("Error : a dan b harus numerik")
    except Exception:
        print("Error tidak diketahui")
    
# menjalankan fungsi untuk SKENARIO 1-3
cetak_pembagian(100, 2)
cetak_pembagian(100, 0)
cetak_pembagian(100, "a")
```

**Output:**

```text
Hasil 100 / 2 adalah 50.0
Error : nilai b tidak boleh 0
Error : a dan b harus numerik
```

Setiap penanganan kesalahan menggunakan try except, sangat dianjurkan untuk menangkap exception sedetail mungkin. Hal ini penting agar penyebab kesalahan dapat diketahui dengan lebih jelas. Jika semua kemungkinan error ditangkap dalam satu tempat, maka akan lebih sulit mengetahui penyebab kesalahan sebenarnya.

Sebagai contoh, jika kita tulis ulang fungsi pembagian hanya dengan satu exception seperti di bawah ini, maka akan sangat sulit mengetahui secara persis apa yang menyebabkan kegagalan program.

**Kode:**

```python
def cetak_pembagian(a, b):
    try:
        output = a / b
        print(f"Hasil {a} / {b} adalah {output}")
    except Exception:
        print("Error : Terjadi Kesalahan")
# menjalankan fungsi untuk SKENARIO 1-3
cetak_pembagian(100, 2)
cetak_pembagian(100, 0)
cetak_pembagian(100, "a")
```

**Output:**

```text
Hasil 100 / 2 adalah 50.0
Error : Terjadi Kesalahan
Error : Terjadi Kesalahan
```

## Menggabungkan Beberapa Exception

Meskipun praktik yang disarankan adalah menggunakan exception yang detail, namun terdapat kondisi yang mungkin memiliki penanganan mirip antara beberapa exception. Sebagai contoh saja, kita dapat menggabungkan exception pembagian dengan nol dan nilai non-numerik secara bersamaan dengan memberikan informasi yang relevan pada blok except.

**Kode:**

```python
def cetak_pembagian(a, b):
    try:
        output = a / b
        print(f"Hasil {a} / {b} adalah {output}")
    except (ZeroDivisionError, TypeError):
        print("Error : a harus numerik, b harus numerik dan tidak 0")
    except Exception:
        print("Error tidak diketahui")
# menjalankan fungsi untuk SKENARIO 1-3
cetak_pembagian(100, 2)
cetak_pembagian(100, 0)
cetak_pembagian(100, "a")
```

**Output:**

```text
Hasil 100 / 2 adalah 50.0
Error : a harus numerik, b harus numerik dan tidak 0
Error : a harus numerik, b harus numerik dan tidak 0
```

## Mengakses Atribut Exception

Saat menangani exception, kita dapat mengakses objek exception tersebut dan menggunakan informasi yang tersedia. Hal ini mungkin dapat memperjelas sumber permasalahan yang ada. Salah satu informasi yang dapat diperoleh adalah pesan error dari exception. Pesan ini dapat diakses melalui atribut `args[0]`.

Berikut adalah contoh penerapannya pada fungsi pembagian:

**Kode:**

```python
def cetak_pembagian(a, b):
    try:
        output = a / b
        print(f"Hasil {a} / {b} adalah {output}")
    except ZeroDivisionError as ex:
        print("Error : nilai b tidak boleh 0")
        print(ex.args[0])
    except TypeError as ex:
        print("Error : a dan b harus numerik")
        print(ex.args[0])
    except Exception as ex:
        print("Error tidak diketahui")
        print(ex.args[0])
    
# menjalankan fungsi untuk SKENARIO 1-3
cetak_pembagian(100, 2)
print()
cetak_pembagian(100, 0)
print()
cetak_pembagian(100, "a")
```

**Output:**

```text
Hasil 100 / 2 adalah 50.0

Error : nilai b tidak boleh 0
division by zero

Error : a dan b harus numerik
unsupported operand type(s) for /: 'int' and 'str'
```

## Blok else dan finally

Jika diperlukan, terdapat dua blok tambahan yang dapat digunakan untuk melengkapi blok try except yaitu else dan finally. Blok else hanya akan dieksekusi jika blok try berjalan tanpa kesalahan, sementara blok finally akan selalu dieksekusi saat ada kesalahan maupun tidak.

Berikut contoh penggunaan blok else dan finally berdasarkan contoh sebelumnya:

**Kode:**

```python
def cetak_pembagian(a, b):
    try:
        output = a / b
        print(f"Hasil {a} / {b} adalah {output}")
    except ZeroDivisionError as ex:
        print("Error : nilai b tidak boleh 0")
        print(ex.args[0])
    except TypeError as ex:
        print("Error : a dan b harus numerik")
        print(ex.args[0])
    except Exception as ex:
        print("Error tidak diketahui")
        print(ex.args[0])
    else:
        print("Blok Try berhasil dijalankan tanpa error")
    finally:
        print("Apapun yang terjadi blok ini akan dieksekusi")
# menjalankan fungsi untuk SKENARIO 1-3
cetak_pembagian(100, 2)
print()
cetak_pembagian(100, 0)
print()
cetak_pembagian(100, "a")
```

**Output:**

```text
Hasil 100 / 2 adalah 50.0
Blok Try berhasil dijalankan tanpa error
Apapun yang terjadi blok ini akan dieksekusi

Error : nilai b tidak boleh 0
division by zero
Apapun yang terjadi blok ini akan dieksekusi

Error : a dan b harus numerik
unsupported operand type(s) for /: 'int' and 'str'
Apapun yang terjadi blok ini akan dieksekusi
```

## Ringkasan

Dalam Python, blok try-except digunakan untuk penanganan kesalahan (error handling) yang mungkin terjadi saat menjalankan suatu kode program. Kode-kode yang berpotensi menimbulkan error ditempatkan dalam blok try, dan jika error terjadi, kontrol program akan beralih ke blok except yang sesuai. Di dalam blok except, penanganan exception dapat dilakukan melalui tindakan yang relevan, seperti menampilkan pesan kesalahan atau mengambil tindakan perbaikan. Objek exception yang dihasilkan juga menyediakan informasi tambahan tentang pengecualian tersebut, seperti pesan dan jenis exception. Blok try-except juga dapat dilengkapi dengan blok else dan finally jika diperlukan.

Dengan menggunakan blok try-except, aliran program dapat dijaga agar tetap berjalan dengan baik serta mengatasi error yang mungkin terjadi secara terkendali.

sumber: [https://sainsdata.id/pemrograman/python/5457/python-penanganan-kesalahan-error-handling/](https://sainsdata.id/pemrograman/python/5457/python-penanganan-kesalahan-error-handling/)
