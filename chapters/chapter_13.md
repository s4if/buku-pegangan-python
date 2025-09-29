# Pemrograman Berbasis Objek di Python

## Pendahuluan

Dalam pengembangan perangkat lunak, terdapat berbagai paradigma pemrograman yang membantu developer dalam menyusun kode secara efektif. Salah satu paradigma yang paling populer dan powerful adalah **Pemrograman Berbasis Objek** (Object-Oriented Programming/OOP). Python sebagai bahasa pemrograman modern mendukung penuh paradigma ini, memungkinkan developer untuk membuat kode yang terstruktur, mudah dikelola, dan dapat digunakan kembali.

Sebelum membahas OOP, mari kita review pendekatan tradisional yang biasa digunakan yaitu **pemrograman prosedural/fungsional**. Dalam paradigma ini, program dibangun dari fungsi-fungsi yang mengolah data. Konsep DRY (Don't Repeat Yourself) diterapkan dengan membuat fungsi untuk menghindari duplikasi kode.

Contoh program sederhana pertarungan monster dengan pendekatan prosedural:

```python
from random import randint
from time import sleep

monster1 = { 'nama':'orc', 'hp':300, 'dmg':35}
monster2 = { 'nama':'skeleton', 'hp':250, 'dmg':40}

def serang(monster, musuh):
    real_dmg = randint(-15,15) + monster['dmg']
    musuh['hp'] -= real_dmg
    print(f"\n{monster['nama']} menyerang {musuh['nama']} dengan damage {real_dmg}\n")
    sleep(1)

print("Game {} vs {} dimulai!".format(monster1['nama'], monster2['nama']))

while True:
    serang(monster1, monster2)
    serang(monster2, monster1)
    
    print(">> {} HP :  {}".format(monster1['nama'], monster1['hp']))
    print(">> {} HP :  {}".format(monster2['nama'], monster2['hp']))
    sleep(1)
    
    if monster1['hp'] <= 0 or monster2['hp'] <= 0: 
        if monster1['hp'] < monster2['hp']:
            print("{} Menang!".format(monster2['nama']))
            break
        elif monster2['hp'] < monster1['hp']:
            print("{} Menang!".format(monster1['nama']))
            break
        else:
            print("Imbang")
            break
```

Program di atas sudah menerapkan konsep DRY dengan baik, namun memiliki kelemahan fundamental: **data dan fungsi terpisah**. Dictionary monster hanya menyimpan data, sedangkan fungsi serang berdiri sendiri. Pada program kecil, pendekatan ini masih dapat dikelola, tetapi ketika program semakin kompleks, pengelolaan data dan fungsi menjadi semakin sulit.

## Konsep Dasar OOP

Object-Oriented Programming (OOP) adalah paradigma pemrograman yang memandang program sebagai kumpulan objek yang berinteraksi. Setiap objek memiliki karakteristik (property) dan perilaku (method). Pendekatan ini lebih alami karena merepresentasikan dunia nyata di mana segala sesuatu adalah objek dengan sifat dan kemampuan tertentu.

### Kelas dan Objek

**Kelas** adalah blueprint atau cetakan untuk membuat objek. **Objek** adalah instance (perwujudan) dari kelas. Analoginya, kelas adalah resep kue, sedangkan objek adalah kue yang dibuat dari resep tersebut.

Mari kita lihat contoh implementasi OOP untuk program pertarungan monster:

```python
from random import randint
from time import sleep

class Monster():
    def __init__(self, nama, hp, dmg):
        self.nama = nama  # properti nama
        self.hp = hp      # properti health points
        self.dmg = dmg    # properti damage
    
    def serang(self, musuh):
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        print("{} menyerang {} dengan damage {}"
              .format(self.nama, musuh.nama, actual_dmg))

# Membuat objek dari kelas Monster
monster1 = Monster("Orc", 200, 30)
monster2 = Monster("Skeleton", 180, 35)

# Memulai pertarungan
while True:
    monster1.serang(monster2)
    sleep(0.5)
    monster2.serang(monster1)
    sleep(0.5)
    
    print(">> {} HP :  {}".format(monster1.nama, monster1.hp))
    print(">> {} HP :  {}".format(monster2.nama, monster2.hp))
    sleep(0.5)
    
    if monster1.hp <= 0 or monster2.hp <= 0:
        if monster1.hp == monster2.hp: 
            print("Imbang")
        elif monster1.hp > monster2.hp: 
            print("{} Menang!".format(monster1.nama))
        else: 
            print("{} Menang!".format(monster2.nama))
        break
```

### Method Khusus \_\_init\_\_

Method `__init__` adalah method khusus yang otomatis dipanggil ketika objek dibuat dari kelas. Method ini digunakan untuk menginisialisasi properti objek. Parameter `self` merujuk pada objek itu sendiri, mirip dengan kata kunci `this` di bahasa pemrograman lain.

### Properti dan Method

**Properti** adalah variabel yang dimiliki objek, menyimpan data atau state objek tersebut. **Method** adalah fungsi yang dimiliki objek, mendefinisikan perilaku atau aksi yang dapat dilakukan objek.

Dalam contoh di atas, `nama`, `hp`, dan `dmg` adalah properti, sedangkan `serang` adalah method. Perhatikan bagaimana data dan fungsi yang terkait sekarang disatukan dalam satu entitas (objek), membuat kode lebih terorganisir dan mudah dipahami.

## Karakteristik OOP

OOP memiliki tiga karakteristik utama yang membuatnya powerful: Inheritance (Pewarisan), Polymorphism (Polimorfisme), dan Abstraction (Abstraksi).

### Inheritance (Pewarisan)

Inheritance memungkinkan kita membuat kelas baru yang mewarisi properti dan method dari kelas yang sudah ada. Kelas yang diwarisi disebut kelas induk (parent class), sedangkan kelas yang mewarisi disebut kelas anak (child class).

Mari kita lihat contoh implementasi inheritance:

```python
from random import randint
from time import sleep

class Monster():
    def __init__(self, nama, hp, dmg):
        self.nama = nama
        self.hp = hp
        self.dmg = dmg
    
    def serang(self, musuh):
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        print("{} menyerang {} dengan damage {}"
              .format(self.nama, musuh.nama, actual_dmg))

class Wisp(Monster):  # Wisp mewarisi dari Monster
    def fireball(self, musuh):
        musuh.hp = musuh.hp - 40
        print("{} melemparkan bola api ke {} dengan damage 40"
              .format(self.nama, musuh.nama))

# Membuat objek
monster1 = Monster("Orc", 200, 30)
monster2 = Wisp("Will o Wisp", 180, 15)  # Wisp memiliki semua properti dan method Monster

while True:
    monster1.serang(monster2)
    sleep(0.5)
    monster2.serang(monster1)  # Method warisan dari Monster
    monster2.fireball(monster1)  # Method khusus Wisp
    sleep(0.5)
    
    print(">> {} HP :  {}".format(monster1.nama, monster1.hp))
    print(">> {} HP :  {}".format(monster2.nama, monster2.hp))
    sleep(0.5)
    
    if monster1.hp <= 0 or monster2.hp <= 0:
        if monster1.hp == monster2.hp: 
            print("Imbang")
        elif monster1.hp > monster2.hp: 
            print("{} Menang!".format(monster1.nama))
        else: 
            print("{} Menang!".format(monster2.nama))
        break
```

Dalam contoh di atas, kelas `Wisp` mewarisi semua properti dan method dari kelas `Monster`, tetapi juga memiliki method tambahan `fireball`. Ini adalah contoh bagaimana inheritance mempromosikan reuseability tanpa harus menulis ulang kode.

### Polymorphism (Polimorfisme)

Polymorphism memungkinkan objek dari kelas yang berbeda merespon method dengan nama yang sama secara berbeda. Dalam Python, polymorphism dicapai dengan mendefinisikan ulang method di kelas anak.

Contoh polymorphism:

```python
from random import randint
from time import sleep

class Monster():
    def __init__(self, nama, hp, dmg):
        self.nama = nama
        self.hp = hp
        self.dmg = dmg
    
    def serang(self, musuh):
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        print("{} menyerang {} dengan damage {}"
              .format(self.nama, musuh.nama, actual_dmg))

class Ghoul(Monster):
    def serang(self, musuh):  # Mendefinisikan ulang method serang
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        self.hp = self.hp + actual_dmg // 4  # Lifesteal: menyembuh 25% damage
        print("{} menyerang {} dengan damage {}, dan lifesteal {} poin"
              .format(self.nama, musuh.nama, actual_dmg, (actual_dmg // 4)))

monster1 = Monster("Orc", 200, 30)
monster2 = Ghoul("Ghoul", 180, 35)

while True:
    monster1.serang(monster2)  # Memanggil method serang dari Monster
    sleep(0.5)
    monster2.serang(monster1)  # Memanggil method serang dari Ghoul (polymorphism)
    sleep(0.5)
    
    print(">> {} HP :  {}".format(monster1.nama, monster1.hp))
    print(">> {} HP :  {}".format(monster2.nama, monster2.hp))
    sleep(0.5)
    
    if monster1.hp <= 0 or monster2.hp <= 0:
        if monster1.hp == monster2.hp: 
            print("Imbang")
        elif monster1.hp > monster2.hp: 
            print("{} Menang!".format(monster1.nama))
        else: 
            print("{} Menang!".format(monster2.nama))
        break
```

Pada contoh di atas, baik `Monster` maupun `Ghoul` memiliki method `serang`, tetapi implementasinya berbeda. Ghoul memiliki kemampuan lifesteal yang tidak dimiliki Monster biasa. Inilah yang disebut polymorphism: method dengan nama sama tetapi perilaku berbeda.

### Abstraction (Abstraksi)

Abstraction adalah konsep menyembunyikan detail implementasi dan hanya menampilkan fungsionalitas esensial. Dalam Python, abstraction dapat dicapai menggunakan abstract base classes (ABC) dari modul `abc`.

Contoh abstraction:

```python
from random import randint
from time import sleep
from abc import ABC, abstractmethod

class Monster(ABC):  # Kelas abstrak
    @abstractmethod
    def __init__(self, nama):
        pass

    @abstractmethod
    def serang(self, musuh):  # Method abstrak
        pass

class Orc(Monster):
    def __init__(self, nama):
        self.nama = nama
        self.hp, self.dmg = 200, 30
        
    def serang(self, musuh):
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        print("{} menyerang {} dengan damage {}"
              .format(self.nama, musuh.nama, actual_dmg))

class Ghoul(Monster):
    def __init__(self, nama):
        self.nama = nama
        self.hp, self.dmg = 150, 35

    def serang(self, musuh):
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        self.hp = self.hp + actual_dmg // 4
        print("{} menyerang {} dengan damage {}, dan lifesteal {} poin"
              .format(self.nama, musuh.nama, actual_dmg, (actual_dmg // 4)))

# monster0 = Monster("Monster")  # Error: tidak bisa instansiasi kelas abstrak
monster1 = Orc("Orc")
monster2 = Ghoul("Ghoul")

# Kode lain sama seperti sebelumnya
```

Kelas abstrak `Monster` mendefinisikan struktur dasar yang harus diikuti oleh semua kelas turunannya. Setiap kelas turunan harus mengimplementasikan method `__init__` dan `serang`. Ini memastikan konsistensi antarmuka (nama method dan parameter sama) meskipun implementasi bisa berbeda.

## Pengembangan Program Pertarungan Monster

Mari kita kembangkan program pertarungan monster dengan memanfaatkan semua konsep OOP yang telah dipelajari:

```python
from random import randint
from time import sleep
from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def __init__(self, nama):
        pass

    @abstractmethod
    def serang(self, musuh):
        pass

class Orc(Monster):
    def __init__(self, nama):
        self.nama = nama
        self.hp, self.dmg = 200, 30
        
    def serang(self, musuh):
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        print("{} menyerang {} dengan damage {}"
              .format(self.nama, musuh.nama, actual_dmg))

class Ghoul(Monster):
    def __init__(self, nama):
        self.nama = nama
        self.hp, self.dmg = 150, 35

    def serang(self, musuh):
        actual_dmg = (self.dmg + randint(-15, 15))
        musuh.hp = musuh.hp - actual_dmg
        self.hp = self.hp + actual_dmg // 4
        print("{} menyerang {} dengan damage {}, dan lifesteal {} poin"
              .format(self.nama, musuh.nama, actual_dmg, (actual_dmg // 4)))

def pilih_monster(id):
    print(f'\nSilahkan pilih monster ke-{id}')
    nama = input('Masukkan Nama Monster : ')
    print('Silahkan pilih tipe monster')
    print('1 -> Orc (HP:200, DMG:30)')
    print('2 -> Ghoul (HP:150, DMG:35, Lifesteal:25%)')
    
    tipe = int(input('Silahkan Pilih: '))
    
    if tipe == 1:
        return Orc(nama)
    elif tipe == 2:
        return Ghoul(nama)
    else:
        print("Pilihan tidak valid, menggunakan Orc secara default")
        return Orc(nama)

# Program utama
print("=== GAME PERTARUNGAN MONSTER ===")
monster1 = pilih_monster(1)
monster2 = pilih_monster(2)

print(f"\nPertarungan {monster1.nama} ({monster1.__class__.__name__})", end=" ")
print(f"vs {monster2.nama} ({monster2.__class__.__name__}) dimulai!")

round = 1
while True:
    print(f"\n=== ROUND {round} ===")
    monster1.serang(monster2)
    sleep(1)
    monster2.serang(monster1)
    sleep(1)
    
    print("\nStatus setelah serangan:")
    print(">> {} HP :  {}".format(monster1.nama, max(0, monster1.hp)))
    print(">> {} HP :  {}".format(monster2.nama, max(0, monster2.hp)))
    sleep(1)
    
    if monster1.hp <= 0 or monster2.hp <= 0:
        print("\n=== HASIL AKHIR ===")
        if monster1.hp <= 0 and monster2.hp <= 0:
            print("KEDUA MONSTER KO! Pertarungan imbang!")
        elif monster1.hp <= 0:
            print("{} KO! {} Menang!".format(monster1.nama, monster2.nama))
        else:
            print("{} KO! {} Menang!".format(monster2.nama, monster1.nama))
        break
    
    round += 1
```

**Contoh Output:**

```text
=== GAME PERTARUNGAN MONSTER ===

Silahkan pilih monster ke-1
Masukkan Nama Monster : Orki
Silahkan pilih tipe monster
1 -> Orc (HP:200, DMG:30)
2 -> Ghoul (HP:150, DMG:35, Lifesteal:25%)
Silahkan Pilih: 1

Silahkan pilih monster ke-2
Masukkan Nama Monster : Gogol
Silahkan pilih tipe monster
1 -> Orc (HP:200, DMG:30)
2 -> Ghoul (HP:150, DMG:35, Lifesteal:25%)
Silahkan Pilih: 2

Pertarungan Orki (Orc) vs Gogol (Ghoul) dimulai!

=== ROUND 1 ===
Orki menyerang Gogol dengan damage 43
Gogol menyerang Orki dengan damage 23, dan lifesteal 5 poin

Status setelah serangan:
>> Orki HP :  177
>> Gogol HP :  112

=== ROUND 2 ===
Orki menyerang Gogol dengan damage 18
Gogol menyerang Orki dengan damage 31, dan lifesteal 7 poin

Status setelah serangan:
>> Orki HP :  146
>> Gogol HP :  101

=== ROUND 3 ===
Orki menyerang Gogol dengan damage 33
Gogol menyerang Orki dengan damage 47, dan lifesteal 11 poin

Status setelah serangan:
>> Orki HP :  99
>> Gogol HP :  79

=== ROUND 4 ===
Orki menyerang Gogol dengan damage 20
Gogol menyerang Orki dengan damage 47, dan lifesteal 11 poin

Status setelah serangan:
>> Orki HP :  52
>> Gogol HP :  70

=== ROUND 5 ===
Orki menyerang Gogol dengan damage 44
Gogol menyerang Orki dengan damage 34, dan lifesteal 8 poin

Status setelah serangan:
>> Orki HP :  18
>> Gogol HP :  34

=== ROUND 6 ===
Orki menyerang Gogol dengan damage 41
Gogol menyerang Orki dengan damage 24, dan lifesteal 6 poin

Status setelah serangan:
>> Orki HP :  0
>> Gogol HP :  0

=== HASIL AKHIR ===
KEDUA MONSTER KO! Pertarungan imbang!
```

Program yang telah dikembangkan ini menunjukkan kekuatan OOP:

1. **Abstraction**: Kelas abstrak `Monster` memastikan semua monster memiliki antarmuka yang konsisten
2. **Inheritance**: Semua kelas monster mewarisi dari kelas dasar yang sama
3. **Polymorphism**: Setiap monster memiliki implementasi method `serang` yang berbeda
4. **Encapsulation**: Data dan behavior dikemas dalam objek yang kohesif

## Kelebihan dan Kelemahan OOP

### Kelebihan OOP

1. **Modularity**: Kode terbagi menjadi objek-objek independen yang mudah dipahami dan maintain
2. **Reusability**: Melalui inheritance, kode dapat digunakan kembali tanpa duplikasi
3. **Scalability**: Struktur OOP memudahkan pengembangan program kompleks
4. **Maintainability**: Perubahan pada satu bagian biasanya tidak mempengaruhi bagian lain

### Kelemahan OOP

1. **Learning Curve**: Konsep OOP lebih sulit dipahami pemula
2. **Overhead**: Program OOP cenderung lebih besar dan lebih lambat
3. **Tidak Cocok untuk Semua Masalah**: Beberapa masalah lebih cocok diselesaikan dengan paradigma lain

## 5.6 Kesimpulan

Pemrograman Berbasis Objek adalah paradigma powerful yang membantu developer membuat kode yang terstruktur, modular, dan mudah dikelola. Python mendukung penuh OOP dengan sintaks yang jelas dan intuitif.

Dalam bab ini, kita telah mempelajari:

1. Konsep dasar kelas dan objek
2. Tiga pilar OOP: Inheritance, Polymorphism, dan Abstraction
3. Penerapan OOP dalam pengembangan game sederhana
4. Kelebihan dan kelemahan pendekatan OOP

Dengan memahami OOP, Anda dapat membuat program yang lebih terorganisir dan siap untuk dikembangkan lebih lanjut.

## Latihan

1. Tambahkan kelas monster baru dengan kemampuan khusus dan integrasikan dengan program yang sudah dibuat, misal: **Fenrir** - Memiliki chance 25% untuk menghasilkan serangan critical yang bernilai 2-5 kali nilai dmg

2. Implementasikan skill pada masing-masing monster yang akan dijalankan secara random.

Dengan menyelesaikan latihan ini, Anda akan semakin mahir dalam menerapkan konsep OOP dalam Python.
