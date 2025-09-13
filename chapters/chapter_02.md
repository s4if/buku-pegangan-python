# Algoritma Pemrograman

## **Pengenalan Algoritma Pemrograman**

### **Sejarah Algoritma**

Istilah "algoritma" berasal dari nama seorang ilmuwan Persia bernama Abu Ja’far Mohammed Ibn Musa al-Khowarizmi, yang hidup pada abad ke-9. Ia menulis sebuah buku berjudul *al-mukhtaṣar fī ḥisāb al-jabr wal-muqābala*, yang dalam bahasa Inggris dikenal sebagai *The Compendious Book on Calculation by Completion and Balancing*. Karya ini mengandung dasar-dasar ilmu aljabar dan dianggap sebagai salah satu buku matematika paling berpengaruh di dunia. Dari namanya, muncullah kata "algoritma" yang kini digunakan dalam dunia teknologi untuk menggambarkan urutan langkah yang logis untuk menyelesaikan masalah. [^n4]

### **Definisi Algoritma**

Secara umum, algoritma adalah serangkaian langkah atau instruksi yang dirancang untuk menyelesaikan masalah tertentu. Langkah-langkah ini harus jelas, terstruktur, dan dapat diterapkan secara berulang pada situasi atau data yang berbeda untuk mendapatkan hasil yang diinginkan. Dalam kehidupan sehari-hari, kita sering menggunakan algoritma, meskipun mungkin tidak kita sadari. Misalnya, resep masakan adalah algoritma—langkah-langkah sistematis untuk menghasilkan hidangan.

### **Algoritma dalam Pemrograman**

Dalam konteks pemrograman, algoritma lebih spesifik sebagai urutan langkah yang digunakan untuk menyelesaikan masalah matematika atau logika dengan bantuan komputer. Pemrograman adalah proses menuliskan algoritma tersebut dalam bahasa pemrograman agar komputer dapat menjalankannya. Sebagai contoh, sebuah algoritma bisa digunakan untuk menyelesaikan masalah seperti pengurutan angka dari yang terkecil hingga yang terbesar, menghitung rata-rata nilai, atau bahkan memprediksi cuaca berdasarkan data historis.

### **Sifat-Sifat Algoritma**

Agar algoritma bisa digunakan secara efektif, menurut **Donald E.Knuth** ia harus memenuhi beberapa kriteria penting yaitu:

- **Terdefinisi dengan baik *(Definiteness)***: Setiap langkah dalam algoritma harus jelas dan tidak ambigu, sehingga siapa pun yang membaca algoritma tersebut akan memahami apa yang harus dilakukan.
- **Terbatas *(Finiteness)***: Algoritma harus berakhir setelah sejumlah langkah tertentu. Algoritma yang tidak memiliki titik akhir akan terus berjalan tanpa pernah menyelesaikan masalah.
- **Efisien**: Algoritma harus disusun sedemikian rupa agar dapat menyelesaikan masalah dalam waktu dan sumber daya yang efisien.
- **Input dan Output**: Algoritma harus menerima input (data awal) dan menghasilkan output (hasil dari langkah-langkah pemrosesan).

## **Penulisan Algoritma Pemrograman**

Algoritma pemrograman dapat dituliskan dengan tiga macam notasi yaitu *Kalimat Terstruktur*, *Pseudo Code* dan *Flowchart*

Berikut elaborasi untuk poin tentang *Kalimat Terstruktur* dalam algoritma pemrograman:

### **Kalimat Terstruktur**

*Kalimat terstruktur* adalah cara sederhana untuk mendeskripsikan langkah-langkah sebuah algoritma dengan menggunakan bahasa yang mudah dipahami. Notasi ini menggunakan kalimat biasa yang diatur secara jelas dan berurutan. Tidak ada aturan baku yang harus diikuti, tetapi penting untuk menyusun setiap langkah dengan rapi dan logis agar mudah dimengerti. Kalimat terstruktur sering digunakan ketika algoritma masih dalam tahap awal perancangan atau ketika kita mencoba untuk menjelaskan cara kerja algoritma kepada seseorang yang tidak terlalu familiar dengan pemrograman.

**Kelebihan:**

