# Pemanfaatan Fungsi, Struktur Kontrol, dan Struktur Data pada Python

## **Pendahuluan**

Selamat datang di bab ini. Pada bagian ini, kita akan mempelajari bagaimana sebuah kode dapat berkembang layaknya tanaman—berawal dari sesuatu yang sederhana, kemudian bertumbuh menjadi lebih kompleks dan terstruktur. Dalam dunia pemrograman, proses ini dikenal dengan istilah **refactoring** (menyusun ulang kode untuk memperbaiki strukturnya tanpa mengubah fungsi) serta **evolusi kode**.

Kita akan memulai dengan sebuah permainan sederhana, lalu secara bertahap menyempurnakannya dengan menambahkan fungsi, struktur kontrol (seperti percabangan `if-else` dan perulangan `while`), serta struktur data (seperti `dictionary` dan `list`). Dengan demikian, Anda dapat mengikuti secara langsung bagaimana sebuah program berkembang dari bentuk awal yang sederhana menuju versi yang lebih teratur dan lebih kuat.

Mari kita mulai pembahasan ini.

## Langkah 1: Game Dasar Pemain vs Monster

**Tujuan:**

Pada versi pertama, tujuan kita sederhana: membuat game turn-based (bergiliran) untuk satu pemain yang melawan sebuah monster. Pemain bisa melakukan serangan dasar atau menggunakan skill khusus.

**Kode:**

```python
from time import sleep
player = {
    'name':'fikri', 'cls':'warrior', 'hp':150,'mp': 100, 'dmg': 15,
    'skills' : {
        'q':{'name':'tebasan kilat', 'dmg':50, 'manacost': 40},
        'w':{'name':'tebasan api', 'dmg':70, 'manacost': 60},
        },
    }
monster = dict(name='goblin', hp=200, dmg=20)

while player['hp'] > 0 and monster['hp'] > 0:
    skills = player['skills']
    
    print('Masukkan Aksi: ') # input aksi
    for key in skills.keys():
        print(' |> {} -> {}'.format(key, skills[key]['name']))
    aksi = input(' |> a -> attack : ')

    if aksi == 'a': # aksi dari player
        print('{} menyerang {} memberikan dmg sebesar {}'.format(
            player['name'], monster['name'], player['dmg']))
        monster['hp'] = monster['hp'] - player['dmg']
        
    else :
        if aksi not in skills.keys():
            print('aksi tidak dikenal!')
            
        elif player['mp'] >= skills[aksi]['manacost']:
            print('{} melakukan jurus {}, dmg: {}'.format(
                player['name'], skills[aksi]['name'], skills[aksi]['dmg']))
            player['mp'] = player['mp'] - skills[aksi]['manacost']
            monster['hp'] = monster['hp'] - skills[aksi]['dmg']
            # akhir edit
        else:
            print('mana tidak cukup!')
        
    sleep(1) 
    print('monster menyerang player dengan dmg: {}'.format(monster['dmg']))
    player['hp'] = player['hp'] - monster['dmg']
    sleep(1) 
    player['mp'] += 20
    print('\nPlayer HP:{}, Player MP:{}\nMonster HP:{}\n'.format(
        player['hp'], player['mp'], monster['hp']
        ))

if player['hp'] > monster['hp']: print('Player Menang')
else : print('Monster Menang!')
```

**Penjelasan Keadaan Saat Ini:**
Kode di atas adalah game sederhana dimana pemain (player) bertarung melawan monster. Pemain memiliki Health Point (HP), Mana Point (MP), damage dasar (dmg), dan dua skill khusus. Monster juga memiliki HP dan damage. Game berjalan dalam loop selama HP pemain dan monster di atas 0. Di setiap giliran, pemain memilih aksi: menyerang (a) atau menggunakan skill (q/w).

**Penjelasan 'Bagaimana' dan 'Mengapa':**

- Kita menggunakan **dictionary** untuk menyimpan data player dan monster karena strukturnya fleksibel dan bisa menampung berbagai jenis data (string, integer, bahkan dictionary lain untuk skills).
- **Struktur kontrol `while`** digunakan untuk membuat loop permainan selama kedua karakter masih hidup.
- **Struktur kontrol `if-else`** yang bersarang (nested) digunakan untuk menangani logika pemilihan aksi pemain: apakah itu serangan biasa, skill, atau aksi tidak valid.
- Kita juga menggunakan `sleep(1)` untuk memberi jeda antar aksi sehingga permainan terasa lebih natural.

**Mempersiapkan Langkah Selanjutnya:**
Kode ini sudah berfungsi dengan baik, tetapi ada beberapa masalah:

1. **Kode campur aduk:** Semua logika ada dalam satu loop besar. Ini seperti menaruh semua barang di satu kamar—berantakan dan susah dicari.
2. **Sulit dikembangkan:** Bayangkan jika kita ingin menambah monster lain atau fitur baru. Kita harus mengotak-atik loop utama yang sudah rumit, yang berisiko menimbulkan bug.
3. **Tidak modular:** Jika kita ingin menggunakan logika serangan yang sama untuk monster, kita harus menyalin-tempel kode, yang tidak efisien.

Oleh karena itu, kita perlu **merapikan kode** dengan memecahnya menjadi bagian-bagian kecil yang disebut **fungsi**. Ini akan memudahkan kita untuk membaca, memahami, dan mengembangkan game ini lebih lanjut.

## Langkah 2: Refactoring dengan Fungsi

**Tujuan:** Sekarang, kita akan memecah kode yang berantakan tadi menjadi beberapa fungsi. Tujuannya adalah meningkatkan **keterbacaan** (readability) dan **kemampuan pemeliharaan** (maintainability) kode.

**Kode:**

```python
from time import sleep

# data player/monster
player = {
    'name':'fikri', 'cls':'warrior', 'hp':150,'mp': 100, 'dmg': 15,
    'skills' : {
        'q':{'name':'tebasan kilat', 'dmg':50, 'manacost': 40},
        'w':{'name':'tebasan api', 'dmg':70, 'manacost': 60},
        },
    }
monster = dict(name='goblin', hp=200, dmg=20)

def input_aksi(player):
    skills = player['skills']
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
while player['hp'] > 0 and monster['hp'] > 0:

    # input aksi player
    aksi = input_aksi(player)
    # aksi dari player dijalankan
    player, monster = aksi_dijalankan(aksi, player, monster)
        
    # aksi dari monster
    sleep(1) 
    player = basic_attack(monster, player)

    # tampilan hp/mp dari player
    sleep(1) 
    print('\nPlayer HP:{}, Player MP:{}\nMonster HP:{}\n'.format(
        player['hp'], player['mp'], monster['hp']
        ))

if player['hp'] > monster['hp']: print('Player Menang')
else : print('Monster Menang!')
```

**Penjelasan Keadaan Saat Ini:**
Kode ini memiliki fungsionalitas yang sama persis dengan Langkah 1. Namun, kodenya jauh lebih terstruktur. Logika yang sebelumnya berantakan di dalam loop sekarang telah dipisah menjadi fungsi-fungsi: `input_aksi`, `basic_attack`, dan `aksi_dijalankan`.

**Penjelasan 'Bagaimana' dan 'Mengapa':**

