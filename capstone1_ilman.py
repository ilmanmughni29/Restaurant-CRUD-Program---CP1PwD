from tabulate import tabulate

# Membuat database menu makanan & minuman
database = [
    {'id': 0, 'kategori': 'makanan', 'nama': 'nasi', 'harga': 5000.0, 'stock': 10, 'notes':''},
    {'id': 1, 'kategori': 'makanan', 'nama': 'ayam geprek', 'harga': 15000.0, 'stock': 10, 'notes':''},
    {'id': 2, 'kategori': 'minuman', 'nama': 'es teh manis', 'harga': 7000.0, 'stock': 10, 'notes':''},
    {'id': 3, 'kategori': 'dessert', 'nama': 'cheese cake', 'harga': 25000.0, 'stock': 10, 'notes':''},
    {'id': 4, 'kategori': 'makanan', 'nama': 'rendang', 'harga': 20000.0, 'stock': 10, 'notes':''},
    {'id': 5, 'kategori': 'makanan', 'nama': 'telor dadar', 'harga': 8000.0, 'stock': 10, 'notes':''},
    {'id': 6, 'kategori': 'side dish', 'nama': 'mix platter', 'harga': 30000.0, 'stock': 10, 'notes':''},
    {'id': 7, 'kategori': 'makanan', 'nama': 'nasi campur bali', 'harga': 40000.0, 'stock': 10, 'notes':''},
    {'id': 8, 'kategori': 'minuman', 'nama': 'es jeruk', 'harga': 10000.0, 'stock': 10, 'notes':''},
    {'id': 9, 'kategori': 'minuman', 'nama': 'jus alpukat', 'harga': 20000.0, 'stock': 10, 'notes':''},
    {'id': 10, 'kategori': 'side dish', 'nama': 'cah kangkung', 'harga': 15000.0, 'stock': 10, 'notes':''}
]

# Membuat database recycle bin untuk menu yang dihapus
recycle_bin = []


# Fungsi untuk login
def login():
    username = 'admin'
    password = 'admin123'
    attempts = 2
    
    while attempts > 0:
        print("=== Silahkan Login Terlebih Dahulu! ===")
        input_uname = input("Masukkan username: ")
        input_password = input("Masukkan password: ")
        
        if input_uname == username and input_password == password:
            print("Login Berhasil! Selamat Datang Admin!")
            return True
        else:
            attempts -= 1
            print("Login Gagal! Username/Password salah!")
            print(f"Sisa percobaan: {attempts}")
            

# Fungsi untuk menjalankan menu utama
def main():
    while True:
        print('''=== SELAMAT DATANG DI WARUNG MAKAN PURWADHIKA! ===:
              1. Menambah Menu* 
              2. Menampilkan Menu
              3. Perbaharui Menu*
              4. Recycle Bin*
              5. Mencari Menu Berdasarkan Kategori
              6. Pesan Makanan/Minuman/Dessert/Side Dish!
              7. Exit Main Menu''')
        user_input = input("Pilih Opsi (1 - 7): ")
        if not user_input.isdigit():
            print("Input harus berupa angka!")
            continue
        option = int(user_input)
        if option == 1:
            if login():
                create_data()
        elif option == 2:
            read_data()
        elif option == 3:
            if login():
                update_data()
        elif option == 4:
            if login():
                recycle_bin_menu()
        elif option == 5:
            search_menu()
        elif option == 6:
            select_menu()
        elif option == 7:
            break
        else:
            print(f"Opsi {option} Invalid")
            print()

         
# Fungsi untuk menambahkan data baru ke dalam database          
def create_data():
    print("=== Menambahkan Data Baru ===")
    category = input("Masukkan kategori (makanan/minuman/dessert/side dish): ").lower()
    name = input("Masukkan nama makanan/minuman/dessert/side dish: ").lower()
    price = float(input("Masukkan harga: "))
    stock = int(input("Masukkan jumlah stock: "))
    notes = input("Masukkan catatan (jika ada), tekan 'enter' jika tidak ada: ")
    
    if database:
        highest_id = 0
        for item in database:
            if item['id'] > highest_id:
                highest_id = item['id']
            new_id = highest_id + 1
    else:
        new_id = 0

    new_item = {
        'id': new_id,
        'kategori': category,
        'nama': name,
        'harga': price,
        'stock': stock,
        'notes': notes
    }
    
    database.append(new_item)
    print(f"Data berhasil ditambahkan: {new_item}")