- **Mudah dipahami**: Karena menggunakan bahasa sehari-hari, kalimat terstruktur dapat dimengerti oleh siapa saja, bahkan oleh orang yang belum mengerti bahasa pemrograman.
- **Fleksibel**: Tidak ada aturan ketat, sehingga kita bisa menulisnya dengan gaya yang paling nyaman.

**Kekurangan:**

- **Tidak standar**: Karena tidak ada aturan khusus, setiap orang mungkin akan menulisnya dengan cara yang berbeda, sehingga bisa sulit untuk diubah menjadi kode pemrograman.
- **Sulit dikonversi menjadi kode**: Notasi ini lebih mudah dipahami manusia, namun terkadang sulit diterjemahkan langsung menjadi kode program karena tidak mengikuti format tertentu seperti *pseudo code* atau *flowchart*.

**Contoh Penggunaan:**
Misalnya, jika kita ingin membuat algoritma sederhana untuk menambahkan dua angka, kita bisa menuliskannya dengan kalimat terstruktur sebagai berikut:

```plaintext
Algoritma penjumlahan
1. Masukkan angka pertama (angka1)
2. Masukkan angka kedua (angka2)
3. Jumlahkan angka1 dan angka2 dan simpan hasilnya
4. Tampilkan hasil penjumlahan
```

Pada contoh ini, setiap langkah diuraikan secara jelas dan berurutan, sehingga pembaca dapat mengikuti prosesnya dengan mudah. Misalnya, pada langkah pertama dan kedua, kita meminta pengguna memasukkan dua angka. Kemudian, kita menjumlahkan kedua angka tersebut dan menyimpan hasilnya. Langkah terakhir adalah menampilkan hasil penjumlahan.

**Aplikasi dalam Pemrograman:**
Walaupun *kalimat terstruktur* cocok digunakan untuk algoritma sederhana, jika kita ingin mengubah algoritma ini menjadi kode program, mungkin akan sedikit sulit karena kalimat-kalimat tersebut harus diterjemahkan terlebih dahulu ke dalam sintaksis bahasa pemrograman. Misalnya, dalam Python, algoritma penjumlahan tersebut dapat diimplementasikan seperti berikut:

```python
# Algoritma penjumlahan dalam Python
angka1 = int(input("Masukkan angka pertama: "))
angka2 = int(input("Masukkan angka kedua: "))
hasil = angka1 + angka2
print("Hasil penjumlahan:", hasil)
```

Seperti yang terlihat, setiap kalimat terstruktur diterjemahkan menjadi instruksi yang bisa dijalankan oleh komputer. Meskipun kalimat terstruktur sangat membantu dalam tahap awal perancangan algoritma, untuk menjalankan algoritma tersebut dalam komputer, kita tetap perlu mengubahnya menjadi kode yang sesuai dengan aturan bahasa pemrograman yang digunakan.

Jadi, *kalimat terstruktur* adalah titik awal yang baik dalam merancang algoritma karena menawarkan fleksibilitas dan kemudahan pemahaman, tetapi harus diperhalus lebih lanjut agar bisa diimplementasikan dalam kode program.

Berikut elaborasi mengenai *Pseudo Code* dan penjelasan lebih dalam tentang penerapannya dalam pemrograman:

### **Pseudo Code**

**Definisi:**
*Pseudo Code* adalah cara penulisan algoritma yang menyerupai bahasa pemrograman, namun tidak mengikuti aturan ketat dari bahasa pemrograman apapun. Dengan menulis algoritma dalam bentuk *pseudo code*, kita dapat menjembatani antara rancangan logika algoritma dan penerjemahan algoritma tersebut ke dalam kode program yang sesungguhnya. Tujuan utama dari *pseudo code* adalah untuk memudahkan proses konversi dari langkah-langkah logis menjadi sintaks pemrograman.

*Pseudo code* banyak menggunakan elemen-elemen umum dalam pemrograman seperti perintah *if-else*, *while*, *for*, dan lain-lain, yang biasanya diambil dari berbagai bahasa pemrograman. Meskipun tidak dapat dijalankan oleh komputer, *pseudo code* menawarkan kejelasan dan struktur yang mendekati bahasa pemrograman sehingga programmer lebih mudah memahami dan menerjemahkannya ke dalam kode sebenarnya.

**Ciri-Ciri:**

