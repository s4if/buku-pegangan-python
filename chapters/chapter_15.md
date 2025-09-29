# Bab Terakhir: Mengubah Game PvP ke Paradigma OOP

Di bab-bab sebelumnya, kita sudah berhasil membuat sebuah game sederhana PvP (Player vs Player), yaitu permainan di mana dua pemain saling bertarung secara bergantian. Game ini berjalan di CLI (Command Line Interface), jadi tampilannya hanya berupa teks di terminal tanpa gambar atau grafik. Pada tahap itu, kita membangunnya menggunakan gaya pemrograman fungsional, yaitu dengan mengandalkan kumpulan fungsi yang dipanggil berulang-ulang untuk mengatur jalannya permainan.

Berikut adalah kode program yang sudah kita buat sebelumnya:

```python
from time import sleep

# data player
player1 = {
    'name':'fikri', 'cls':'warrior', 'hp':150,'mp': 100, 'dmg': 15,
    'skills' : {
        'q':{'name':'tebasan kilat', 'dmg':50, 'manacost': 40},
        'w':{'name':'tebasan api', 'dmg':70, 'manacost': 60},
        },
    }

player2 = {
    'name':'ihsan', 'cls':'spearman', 'hp':120,'mp': 120, 'dmg': 17,
    'skills' : {
        'q':{'name':'tusukan maut', 'dmg':50, 'manacost': 40},
        'w':{'name':'lemparan tombak nagabumi', 'dmg':70, 'manacost': 60},
        },
    }

def input_aksi(player):
    skills = player['skills'qq]
    print('Masukkan Aksi: ') 
    for key in skills.keys():
        print(' |> {} -> {}'.format(key, skills[key]['name']))
    aksi = input(' |> a -> attack : ')
    return aksi

def basic_attack(player, musuh):
    print('{} menyerang {} memberikan dmg sebesar {}'.format(
            player['name'], musuh['name'], player['dmg']))
    musuh['hp'] = musuh['hp'] - player['dmg']
    return musuh

def aksi_dijalankan(aksi, player, musuh):
    skills = player['skills']
    if aksi == 'a': 
        musuh = basic_attack(player,musuh)
        
    else :
        if aksi not in skills.keys():
            print('aksi tidak dikenal!')
            
        elif player['mp'] >= skills[aksi]['manacost']:
            print('{} melakukan jurus {}, dmg: {}'.format(
                player['name'], skills[aksi]['name'], skills[aksi]['dmg']))
            player['mp'] = player['mp'] - skills[aksi]['manacost']
            musuh['hp'] = musuh['hp'] - skills[aksi]['dmg']
        else:
            print('mana tidak cukup!')

    player['mp'] += 20 # sejajar dengan if aksi == 'a'
    return player, musuh
    

# main loop
while player1['hp'] > 0 and player2['hp'] > 0:

    # input aksi player1
    print("Giliran Player 1!")
    aksi = input_aksi(player1)
    # aksi dari player1 dijalankan
    player1, player2 = aksi_dijalankan(aksi, player1, player2)
        
    sleep(1) 
    # input aksi player2
    print("Giliran Player 2!")
    aksi = input_aksi(player2)
    # aksi dari player2 dijalankan
    player2, player1 = aksi_dijalankan(aksi, player2, player1)

    # tampilan hp/mp dari player dan monster
    sleep(1) 
    print('\nPlayer1 HP:{}, Player1 MP:{}\n=======\nPlayer2 HP:{}, Player1 MP:{}\n'.format(
        player1['hp'], player1['mp'], player2['hp'], player2['mp']
        ))

if player1['hp'] > player2['hp']: print('Player1 Menang')
elif player1['hp'] < player2['hp']: print('Player2 Menang')
else : print('Imbang')
````

Game ini memang sudah bisa dimainkan dan cukup seru, tapi masih ada beberapa kekurangan yang membuatnya kurang nyaman untuk dikembangkan lebih lanjut. Misalnya, ada banyak kode yang berulang-ulang sehingga terlihat panjang dan agak membingungkan. Selain itu, jika kita ingin menambahkan fitur baru atau mengubah aturan permainan, prosesnya bisa menjadi rumit dan memakan waktu. Hal ini membuat game kita kurang fleksibel untuk dikembangkan lebih jauh.

Untuk mengatasi masalah tersebut, kita akan mencoba pendekatan lain, yaitu menggunakan Object-Oriented Programming (OOP). Dengan OOP, kita bisa menata kode agar lebih rapi, mudah dipahami, dan mudah dikembangkan.

## Prinsip OOP yang Akan Dipakai

Sebelum masuk ke kode, mari kita pahami dulu prinsip **OOP (Object-Oriented Programming)** yang akan kita gunakan untuk memperbaiki game ini. Dengan OOP, kita tidak hanya menulis ulang kode agar lebih rapi, tapi juga memberikan struktur yang jelas sehingga game lebih mudah dikembangkan di masa depan.

1. **Inheritance (Pewarisan)**
   Dalam OOP, kita bisa membuat sebuah **kelas dasar (parent class)** yang berisi atribut dan fungsi umum. Nantinya, kelas ini bisa diturunkan ke **kelas turunan (child class)** seperti *Warrior*, *Mage*, atau *Assassin*. Dengan cara ini, kita tidak perlu menulis ulang kode yang sama berulang-ulang. Cukup sekali di kelas dasar, lalu semua kelas turunan otomatis bisa menggunakannya.

2. **Abstraction & Polymorphism**

   * **Abstraction (Abstraksi)** berarti kita hanya menampilkan hal-hal penting dari sebuah objek dan menyembunyikan detail yang rumit. Contohnya, kita cukup tahu bahwa setiap hero bisa menyerang dan memakai skill, tanpa harus memikirkan detail teknisnya.
   * **Polymorphism (Polimorfisme)** membuat setiap kelas hero bisa dipanggil dengan cara yang sama, meskipun isi detailnya berbeda. Misalnya, saat kita memanggil `serang()`, *Warrior* akan menebas, sedangkan *Mage* mungkin akan menembakkan sihir. Kita cukup memanggil fungsi yang sama tanpa peduli siapa heronya.

### Fitur Tambahan untuk Membuat Game Lebih Seru

Selain memperbaiki struktur kodenya dengan OOP, kita juga menambahkan beberapa fitur baru agar permainannya lebih menarik:

* **Damage random** -> setiap serangan tidak selalu menghasilkan damage yang sama. Ada variasi, sehingga permainan terasa lebih realistis dan menegangkan.
* **Rebalance HP/MP/damage** -> setiap kelas hero akan disesuaikan supaya lebih adil. Tidak ada yang terlalu kuat atau terlalu lemah.
* **Regenerasi MP otomatis** -> setiap giliran, hero akan mendapatkan tambahan MP. Dengan begitu, pemain bisa tetap menggunakan skill dan tidak cepat kehabisan tenaga.

### Implementasi OOP Versi Pertama

```python
from time import sleep
from abc import ABC, abstractmethod
from random import randint

