# Modul, Library, dan Mekanisme Import di Python

## Pengantar

Saat menulis program Python, kita tidak selalu harus membuat semua kode dari nol. Bayangkan jika kita ingin menghitung akar kuadrat, membuat grafik, atau bahkan mengelola file. Daripada menulis ulang fungsi-fungsi tersebut, kita bisa menggunakan **modul** atau **library** yang sudah tersedia.

Python sangat terkenal karena ekosistem modulnya yang besar dan beragam. Hampir semua kebutuhan programmer, mulai dari matematika hingga kecerdasan buatan, sudah ada library yang siap digunakan.

## Apa itu Modul dan Library?

* **Modul** adalah file Python (berekstensi `.py`) yang berisi kumpulan fungsi, variabel, atau kelas yang bisa digunakan kembali. Modul membantu kita mengorganisir kode agar lebih rapi.
* **Library** adalah kumpulan dari banyak modul yang dikemas bersama untuk tujuan tertentu. Misalnya library `NumPy` berisi banyak modul untuk perhitungan numerik.

> **Analogi sederhana:** Modul seperti sebuah alat tunggal (misalnya obeng), sedangkan library seperti kotak peralatan yang berisi banyak alat (obeng, palu, kunci inggris, dll).

## Tiga Jenis Modul di Python

Python menyediakan modul dalam tiga kategori:

### Modul Built-in

Merupakan modul bawaan yang langsung tersedia saat Python diinstal. Kita bisa langsung memakainya tanpa menginstal apapun.
Contoh:

```python
import math

print(math.sqrt(25))   # menghitung akar kuadrat
print(math.pi)         # menampilkan nilai pi
```

### Modul Buatan Sendiri (User-defined)

Kita bisa membuat modul sendiri. Caranya cukup dengan menyimpan kode Python di file `.py`, lalu mengimpornya di program utama.

Misalnya kita buat file bernama `mymath.py`:

```python
# isi mymath.py
def tambah(a, b):
    return a + b

def kali(a, b):
    return a * b
```

Kemudian di file utama:

```python
import mymath

print(mymath.tambah(2, 3))  # Output: 5
print(mymath.kali(4, 6))    # Output: 24
```

### Library Pihak Ketiga (Third-Party Library)

Library ini dibuat oleh komunitas atau perusahaan, bukan bagian bawaan Python. Untuk memakainya, biasanya kita perlu menginstalnya dulu dengan `pip`.

Contoh penggunaan library `requests` untuk mengambil data dari internet:

```bash
pip install requests
```

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.json())
```

## Mekanisme Import di Python

Agar kita bisa menggunakan modul atau library, kita harus **mengimpor**-nya ke dalam program. Kata kunci yang digunakan adalah `import`.

Contoh sederhana:

```python
import math

print(math.factorial(5))  # Output: 120
```

## Macam-Macam Import di Python

Python menyediakan beberapa cara untuk mengimpor modul, sesuai kebutuhan kita.

### Import Paket/Modul Langsung

```python
import math
print(math.sqrt(16))
```

Kelebihan: jelas sumber fungsi berasal dari mana (`math.sqrt`).
Kekurangan: harus menulis nama modul setiap kali.

### `from modul import ...`

```python
from math import sqrt, pi
print(sqrt(16))
print(pi)
```

Kelebihan: lebih ringkas.
Kekurangan: jika terlalu banyak fungsi dengan nama mirip, bisa membingungkan.

### `import ... as ...` (alias)

```python
import numpy as np
print(np.array([1, 2, 3]))
```

Kelebihan: mempersingkat penulisan, cocok untuk library dengan nama panjang.
Kekurangan: bisa membingungkan pembaca jika alias tidak umum.

### `from ... import ... as ...`

```python
from math import factorial as f
print(f(5))  # Output: 120
```

Kelebihan: sangat ringkas, enak jika hanya memakai 1-2 fungsi.
Kekurangan: bisa membuat kode sulit dibaca jika terlalu banyak dipendekkan.

## Modul dalam Bentuk Folder (Package) dan `__init__.py`

Selain modul tunggal (file `.py`), Python juga mendukung **paket** (package).

* **Paket** adalah folder yang berisi banyak modul, sehingga memudahkan pengorganisasian kode dalam skala besar.
* Agar sebuah folder dikenali sebagai paket Python, di dalamnya biasanya terdapat file khusus bernama `__init__.py`.

**Peran `__init__.py`:**

1. Menandai folder tersebut sebagai paket Python.
2. Bisa dipakai untuk mengatur apa yang otomatis tersedia saat paket diimpor.
3. Bisa dibiarkan kosong, atau berisi kode inisialisasi.

### Contoh Struktur Folder

```text
myproject/
│
├── main.py
└── utils/
    ├── __init__.py
    ├── string_utils.py
    └── math_utils.py
```

Isi `string_utils.py`:

```python
def capitalize_words(text):
    return text.title()
```

Isi `math_utils.py`:

```python
def pangkat(a, b):
    return a ** b
```

Isi `__init__.py`:

```python
from .string_utils import capitalize_words
from .math_utils import pangkat
```

Isi `main.py`:

```python
import utils

print(utils.capitalize_words("halo dunia"))  # Output: Halo Dunia
print(utils.pangkat(2, 5))                   # Output: 32
```

> Dengan adanya `__init__.py`, kita bisa langsung memanggil fungsi dari modul dalam paket tanpa menulis `utils.string_utils.capitalize_words`.

## Kapan Menggunakan Teknik Import Tertentu?

* **`import modul`**

  * Kelebihan: jelas asal fungsi.
  * Kekurangan: penulisan lebih panjang.
  * Waktu Tepat: saat ingin menjaga kejelasan kode.

* **`from modul import ...`**

  * Kelebihan: lebih singkat.
  * Kekurangan: berisiko terjadi konflik nama variabel/fungsi.
  * Waktu Tepat: jika hanya butuh beberapa fungsi dari modul.

* **`import modul as alias`**

  * Kelebihan: penulisan ringkas, umum dipakai.
  * Kekurangan: bisa membingungkan jika alias tidak jelas.
  * Waktu Tepat: untuk library populer dengan alias umum (misalnya `numpy as np`, `pandas as pd`).

* **`from modul import ... as ...`**

  * Kelebihan: sangat ringkas.
  * Kekurangan: bisa menurunkan keterbacaan jika terlalu sering dipakai.
  * Waktu Tepat: jika hanya satu-dua fungsi dipakai terus-menerus.

* **Paket dengan `__init__.py`**

  * Kelebihan: rapi, mudah diatur dalam folder.
  * Kekurangan: perlu manajemen struktur folder yang lebih disiplin.
  * Waktu Tepat: saat mengerjakan proyek besar dengan banyak modul.

## Kesimpulan

* **Modul** adalah file Python yang berisi fungsi/kelas/variabel, sedangkan **library** adalah kumpulan modul.
* Ada tiga jenis modul: **built-in**, **user-defined**, dan **third-party library**.
* Untuk menggunakan modul, kita harus melakukan **import**.
* Python menyediakan beberapa cara import: `import modul`, `from modul import ...`, `import modul as ...`, dan `from modul import ... as ...`.
* **Paket (package)** memungkinkan pengorganisasian modul dalam folder dengan bantuan file `__init__.py`.
* Pemilihan teknik import bergantung pada kebutuhan: ringkas, jelas, atau fleksibel.

Dengan memahami modul, library, mekanisme import, serta paket dengan `__init__.py`, kita bisa menulis program Python yang lebih rapi, terstruktur, dan siap digunakan dalam skala kecil maupun besar.
