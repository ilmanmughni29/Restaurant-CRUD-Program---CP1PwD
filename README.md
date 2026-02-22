# Capstone-Project-1-Purwadhika: Aplikasi "Warung Makan Purwadhika"
Program ini bertujuan untuk membantu pelaku UMKM F&B untuk membuat aplikasi sederhana untuk memesan makanan dan menambah/mengedit menu makanan/minuman. Aplikasi ini mendukung dua peran yang berbeda ketika program dijalankan. Dua peran tersebut adalah Admin (pemilik usaha) dan User (pelanggan/customer). Admin adalah peran yang dapat mengakses semua menu di dalam program, termasuk dapat mengakses fitur yang sensitif seperti menambah menu, memperbaharui (update) menu, dan menu recycle bin. 

## Dependency
1. Python 3.x
2. *Tabulate* library: Untuk menampilkan data dalam bentuk tabel

## Stakeholders
1. Pelaku UMKM (User)
2. Pemesan makanan (Pelanggan/Customer)
3. Teman-teman programmer (Sebagai referensi dan sarana pembelajaran)

## Fitur
Program ini didasari dengan konsep CRUD. Yaitu program yang bisa menjalankan fitur untuk CREATE data, READ data, UPDATE data, dan DELETE data
Berikut merupakan fitur dari aplikasi "Warung Makan Purwadhika":
1. Menambah Menu*
2. Menampilkan Menu
3. Perbaharui Menu*
4. Recycle Bin*
    - Lihat Recycle Bin
    - Hapus Menu
    - Kembalikan Menu yang Dihapus
    - Kosongkan Recycle Bin
    - Keluar
6. Mencari Menu Berdasarkan Kategori
7. Pesan Makanan
8. Exit Main Menu

Fitur dengan simbol bintang atau *asterisk* (*) adalah fitur yang sensitif, yaitu hanya bisa diakses sehingga perlu melakukan login dengan memasukkan Username dan Password yang benar.

## Alur Program
### Menu Utama
<img width="421" height="170" alt="menu utama" src="https://github.com/user-attachments/assets/3f5e91d1-8422-4789-a88b-c3ead001005d" />

Saat program dijalankan, Menu ini yang akan ditampilkan pertama kali.

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

### Mencari Menu Berdasarkan Kategori (Filter)
Berikut merupakan diagram alur ketika "Opsi 5: Mencari Menu Berdasarkan Kategori" dijalankan.

### Pesan Makanan (Order)
Berikut merupakan diagram alur ketika "Opsi 6: Pesan Makanan" dijalankan.