# Kelas dasar Hero (abstract class)
class Hero(ABC):
    @abstractmethod
    def __init__(self, nama):
        pass

    # Serangan biasa dengan damage random
    def serang(self, musuh):
        actual_dmg = self.dmg + randint(0, 16)
        musuh.hp -= actual_dmg
        print(f"{self.nama} menyerang {musuh.nama} dengan damage {actual_dmg}")

    # Menggunakan skill (cek apakah ada skill dan cukup mana)
    def use_skill(self, musuh, aksi):
        if aksi not in self.skills.keys():
            print('aksi tidak dikenal!')
        elif self.mp >= self.skills[aksi]['manacost']:
            print(f'{self.nama} melakukan jurus {self.skills[aksi]["nama"]}, dmg: {self.skills[aksi]["dmg"]}')
            self.mp -= self.skills[aksi]['manacost']
            musuh.hp -= self.skills[aksi]['dmg']
        else:
            print('mana tidak cukup!')

# Kelas turunan: Warrior
class Warrior(Hero):  # Seimbang
    def __init__(self, nama):
        self.nama, self.cls = nama, "Warrior"
        self.hp, self.mp, self.dmg = 300, 100, 30
        self.skills = {
            'q': {'nama': 'tebasan kilat', 'dmg': 60, 'manacost': 40},
            'w': {'nama': 'tebasan api', 'dmg': 80, 'manacost': 60},
        }