- Menggunakan bahasa yang mirip dengan bahasa pemrograman, tetapi tetap dalam bentuk yang bisa dipahami oleh manusia.
- Tidak mengikuti aturan sintaksis ketat seperti dalam bahasa pemrograman, sehingga lebih fleksibel dan mudah dimodifikasi.
- Terdiri dari dua bagian penting: **Deklarasi** (untuk mendeklarasikan variabel dan tipe data) dan **Deskripsi** (alur langkah-langkah atau instruksi logika algoritma).

**Bagian-Bagian Pseudo Code:**

1. **Deklarasi**: Pada bagian ini, kita mendefinisikan variabel yang digunakan dalam algoritma beserta tipe datanya. Ini serupa dengan bagian deklarasi variabel dalam bahasa pemrograman, di mana kita memberi tahu komputer jenis data apa yang akan digunakan.

2. **Deskripsi**: Di sini, kita menuliskan langkah-langkah algoritma, menggunakan elemen-elemen logika seperti operasi matematika, kondisi (if-else), perulangan (loops), dan sebagainya. Deskripsi ini akan diubah menjadi kode program sesungguhnya ketika algoritma sudah siap diimplementasikan.

**Kelebihan Pseudo Code:**

- **Lebih dekat dengan bahasa pemrograman**: *Pseudo code* lebih mudah dikonversi ke dalam kode program yang sebenarnya karena bentuknya sudah menyerupai sintaks pemrograman.
- **Fleksibilitas**: Walaupun menyerupai bahasa pemrograman, *pseudo code* tetap lebih bebas dalam struktur dan tidak terikat aturan ketat, sehingga bisa ditulis dengan berbagai gaya tanpa harus memperhatikan kesalahan sintaksis.
- **Lebih mudah untuk dipahami oleh programmer**: Karena menggunakan istilah yang dekat dengan bahasa pemrograman, *pseudo code* sangat membantu programmer untuk membayangkan bagaimana algoritma akan diimplementasikan dalam kode.

**Kekurangan Pseudo Code:**

- **Tidak bisa dieksekusi langsung**: Meskipun mendekati bahasa pemrograman, *pseudo code* tidak bisa dijalankan oleh komputer dan harus dikonversi terlebih dahulu ke dalam bahasa pemrograman yang sebenarnya.
- **Variabilitas penulisan**: Berbeda dengan bahasa pemrograman yang memiliki aturan sintaks baku, *pseudo code* bisa ditulis dengan gaya yang berbeda oleh setiap orang, sehingga kadang bisa membingungkan jika standar penulisan tidak konsisten.

**Contoh:**
Berikut adalah contoh *pseudo code* sederhana untuk algoritma penjumlahan dua angka:

```plaintext
Algoritma penjumlahan
Deklarasi:
  a, b, hasil: integer

Deskripsi:
  input a
  input b
  hasil <- a + b
  print hasil
```

Penjelasan:

- Pada bagian **Deklarasi**, kita mendeklarasikan variabel `a`, `b`, dan `hasil` sebagai tipe data integer (bilangan bulat).
- Pada bagian **Deskripsi**, kita menuliskan alur langkah-langkah algoritma. Pertama, kita meminta input dari pengguna untuk variabel `a` dan `b`. Lalu, kita menjumlahkan kedua variabel tersebut dan menyimpan hasilnya ke variabel `hasil`. Terakhir, kita menampilkan hasil penjumlahan.

**Aplikasi dalam Pemrograman:**
*Pseudo code* sangat berguna dalam merancang algoritma sebelum langsung menuliskannya dalam bahasa pemrograman. Misalnya, ketika mengembangkan program yang lebih kompleks seperti pengurutan data atau pencarian informasi, menuliskannya terlebih dahulu dalam *pseudo code* dapat membantu programmer untuk mengatur alur logika sebelum berurusan dengan detail teknis dari bahasa pemrograman yang digunakan.

Dengan menuliskan algoritma dalam bentuk *pseudo code*, kita dapat membuat rancangan yang mudah dipahami dan diimplementasikan oleh tim, tanpa harus khawatir tentang kesalahan sintaks atau aturan spesifik dari bahasa pemrograman.

### **Diagram Alur *(Flowchart)***

