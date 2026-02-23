# Python CRUD Application for Selecting the Menu in a Restaurant
Program ini bertujuan untuk membantu pelaku UMKM F&B untuk membuat aplikasi sederhana untuk memesan makanan dan menambah/mengedit menu makanan/minuman. Aplikasi ini mendukung dua peran yang berbeda ketika program dijalankan. Dua peran tersebut adalah Admin (pemilik usaha) dan User (pelanggan/customer). Admin adalah peran yang dapat mengakses semua menu di dalam program, termasuk dapat mengakses fitur yang sensitif seperti menambah menu, memperbaharui (update) menu, dan menu recycle bin. 

## Dependency
1. Python 3.x
2. ```Tabulate``` library: Untuk menampilkan data dalam bentuk tabel

## Stakeholders
1. Pelaku UMKM (User)
2. Pemesan makanan (Pelanggan/Customer)
3. Teman-teman programmer (Sebagai referensi dan sarana pembelajaran)

## Fitur
Program ini didasari dengan konsep CRUD. Yaitu program yang bisa menjalankan fitur untuk CREATE data, READ data, UPDATE data, dan DELETE data. Di mana entitas data disimpan di dalam struktur data *dictionary*. *Keys* pada *dictionary* tersebut di antaranya 'ID', 'Kategori', 'Nama', 'Harga', 'Stock', dan 'Notes'.

Berikut merupakan fitur dari aplikasi "Warung Makan Purwadhika":
1. Menambah Menu*
    - Menambah entri data baru sesuai dengan input dari user
    - Menampilkan notifikasi ketika data berhasil ditambahkan
2. Menampilkan Menu
    - Menampilkan entitas data yang tersimpan di *dictionary* secara spesifik
    - Data ditampilkan dalam format tabel dengan memanfaatkan *library* ```tabulate```
    - Program akan secara otomatis memberikan input "Stock habis" pada kolom 'Notes' ketika stock = 0
3. Perbaharui Menu*
    - Memodifikasi data sesuai keinginan user baik pada data 'Kategori', 'Nama', 'Harga', 'Stock', maupun 'Notes'
    - Menampilkan notifikasi konfirmasi maupun error ketika data berhasil atau gagal diupdate
4. Recycle Bin*
    - Lihat Recycle Bin
    - Hapus Menu
       - Menghapus data yang ingin dihilangkan dan memasukkan nya ke dalam *dictionary* ```recycle_bin = []```
       - Karena ada *dictionary* ```recycle_bin = []```, data tidak secara permanen dihapus, melainkan disimpan sementara sehingga memungkinkan user untuk dapat memulihkan data yang dihapus
    - Kembalikan Menu yang Dihapus
       - Memulihkan data yang sudah dihapus (masuk ke ```recycle_bin = []```) dan mengembalikan ke ```database = []```
    - Kosongkan Recycle Bin
       - Menghapus data secara permanen
    - Keluar
5. Mencari Menu Berdasarkan Kategori
    - Menampilkan menu berdasarkan kategori yang diinput oleh user (makanan/minuman/dessert/side dish)
    - Menampilkan data dalam bentuk tabel
6. Pesan Makanan
     - Menu ini mengizinkan *customer*/pelanggan untuk memilih menu yang tersedia di dalam tabel ```database = []```
     - Setelah memilih menu, pelanggan juga diizinkan untuk memilih jumlah menu yang dipesan
     - Selain itu, pelanggan juga memungkinkan untuk menambahkan keterangan/*notes* pada menu yang dipilih
     - Setelah mengetik kata "selesai", akan ditampilkan tabel yang berisi rangkuman pesanan (menu, jumlah, notes, total harga) yang sudah dipilih oleh pelanggan sebelumnya
     - Program juga akan menampilkan jumlah yang harus dibayar
     - Pelanggan dapat meng-input nominal pembayaran berdasarkan jumlah yang harus dibayar
     - Output kembalian juga akan ditampilkan setelah pelanggan memasukkan nominal pembayaran
7. Exit Main Menu

Fitur dengan simbol bintang atau *asterisk* (*) adalah fitur yang sensitif, yaitu hanya bisa diakses sehingga perlu melakukan login dengan memasukkan Username dan Password yang benar.

## Alur Program
### Menu Utama
Saat program dijalankan, Menu ini yang akan ditampilkan pertama kali.


<img width="467" height="161" alt="menu utama" src="https://github.com/user-attachments/assets/c0c8d33c-7f89-4307-a2fc-bef4f4d8b005" />



Berikut merupakan diagram alur ketika Menu Utama dijalankan.


<img width="728" height="751" alt="main menu-main menu drawio" src="https://github.com/user-attachments/assets/5701c1cf-7159-442b-8255-cf82e1244daf" />



### Menambah Menu (Create)
Berikut merupakan diagram alur ketika "Opsi 1: Menambah Menu" dijalankan.


<img width="876" height="452" alt="create menu-create drawio" src="https://github.com/user-attachments/assets/2d13f56c-4fff-4d4f-b0ec-14e71b066a87" />



### Menampilkan Menu (Read)
Berikut merupakan diagram alur ketika "Opsi 2: Menampilkan Menu" dijalankan.


<img width="587" height="382" alt="create menu-read drawio" src="https://github.com/user-attachments/assets/901934d1-5f2f-4ffa-9311-f2f3367aab8e" />



### Perbaharui Menu (Update)
Berikut merupakan diagram alur ketika "Opsi 3: Perbaharui Menu" dijalankan.


<img width="636" height="731" alt="create menu-update drawio" src="https://github.com/user-attachments/assets/cb030a03-219a-4fe8-8810-f09b348edb2b" />



### Recycle Bin (Delete)
Berikut merupakan diagram alur ketika "Opsi 4: Recycle Bin >> Opsi 2: Hapus Menu" dijalankan.


<img width="280" height="681" alt="create menu-delete drawio" src="https://github.com/user-attachments/assets/89f8cdd0-7495-4f39-b634-b18ca9859a5d" />



### Mencari Menu Berdasarkan Kategori (Filter)
Berikut merupakan diagram alur ketika "Opsi 5: Mencari Menu Berdasarkan Kategori" dijalankan.


<img width="121" height="291" alt="create menu-search drawio" src="https://github.com/user-attachments/assets/509533dc-b8f4-4078-9bf1-6e9046d390fa" />



### Pesan Makanan (Order)
Berikut merupakan diagram alur ketika "Opsi 6: Pesan Makanan" dijalankan.


<img width="759" height="931" alt="create menu-order drawio" src="https://github.com/user-attachments/assets/9fa09355-0ba1-4fe7-a416-ab9e297de625" />



## Contributing
Jika terdapat pertanyaan, mengalami masalah, atau memiliki saran untuk perbaikan, silahkan email ke ilmanmughni29@gmail.com.

We welcome contributions to this project! If you have any inquiries, encounter any problems, or have suggestions for improvements, please feel free to email me to ilmanmughni29@gmail.com.