# Kelas turunan: Spearman
class Spearman(Hero):  # Dmg tinggi, hp rendah
    def __init__(self, nama):
        self.nama, self.cls = nama, "Spearman"
        self.hp, self.mp, self.dmg = 250, 120, 35
        self.skills = {
            'q': {'nama': 'tusukan maut', 'dmg': 68, 'manacost': 40},
            'w': {'nama': 'lemparan tombak nagabumi', 'dmg': 90, 'manacost': 60},
        }

# Fungsi untuk memilih aksi
def input_aksi(player):
    skills = player.skills
    print('Masukkan Aksi: ')
    for key in skills.keys():
        print(f' |> {key} -> {skills[key]["nama"]}')
    aksi = input(' |> a -> attack : ')
    return aksi

# Inisialisasi pemain
player1 = Warrior('fikri')
player2 = Spearman('ihsan')

# Main loop
while player1.hp > 0 and player2.hp > 0:
    print("Giliran Player 1!")
    aksi = input_aksi(player1)
    if aksi == 'a':
        player1.serang(player2)
    else:
        player1.use_skill(player2, aksi)

    sleep(1)

    print("Giliran Player 2!")
    aksi = input_aksi(player2)
    if aksi == 'a':
        player2.serang(player1)
    else:
        player2.use_skill(player1, aksi)

    # Regenerasi MP setiap giliran
    player1.mp += randint(10, 21)
    player2.mp += randint(10, 21)

    sleep(1)
    print(
        f'\nP1: {player1.nama}[{player1.cls}] HP:{player1.hp} -- MP:{player1.mp}\n'
        f'=======\n'
        f'P2: {player2.nama}[{player2.cls}] HP:{player2.hp} -- MP:{player2.mp}\n'
    )

# Tentukan pemenang
if player1.hp > player2.hp:
    print('Player1 Menang')
elif player1.hp < player2.hp:
    print('Player2 Menang')
else:
    print('Imbang')
```

## Menambahkan Pilihan Kelas & Hero Baru

Supaya permainan terasa lebih seru dan bervariasi, kita tidak hanya menggunakan satu jenis karakter saja. Kali ini, kita akan menambahkan fitur **pemilihan kelas** sehingga setiap pemain bisa memilih peran atau tipe hero yang berbeda sesuai gaya bermainnya.

Sebagai contoh, kita tambahkan beberapa hero baru:

* **Mage** -> Hero ini memiliki skill berbasis **magic attack** yang bisa memberikan serangan besar, tetapi biasanya memiliki HP yang lebih rendah dibandingkan kelas lain.
* **Assassin** -> Hero ini memiliki kemampuan **critical damage**, yaitu serangan yang sesekali bisa memberikan damage jauh lebih besar dari serangan biasa.

Dengan adanya kelas dan hero baru ini, permainan akan menjadi lebih **strategis**. Pemain harus memilih kelas yang sesuai dengan taktiknya, apakah ingin mengandalkan kekuatan sihir, kecepatan serangan, atau ketahanan tubuh seperti kelas **Warrior** yang sudah kita buat sebelumnya.

### Implementasi

```python
from time import sleep
from abc import ABC, abstractmethod
from random import randint

class Hero(ABC):
    @abstractmethod
    def __init__(self, nama):
        pass

    def serang(self, musuh):
        actual_dmg = self.dmg + randint(0, 16)
        musuh.hp -= actual_dmg
        print(f"{self.nama} menyerang {musuh.nama} dengan damage {actual_dmg}")

    def use_skill(self, musuh, aksi):
        if aksi not in self.skills.keys():
            print('aksi tidak dikenal!')
        elif self.mp >= self.skills[aksi]['manacost']:
            print(f'{self.nama} melakukan jurus {self.skills[aksi]["nama"]}, dmg: {self.skills[aksi]["dmg"]}')
            self.mp -= self.skills[aksi]['manacost']
            musuh.hp -= self.skills[aksi]['dmg']
        else:
            print('mana tidak cukup!')