Flowchart adalah alat visual yang digunakan untuk merepresentasikan alur kerja atau proses dalam bentuk diagram. Dalam dunia pemrograman dan sistem, flowchart digunakan untuk merencanakan, menganalisis, dan memahami langkah-langkah yang diperlukan dalam menyelesaikan suatu tugas atau masalah. [^n5]

#### **Model dan Jenis Flowchart**

Flowchart atau bagan alur merupakan diagram yang menggunakan simbol-simbol grafis untuk merepresentasikan urutan langkah, proses, atau aktivitas dalam menyelesaikan suatu masalah. Ada dua model utama flowchart yang umum digunakan, yaitu:

1. **System Flowchart**
2. **Program Flowchart**

##### **System Flowchart (Bagan Alur Sistem)**

**System flowchart** adalah jenis flowchart yang digunakan untuk menggambarkan keseluruhan sistem peralatan komputer yang terlibat dalam proses pengolahan data. Bagan ini menunjukkan hubungan antara satu perangkat dengan perangkat lainnya dalam suatu sistem informasi.

Penjelasan lebih lanjut:

- Tidak dimaksudkan untuk menjelaskan urutan langkah-langkah logis dalam memecahkan suatu masalah.
- Lebih berfokus pada gambaran fisik atau infrastruktur sistem, seperti perangkat keras (hardware), perangkat lunak (software), media penyimpanan data, dan jalur komunikasi data.
- Digunakan untuk memvisualisasikan prosedur atau proses kerja dalam sistem yang dibentuk, termasuk alur data antar bagian atau antar perangkat.
- Berguna dalam tahap analisis dan perancangan sistem untuk membantu pemahaman struktur teknologi informasi dalam organisasi.

Contoh: Sistem komputer memiliki keyboard, monitor, sistem proses dan sistem penyimpanan. Hubungan antar sistem dan jalur perpindahan data dapat dituls dengan system flowchart seperti dibawah.

![system image](images/system_flowchart.png)

##### **Program Flowchart (Bagan Alur Program)**

**Program flowchart** adalah jenis flowchart yang digunakan untuk menggambarkan secara visual urutan logika atau alur dari suatu program komputer. Bagan ini sangat penting dalam dunia pemrograman karena membantu programmer dalam merancang solusi sebelum menulis kode.

Ada dua metode utama dalam membuat program flowchart, yaitu:

###### **Conceptual Flowchart**

- Merupakan bagan alur yang menggambarkan alur pemecahan masalah secara umum atau konseptual.
- Tidak terlalu detail dalam hal langkah-langkah teknis, tetapi memberikan gambaran besar tentang cara suatu masalah akan diselesaikan melalui program.
- Digunakan pada tahap awal perencanaan program untuk menyusun ide dan logika dasar.
- Contoh:

###### **Detail Flowchart**

- Merupakan bagan alur yang menggambarkan proses pemecahan masalah secara lengkap dan rinci.
- Semua langkah, kondisi, dan operasi ditampilkan secara spesifik sesuai dengan alur program yang akan dibuat.
- Sangat berguna untuk meminimalkan kesalahan logika saat penulisan kode dan mempermudah proses debugging.

Dengan kedua jenis flowchart tersebut, seorang programmer dapat lebih mudah memahami serta menerjemahkan algoritma menjadi program yang dapat dijalankan oleh komputer.

#### **Simbol-simbol dalam Flowchart**

##### **Flow direction symbols**

Digunakan untuk menghubungkan simbol satu dengan yang lain, disebut juga connecting line
Macamnya:

![simbol_arus](images/simbol_arus.png)

##### **Processing symbols**

Menunjukan jenis operasi pengolahan dalam suatu proses / prosedur  
Macamnya:  
![simbol_proses](images/simbol_proses.png)

##### **Input / Output symbols**

Menunjukkan jenis input atau output dari suatu sistem
Macamnya:  
![simbol_io](images/simbol_io.png)

[^n4]: sumber: [https://id.wikipedia.org/wiki/Algoritma](https://id.wikipedia.org/wiki/Algoritma)
[^n5]: sumber: [https://bee.telkomuniversity.ac.id/pengertian-flowchart-fungsi-jenis-simbol-dan-contohnya/](https://bee.telkomuniversity.ac.id/pengertian-flowchart-fungsi-jenis-simbol-dan-contohnya/)