# Fungsi untuk menampilkan seluruh menu makanan dan minuman dalam bentuk tabel
def read_data():
    print("=== Menu Warung Makan Purwadhika ===")
    if database:
        for item in database:
            if item['stock'] == 0:
                item['notes'] = "Stock habis"
        print(tabulate(database, headers='keys', tablefmt='fancy_grid'))
    else:
        print("Database kosong.")


# Fungsi untuk mengubah/meng-update data di dalam database (kolom/baris)
def update_data():
    print("=== Update Data ===")
    
    while True:
        id_input = input("Masukkan ID menu yang ingin diupdate: ")
        if not id_input.isdigit():
            print("Input tidak valid. ID harus berupa angka.")
            continue
        
        id_to_update = int(id_input)
        item = None
        for i in database:
            if i['id'] == id_to_update:
                item = i
                break
            
        if item:
            print(f"Data saat ini: {item}")
            
            category = input("Masukkan kategori baru (makanan/minuman/dessert/side dish) atau tekan 'enter' untuk tidak mengubah: ").lower()
            name = input("Masukkan nama makanan/minuman/dessert/side dish baru atau tekan 'enter' untuk tidak mengubah: ").lower()
            price = input("Masukkan harga baru atau tekan 'enter' untuk tidak mengubah: ")
            stock = input("Masukkan jumlah stock baru atau tekan 'enter' untuk tidak mengubah: ")
            notes = input("Masukkan catatan atau tekan 'enter' untuk tidak mengubah: ")
            
            if category:
                item['kategori'] = category
            if name:
                item['nama'] = name
            if price:
                if price.isdigit():  # cek apakah input angka (bisa float)
                    item['harga'] = float(price)
                else:
                    print("Harga tidak valid. Harus berupa angka!")
            if stock:
                if stock.isdigit():  # cek apakah input angka (bisa float)
                    item['stock'] = float(stock)
                else:
                    print("Input tidak valid. Stock harus berupa angka!")
            if notes:
                item['notes'] = notes
            
            print(f"Data berhasil diupdate: {item}")
            return
        else:
            print(f"Menu dengan ID {id_to_update} tidak ditemukan.")


# Fungsi untuk menjalankan menu recycle bin (view, delete, restore)
def recycle_bin_menu():
    while True:
        print('''=== Recycle Bin ===
            1. Lihat Recycle Bin
            2. Hapus Menu
            3. Kembalikan Menu yang Dihapus
            4. Kosongkan Recycle Bin
            5. Keluar''')
        
        user_input = input("Pilih Opsi (1 - 5): ")
        if not user_input.isdigit():
            print("Input harus berupa angka!")
            continue
        option = int(user_input)
        if option == 1:
            view_recycleBin()
        elif option == 2:
            delete_data()
        elif option == 3:
            restore_data()
        elif option == 4:
            empty_recycleBin()
        elif option == 5:
            break
        else:
            print(f"Input {option} invalid!")
            print()
    
    
# Fungsi untuk menghapus data di dalam database dan memasukkannya ke dalam recycle bin
def delete_data():
    print("=== Hapus Data ===")
    
    id_input = input("Masukkan ID menu yang ingin dihapus: ")
    if not id_input.isdigit():
        print("Input tidak valid. ID harus berupa angka!")
        return
    
    id_to_delete = int(id_input)
    item_index = None
    i = 0
    for item in database:
        if item['id'] == id_to_delete:
            item_index = i
            break
        i += 1

    if item_index is not None:
        # Simpan data yang akan dihapus ke recycle bin
        recycle_bin.append(database[item_index])
        del database[item_index]
        print(f"Menu dengan ID {id_to_delete} berhasil dihapus dan dipindahkan ke recycle bin.")
    else:
        print(f"Menu dengan ID {id_to_delete} tidak ditemukan.")        
    
    
# Fungsi untuk merestorasi/mengembalikan data yang ada di dalam recycle bin
def restore_data():
    print("=== Restore Data dari Recycle Bin ===")
    
    if not recycle_bin:
        print("Recycle bin kosong. Tidak ada data untuk direstore.")
        return
    
    id_input = input("Masukkan ID menu yang ingin direstore: ")
    if not id_input.isdigit():
        print("Input tidak valid. ID harus berupa angka!")
        return
    
    id_to_restore = int(id_input)
    for index, item in enumerate(recycle_bin):
        if item['id'] == id_to_restore:
            item_index = index
            break
        else:
            item_index = None

    if item_index is not None:
        #Pindahkan data dari recycle bin kembali ke database
        database.append(recycle_bin[item_index])
        del recycle_bin[item_index]
        print(f"Menu dengan ID {id_to_restore} BERHASIL DIRESTORE ke database!")
    else:
        print(f"Menu dengan ID {id_to_restore} TIDAK DITEMUKAN di recycle bin.")