# Kelas Hero
class Warrior(Hero):
    def __init__(self, nama):
        self.nama, self.cls = nama, "Warrior"
        self.hp, self.mp, self.dmg = 300, 100, 30
        self.skills = {
            'q': {'nama': 'tebasan kilat', 'dmg': 60, 'manacost': 40},
            'w': {'nama': 'tebasan api', 'dmg': 80, 'manacost': 60},
        }

class Spearman(Hero):
    def __init__(self, nama):
        self.nama, self.cls = nama, "Spearman"
        self.hp, self.mp, self.dmg = 250, 120, 35
        self.skills = {
            'q': {'nama': 'tusukan maut', 'dmg': 68, 'manacost': 40},
            'w': {'nama': 'lemparan tombak nagabumi', 'dmg': 90, 'manacost': 60},
        }

class Mage(Hero):
    def __init__(self, nama):
        self.nama, self.cls = nama, "Mage"
        self.hp, self.mp, self.dmg = 230, 150, 25
        self.skills = {
            'q': {'nama': 'angin pemotong', 'dmg': 70, 'manacost': 35},
            'w': {'nama': 'badai petir', 'dmg': 90, 'manacost': 55},
        }

class Assassin(Hero):
    def __init__(self, nama):
        self.nama, self.cls = nama, "Assassin"
        self.hp, self.mp, self.dmg = 210, 80, 37
        self.skills = {
            'q': {'nama': 'backstab', 'dmg': 65, 'manacost': 35},
            'w': {'nama': 'coup de grace', 'dmg': 120, 'manacost': 120},
        }

    def serang(self, musuh):
        peluang_crit = randint(0, 101)
        if peluang_crit <= 40:
            actual_dmg = self.dmg * randint(2, 4)
            musuh.hp -= actual_dmg
            print("CRITICAL DAMAGE!")
            print(f"{self.nama} menyerang {musuh.nama} dengan damage {actual_dmg}")
        else:
            super().serang(musuh)

# Input aksi
def input_aksi(player):
    skills = player.skills
    print('Masukkan Aksi: ')
    for key in skills.keys():
        print(f' |> {key} -> {skills[key]["nama"]} [manacost = {skills[key]["manacost"]}]')
    aksi = input(' |> a -> attack : ')
    return aksi

# Pemilihan kelas
def pilih_kelas(id):
    nama = input(f'Masukkan nama player ke-{id}: ')
    print("Pilih Kelas:\n1. Warrior\n2. Spearman\n3. Mage\n4. Assassin")
    pilihan = input('Masukkan pilihan: ')
    if pilihan == '1':
        return Warrior(nama)
    elif pilihan == '2':
        return Spearman(nama)
    elif pilihan == '3':
        return Mage(nama)
    elif pilihan == '4':
        return Assassin(nama)
    else:
        print('Pilihan tidak dikenal, gunakan kelas default: Warrior.')
        return Warrior(nama)

# Main program
player1 = pilih_kelas(1)
player2 = pilih_kelas(2)

while player1.hp > 0 and player2.hp > 0:
    print("Giliran Player 1!")
    aksi = input_aksi(player1)
    if aksi == 'a':
        player1.serang(player2)
    else:
        player1.use_skill(player2, aksi)

    sleep(1)

    print("Giliran Player 2!")
    aksi = input_aksi(player2)
    if aksi == 'a':
        player2.serang(player1)
    else:
        player2.use_skill(player1, aksi)

    player1.mp += randint(10, 21)
    player2.mp += randint(10, 21)

    sleep(1)
    print(
        f'\nP1: {player1.nama}[{player1.cls}] HP:{player1.hp} -- MP:{player1.mp}\n'
        f'=======\n'
        f'P2: {player2.nama}[{player2.cls}] HP:{player2.hp} -- MP:{player2.mp}\n'
    )