- **Fungsi `input_aksi`:** Bertugas hanya untuk menampilkan pilihan aksi dan menerima input dari user. Ini memisahkan logika input dari logika permainan.
- **Fungsi `basic_attack`:** Menangani serangan dasar. Dengan membuatnya sebagai fungsi, kita bisa memanggilnya baik untuk player maupun monster (seperti yang terlihat pada `basic_attack(monster, player)`), tanpa perlu menulis kode yang sama dua kali. Ini prinsip **DRY (Don't Repeat Yourself)**.
- **Fungsi `aksi_dijalankan`:** Menangani semua logika kompleks terkait pemilihan aksi. Fungsi ini menerima input `aksi`, `player`, dan `musuh`, lalu memutuskan apa yang harus dilakukan berdasarkan aksi tersebut.
- **Loop utama** sekarang menjadi sangat bersih dan mudah dibaca. Alur program terlihat jelas: minta input, jalankan aksi, monster menyerang, tampilkan status.
  
**Mempersiapkan Langkah Selanjutnya**
Dengan struktur yang sudah berfungsi, kode kini lebih siap untuk dikembangkan. Sebagai contoh, bayangkan jika permainan yang semula berbentuk *Player vs Monster* (PvE) diubah menjadi *Player vs Player* (PvP). Pertanyaan yang muncul adalah: langkah apa saja yang perlu dilakukan untuk mewujudkan perubahan tersebut?

1. Kita perlu **dua set data player**, bukan satu player dan satu monster.
2. Loop utama perlu diubah agar kedua player bergantian memilih aksi.
3. Fungsi `basic_attack` dan `aksi_dijalankan` sudah bisa digunakan untuk player mana pun karena menerima parameter. Ini keuntungan besar dari refactoring!

Keterbatasan kode saat ini adalah data monster (`monster = dict(...)`) dan logika di loop utama yang masih khusus untuk PvE (misalnya, monster selalu menyerang dengan `basic_attack`). Mari kita evolusi lagi!

## Langkah 3: Evolusi Menuju Game Multiplayer (PvP)

**Tujuan:** Mengembangkan game PvE kita menjadi game Player vs Player (PvP), di mana dua pemain saling bertarung.

**Kode:**

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
    skills = player['skills']
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
```

**Penjelasan Keadaan Saat Ini**
Permainan kini telah berkembang menjadi mode *Player vs Player* (PvP). Dua pemain, yaitu `player1` dan `player2`, saling berhadapan dengan data karakter yang setara dalam kompleksitas, mencakup nama, HP, MP, *damage*, serta keterampilan (*skill*). Kedua pemain tersebut bergantian menjalankan aksi dalam permainan.

**Penjelasan 'Bagaimana' dan 'Mengapa':**

- **Perubahan Data:** Kita mengganti dictionary `monster` dengan dictionary `player2`. Struktur datanya sama dengan `player1`, yang membuktikan bahwa fungsi `basic_attack` dan `aksi_dijalankan` kita memang bersifat umum (bisa untuk player atau monster).
- **Perubahan Loop Utama:** Loop `while` sekarang memeriksa HP kedua player. Di dalam loop, giliran setiap player ditandai dengan pesan `print("Giliran Player X!")`.
- **Fungsi Tetap Sama:** Kita tidak perlu mengubah *isi* dari fungsi `input_aksi`, `basic_attack`, atau `aksi_dijalankan` sama sekali. Kita hanya perlu memanggilnya dengan parameter yang berbeda (`player1` dan `player2` bergantian sebagai `player` dan `musuh`). Ini menghemat banyak waktu dan tenaga!
- **Kondisi Akhir:** Kita menambahkan kondisi `elif` untuk menangani kemungkinan hasil imbang.

## Keterbatasan untuk Pengembangan Lebih Lanjut

Meskipun permainan PvP yang telah dibuat sudah berfungsi dengan baik, selalu terdapat ruang untuk pengembangan lebih lanjut. Beberapa kemungkinan perbaikan yang dapat dipertimbangkan antara lain:

1. **Pilihan Kelas Pemain:** Pada versi sebelumnya, pemain hanya dapat menggunakan kelas yang telah ditentukan. Sebagai pengembangan, permainan dapat dibuat agar setiap pemain dapat memilih kelas tertentu, misalnya *Swordsman*, *Spearman*, *Mage*, atau *Paladin*.

2. **AI untuk Monster:** Jika ingin menambahkan kembali mode PvE, monster dapat diberikan kemampuan untuk menggunakan keterampilan layaknya pemain. Untuk itu, diperlukan fungsi AI yang dapat menentukan aksi yang dilakukan oleh monster.

3. **Manajemen Kode yang Lebih Baik:** Seiring bertambahnya jumlah keterampilan atau properti pemain, struktur data dalam bentuk *dictionary* akan menjadi semakin panjang dan sulit dikelola. Dalam hal ini, penggunaan **kelas (Class)** dengan pendekatan Pemrograman Berorientasi Objek (OOP) dapat menjadi solusi yang lebih rapi dan terstruktur.

Poin-poin di atas merupakan tantangan yang dapat dicoba secara mandiri untuk melanjutkan pengembangan permainan.

## Ringkasan Pelajaran

Perjalanan evolusi kode dalam bab ini dapat dirangkum sebagai berikut:

1. **Langkah 1 (Dasar):** Kita memulai dengan kode yang masih sederhana dan belum terstruktur dengan baik, namun sudah berfungsi. Pada tahap ini, kita belajar menggunakan **dictionary** untuk menyimpan data yang lebih kompleks, serta **struktur kontrol** (`while`, `if-elif-else`) untuk mengatur alur permainan. Keterbatasannya adalah kode tidak modular dan sulit dikembangkan lebih lanjut.

2. **Langkah 2 (Refactoring):** Kita kemudian memperkenalkan **fungsi** untuk memecah kode menjadi bagian-bagian yang lebih spesifik. Hal ini meningkatkan keterbacaan sekaligus memudahkan pemeliharaan. Prinsip **DRY (Don't Repeat Yourself)** diterapkan, misalnya dengan membuat fungsi `basic_attack` yang dapat digunakan oleh berbagai karakter.

3. **Langkah 3 (Evolusi PvP):** Dengan fondasi fungsi yang sudah terbangun, kita dapat mengubah permainan dari PvE menjadi PvP hanya dengan menyesuaikan **data** (dari monster menjadi player2) dan **logika utama** (urutan pemanggilan fungsi). Perubahan ini tidak memerlukan penyesuaian pada isi fungsi-fungsi yang telah dibuat.

Inti dari pembelajaran ini adalah pentingnya merencanakan struktur kode dengan baik. Mulailah dari bentuk sederhana, lalu lakukan refactoring ke dalam fungsi-fungsi yang jelas agar kode dapat berkembang dengan lebih mudah di masa depan.