# Fungsi untuk menghapus/mengosongkan data di dalam recycle bin secara permanen
def empty_recycleBin():
    if recycle_bin:
        confirm = input("Apakah anda ingin mengosongkan Recycle Bin?\nPilih 'y' jika iya, 'n' jika tidak --> ").lower()
        if confirm == 'y':
            recycle_bin.clear()
            print("Recycle bin berhasil dikosongkan!")
        elif confirm == 'n':
            print("Recycle Bin tidak jadi dikosongkan.")
        else:
            print(f"Input {confirm} invalid! Pilih 'y' atau 'n'!")
            return empty_recycleBin()
    else:
        print("Recycle bin kosong. Tidak ada data untuk dihapus.")


# Fungsi untuk menampilkan data di dalam recycle bin
def view_recycleBin():
    if recycle_bin:
        print("=== Data di Recycle Bin ===")
        print(tabulate(recycle_bin, headers='keys', tablefmt='grid'))
    else:
        print("Recycle bin kosong.")


# Fungsi untuk mencari menu berdasarkan kategori (makanan/minuman/dessert/side dish)
def search_menu():
    print("=== Cari Menu Berdasarkan Kategori ===")
    category_input = input("Masukkan kategori yang ingin dicari:\n(makanan/minuman/dessert/side dish) --> ").lower()
    
    hasil = []
    for item in database:
        if item['kategori'] == category_input:
            hasil.append(item)
            
    if hasil:
        print(tabulate(hasil, headers='keys', tablefmt='grid'))
    else:
        print(f"Tidak ada menu dengan kategori '{category_input}'.")
    

# Fungsi untuk memesan menu makanan dan minuman yang ada di dalam database dan menjumlahkan menu pilihan user
def select_menu():
    print("=== Pesan Menu ===")
    read_data()  # tampilkan semua menu
    
    order = []
    total_price = 0.0
    sum_total_price = 0.0
    
    while True:
        id_input = input("Masukkan ID menu yang ingin dipesan (atau ketik 'selesai' untuk selesai): ")
        
        if id_input.lower() == 'selesai':
            break
        
        if not id_input.isdigit():
            print("Input tidak valid. ID harus berupa angka.")
            continue
        
        id_order = int(id_input)
        item = None
        
        for i in database:
            if i['id'] == id_order:
                item = i
                break              
        
        if item:
            if item['stock'] > 0:
                qty_input = input(f"Masukkan jumlah '{item['nama'].upper()}' yang ingin dipesan: ")
                if not qty_input.isdigit():
                    print("Input tidak valid. Jumlah harus berupa angka.")
                    continue
                quantity = int(qty_input)
                item['stock'] = item['stock'] - quantity
                if item['stock'] < 0:
                    item['stock'] = item['stock'] + quantity
                    print(f"Jumlah pesanan melebihi stock yang ada!\nSisa stock: {item['stock']}")
                    continue
                notes_input = input(f"Masukkan catatan untuk menu '{item['nama'].upper()}': ")
                total_price = item['harga'] * quantity
                sum_total_price += total_price
                print(f"Menu '{item['nama'].upper()}' berhasil ditambahkan ke pesanan.")
                print()
                
                new_order = {
                    'ID':item['id'],
                    'Kategori':item['kategori'],
                    'Nama':item['nama'],
                    'Harga':item['harga'],
                    'Jumlah':quantity,
                    'Total Harga':total_price,
                    'Notes':notes_input
                }
                
                order.append(new_order)
                
            else:
                print(f"Stock '{item['nama'].upper()}' habis")
        else:
            print(f"Menu dengan ID {id_order} tidak ditemukan atau tidak tersedia.")
    
    if order:
        print("\n=== Ringkasan Pesanan ===")
        print(tabulate(order, headers='keys', tablefmt='grid'))
        print(f"Total harga pesanan: Rp {sum_total_price:,.0f}")
        
        # Proses pembayaran
        while True:
            payment_input = (input("Masukkan nominal uang untuk membayar: Rp "))       
            if not payment_input.isdigit():
                print("Input harus berupa angka!")
                continue
                
            payment = float(payment_input)
            if payment >= sum_total_price:
                change = payment - sum_total_price
                print(f"Pembayaran sukses!\nUang kembalian anda: Rp {change:,.0f}")
                print("Silahkan Menikmati!")
                print()
                return
            elif payment < sum_total_price:
                print("Uang pembayaran lebih rendah dari total harga.")
            
        
    else:
        print("Tidak ada pesanan yang dibuat.")


main()