if player1.hp > player2.hp:
    print('Player1 Menang')
elif player1.hp < player2.hp:
    print('Player2 Menang')
else:
    print('Imbang')
```

### Penjelasan

* **Mage**
  Kelas **Mage** sebenarnya tidak terlalu rumit untuk dibuat. Konsep dasarnya masih sama dengan kelas **Hero** yang sudah kita miliki sebelumnya. Kita hanya perlu membuat sebuah kelas baru yang menjadi **turunan (child class)** dari `Hero`, lalu membedakan nilai **stats**-nya, misalnya HP lebih rendah tetapi MP lebih tinggi, serta damage yang berfokus pada serangan sihir. Dengan cara ini, kita tidak perlu menulis ulang semua logika dasar hero, cukup menambahkan perbedaan di atribut yang relevan.

* **Assassin**
  Untuk kelas **Assassin**, implementasinya sedikit lebih menantang. Berbeda dengan Mage, Assassin memiliki kemampuan khusus yaitu **critical hit**. Setiap kali menyerang, Assassin memiliki peluang **40%** untuk menghasilkan serangan **2–4 kali lipat** dari damage normal.
  Karena ada mekanisme khusus ini, kita tidak bisa sekadar menggunakan method `serang()` biasa yang ada di kelas induk. Method tersebut harus **diimplementasikan ulang (override)** di dalam kelas `Assassin`. Pada versi barunya, method `serang()` akan melakukan **pengundian (random check)**:

  * Jika **critical hit terjadi**, maka dijalankan kode khusus yang menghitung damage besar sesuai mekanisme critical.
  * Jika **tidak terjadi**, maka method akan memanggil kode serangan biasa dari kelas asal (menggunakan konsep **super()**).

Dengan pendekatan ini, kita bisa melihat bagaimana konsep **polymorphism** bekerja: meskipun semua hero memiliki method `serang()`, cara kerjanya bisa berbeda tergantung kelas masing-masing.

## Penutup

Selamat!
Kamu sudah berhasil melakukan perjalanan penting dalam belajar Python: mengubah sebuah game sederhana dari paradigma **fungsional** menjadi **Object-Oriented Programming (OOP)** penuh. Dalam proses ini, kamu sudah menerapkan konsep-konsep inti OOP seperti **Inheritance (pewarisan)**, **Abstraction (abstraksi)**, dan **Polymorphism (polimorfisme)**.

Dengan OOP, kode programmu menjadi lebih **rapi, fleksibel, dan mudah dikembangkan**. Kamu tidak perlu lagi menulis kode yang berulang-ulang, karena cukup membuat kerangka dasar yang bisa diturunkan dan disesuaikan untuk hero atau fitur baru.

Tentu, perjalanan belajar belum selesai sampai di sini. Setelah paham dasar-dasarnya, kamu bisa **ber-eksperimen** lebih jauh. Beberapa ide yang bisa dicoba:

1. **Menambah hero baru**

   * *Healer* -> memiliki skill khusus untuk menyembuhkan dirinya sendiri.
   * *Berserker* -> setiap kali menyerang, otomatis memulihkan HP sebesar 25% dari damage yang diberikan ke lawan.

2. **Menambahkan item**
   Misalnya: *healing potion* untuk memulihkan HP, atau *damage buff* untuk meningkatkan serangan sementara.

3. **Memberikan passive skill untuk semua kelas**
   Setiap hero memiliki kemampuan pasif yang otomatis berjalan di setiap giliran. Contoh: regenerasi kecil untuk HP, atau peluang blokir serangan.

4. **Membuat versi grafis dengan framework game**
   Misalnya menggunakan **Pygame**, sehingga game tidak hanya berupa teks di terminal, tetapi bisa memiliki tampilan grafis, animasi, dan kontrol yang lebih interaktif.

Ingat, belajar Python (dan pemrograman secara umum) adalah **perjalanan tanpa akhir**. Semakin kamu mencoba hal baru, semakin banyak pula hal menarik yang bisa kamu kuasai. Jadi, jangan berhenti di sini—teruslah berkreasi!
