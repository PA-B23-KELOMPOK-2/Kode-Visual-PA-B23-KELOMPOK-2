import mysql.connector
from mysql.connector import Error
from prettytable import PrettyTable
import getpass

try:
    mydb = mysql.connector.connect(
        host="sql6.freesqldatabase.com",
        user="sql6701169",
        password="Lh6evPczGK",
        database="sql6701169"
    )
    mycursor = mydb.cursor()
except Error as e:
    print("Error saat menghubungkan ke database:", e)
    exit()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display_admin(self):
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID Admin", "Nama Admin", "Email Admin", "Password Admin", "Role"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

    def display_perkotaan(self):
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID", "Nama Kota", "Provinsi", "Jumlah Penduduk", "Luas Wilayah", "indeks keberlanjutan_kota", "ID ADMIN"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)
    
    def display_pemukiman(self):
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID Pemukiman", "Nama Pemukiman", "ID Perkotaan", "Jenis Pemukiman", "Akses Air Bersih", "Akses Sanitasi Layak", "ID ADMIN"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)

    def display_proyek(self):
        current = self.head
        x = PrettyTable()
        x.field_names = ["ID Proyek", "Nama Proyek", "ID Pemukiman", "Deskripsi Proyek", "Jenis Proyek", "Dana Proyek", "Status Proyek", "ID ADMIN"]
        while current:
            x.add_row(current.data)
            current = current.next
        print(x)
        
def quick_sort(arr, ascending=True):
    try:
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2][0]
        left = [x for x in arr if x[0] < pivot]
        middle = [x for x in arr if x[0] == pivot]
        right = [x for x in arr if x[0] > pivot]
        if ascending:
            return quick_sort(left, ascending) + middle + quick_sort(right, ascending)
        else:
            return quick_sort(right, ascending) + middle + quick_sort(left, ascending)
    except Exception as e:
        print("Error saat melakukan sorting:", e)

def jump_search(arr, x):
    try:
        n = len(arr)
        step = int(n ** 0.5)
        prev = 0
        while arr[min(step, n)-1][0] < x:
            prev = step
            step += int(n ** 0.5)
            if prev >= n:
                return -1
        while arr[prev][0] < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if arr[prev][0] == x:
            return prev
        return -1
    except Exception as e:
        print("Error saat melakukan pencarian:", e)
        return -1
    
def input_handler(prompt, type='str', min=0, max=None):
    while True:
        try:
            if type == 'str':
                user_input = input(prompt).strip()
            elif type == 'int':
                user_input = int(input(prompt))
            
            if '\\' in user_input or '\t' in user_input: 
                print("Terdeteksi karakter spesial di input\n")
                continue
            if min > len(user_input):
                print(f"Panjang minimum {min} karakter\n")
                continue
            if max is not None and max < len(user_input):
                print(f"Panjang melewati batas maksimum {max} karakter\n")
                continue
            return user_input
        except ValueError:
            print("input hanya bisa berupa angka (integer)\n")
        except:
            print("\nNgapain hayo\n")

def read_admin():
    try:
        mycursor.execute("SELECT * FROM admin")
        myresult = mycursor.fetchall()
        ll = LinkedList()
        for data in myresult:
            ll.append(data)
        ll.display_admin()
    except Error as e:
        print("Error saat membaca data admin:", e)

def tambah_data_admin():
    try:
        nama_admin = input_handler("Masukkan Nama Admin: ", min=5, max=50)
        email_admin = input_handler("Masukkan Email Admin: ", min=5, max=100)
        password_admin = input_handler("Masukkan Password Admin: ", min=5, max=50)
        role = input_handler("Masukkan Role Admin: ", min=5, max=50)
        query = f"""
        INSERT INTO admin (nama_admin, email_admin, password_admin, role)
        VALUES ('{nama_admin}', '{email_admin}', '{password_admin}', '{role}')
        """
        mycursor.execute(query)
        mydb.commit()
        print("Data Admin berhasil ditambahkan")
    except Error as e:
        print("Error saat menambahkan data admin:", e)

def hapus_data_admin():
    try:
        id_admin = int(input_handler("Masukkan ID Admin yang ingin dihapus: "))
        query = f"DELETE FROM admin WHERE id_admin = {id_admin}"
        mycursor.execute(query)
        mydb.commit()
        print("Data Admin berhasil dihapus")
    except ValueError:
        print("Masukkan ID Admin yang valid.")
    except Error as e:
        print("Error saat menghapus data admin:", e)

def perbarui_data_admin():
    try:
        id_admin = int(input_handler("Masukkan ID Admin yang ingin diperbarui: "))
        nama_admin = input_handler("Masukkan Nama Admin Baru: ", min=5, max=50)
        email_admin = input_handler("Masukkan Email Admin Baru: ", min=5, max=100)
        password_admin = input_handler("Masukkan Password Admin: ", min=5, max=50)
        role = input_handler("Masukkan Role Admin: ", min=5, max=50)

        query = f"""
        UPDATE admin
        SET nama_admin = '{nama_admin}',
        email_admin = '{email_admin}',
        password_admin = '{password_admin}',
        role = '{role}'
        WHERE id_admin = {id_admin}
        """

        mycursor.execute(query)
        if mycursor.rowcount == 0:
            print("ID Admin tidak ditemukan.")
        else:
            mydb.commit()
            print("Data Admin berhasil diperbarui")
    except ValueError:
        print("Masukkan ID Admin dalam bentuk bilangan bulat.")
    except Exception as e:
        print("Terjadi kesalahan:", e)

def read_perkotaan():
    try:
        mycursor.execute("SELECT * FROM perkotaan")
        myresult = mycursor.fetchall()
        data_list = []
        for data in myresult:
            data_list.append(data)

        while True:
            print("============================================================")
            print("|                 TAMPILKAN DATA PERKOTAAN                 |")
            print("============================================================")
            print("|   1. Tampilkan Data (urutkan berdasarkan ID - A-Z)       |")
            print("|   2. Tampilkan Data (urutkan berdasarkan ID - Z-A)       |")
            print("|   3. Cari Data (berdasarkan ID)                          |")
            print("|   4. Kembali ke Menu Utama                               |")
            print("============================================================")

            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                sorted_data = quick_sort(data_list, ascending=True)
                ll = LinkedList()
                for data in sorted_data:
                    ll.append(data)
                ll.display_perkotaan()
            elif pilihan == "2":
                sorted_data = quick_sort(data_list, ascending=False)
                ll = LinkedList()
                for data in sorted_data:
                    ll.append(data)
                ll.display_perkotaan()
            elif pilihan == "3":
                id_to_search = int(input_handler("Masukkan ID yang ingin dicari: "))
                result_index = jump_search(data_list, id_to_search)
                if result_index != -1:
                    print("Data ditemukan:")
                    x = PrettyTable()
                    x.field_names = ["ID", "Nama Kota", "Provinsi", "Jumlah Penduduk", "Luas Wilayah", "Indeks Keberlanjutan", "ID ADMIN"]
                    x.add_row(data_list[result_index])
                    print(x)
                else:
                    print("Data tidak ditemukan.")
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
    except ValueError:
        print("Input tidak valid.")
    except Error as e:
        print("Error saat membaca data perkotaan:", e)


def tambah_data_perkotaan():
    try:
        nama_kota = input_handler( "Masukkan Nama Kota: " ,min=5, max=50)
        provinsi = input_handler("Masukkan Provinsi: " ,min=5, max=50)
        jumlah_penduduk = int(input_handler("Masukkan Jumlah Penduduk: "))

        luas_wilayah = None
        while luas_wilayah is None:
            try:
                luas_wilayah = float(input_handler("Masukkan Luas Wilayah: "))
            except ValueError:
                print("Luas wilayah harus berupa angka.")

        indeks_keberlanjutan_kota = int(input_handler("Masukkan Indeks Keberlanjutan Kota: "))
        id_admin = int(input_handler("Masukkan ID Admin: "))

        if jumlah_penduduk < 0 or luas_wilayah < 0:
            raise ValueError("Jumlah penduduk dan luas wilayah tidak boleh negatif")

        query_check_admin = f"SELECT id_admin FROM admin WHERE id_admin = {id_admin}"
        mycursor.execute(query_check_admin)
        result_admin = mycursor.fetchone()

        if not result_admin:
            print("ID Admin tidak ditemukan dalam database.")
            return

        query = f"""
        INSERT INTO perkotaan (nama_kota, provinsi, jumlah_penduduk, luas_wilayah, indeks_keberlanjutan_kota, id_admin)
        VALUES ('{nama_kota}', '{provinsi}', {jumlah_penduduk}, {luas_wilayah}, {indeks_keberlanjutan_kota}, {id_admin})
        """

        mycursor.execute(query)
        mydb.commit()

    except ValueError:
        print("Data berhasil ditambahkan")

    except Error as e:
        print("Input tidak valid.")
        print("Error saat menambahkan data perkotaan:", e)


def hapus_data_perkotaan():
    try:
        id_perkotaan = int(input_handler("Masukkan ID Perkotaan yang ingin dihapus: "))

        query = f"DELETE FROM perkotaan WHERE id_perkotaan = {id_perkotaan}"

        mycursor.execute(query)
        mydb.commit()
        print("Data berhasil dihapus")
    except ValueError:
        print("Input tidak valid.")
    except Error as e:
        print("Error saat menghapus data perkotaan:", e)

def perbarui_data_perkotaan():
    try:
        id_perkotaan = int(input_handler("Masukkan ID Perkotaan yang ingin diperbarui: "))
        nama_kota = input_handler("Masukkan Nama Kota Baru: ",min=5, max=50)
        provinsi = input_handler("Masukkan Provinsi Baru: ",min=5, max=50)
        jumlah_penduduk = int(input_handler("Masukkan Jumlah Penduduk Baru: "))

        luas_wilayah = None
        while luas_wilayah is None:
            try:
                luas_wilayah = float(input_handler("Masukkan Luas Wilayah: "))
            except ValueError:
                print("Luas wilayah harus berupa angka.")

        indeks_keberlanjutan_kota = int(input_handler("Masukkan Indeks Keberlanjutan Kota Baru: "))
        id_admin = input_handler("Masukkan ID Admin: ")

        if jumlah_penduduk < 0 or luas_wilayah < 0:
            raise ValueError("Jumlah penduduk dan luas wilayah tidak boleh negatif")

        query_check_admin = f"SELECT id_admin FROM admin WHERE id_admin = {id_admin}"
        mycursor.execute(query_check_admin)
        result_admin = mycursor.fetchone()

        if not result_admin:
            print("ID Admin tidak ditemukan dalam database.")
            return

        query = f"""
        UPDATE perkotaan
        SET nama_kota = '{nama_kota}', 
        provinsi = '{provinsi}',
        jumlah_penduduk = {jumlah_penduduk}, 
        luas_wilayah = {luas_wilayah},
        indeks_keberlanjutan_kota = {indeks_keberlanjutan_kota}
        WHERE id_perkotaan = {id_perkotaan} AND id_admin = {id_admin}
        """
        
        mycursor.execute(query)

        if mycursor.rowcount == 0:
            print("ID Perkotaan atau ID Admin tidak ditemukan.")

        else:
            mydb.commit()
            print("Data berhasil diperbarui")

    except ValueError:
        print("Pastikan input berupa bilangan bulat untuk ID perkotaan, jumlah penduduk, dan indeks keberlanjutan, serta bilangan pecahan untuk luas wilayah.")

    except Exception as e:
        print("Terjadi kesalahan:", e)


def read_pemukiman():
    try:
        mycursor.execute("SELECT * FROM pemukiman")
        myresult = mycursor.fetchall()
        data_list = []
        for data in myresult:
            data_list.append(data)

        while True:
            print("============================================================")
            print("|                 TAMPILKAN DATA PEMUKIMAN                 |")
            print("============================================================")
            print("|   1. Tampilkan Data (urutkan berdasarkan ID - A-Z)       |")
            print("|   2. Tampilkan Data (urutkan berdasarkan ID - Z-A)       |")
            print("|   3. Cari Data (berdasarkan ID)                          |")
            print("|   4. Kembali ke Menu Utama                               |")
            print("============================================================")

            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                sorted_data = quick_sort(data_list, ascending=True)
                ll = LinkedList()
                for data in sorted_data:
                    ll.append(data)
                ll.display_pemukiman()
            elif pilihan == "2":
                sorted_data = quick_sort(data_list, ascending=False)
                ll = LinkedList()
                for data in sorted_data:
                    ll.append(data)
                ll.display_pemukiman()
            elif pilihan == "3":
                id_to_search = int(input_handler("Masukkan ID yang ingin dicari: "))
                result_index = jump_search(data_list, id_to_search)
                if result_index != -1:
                    print("Data ditemukan:")
                    x = PrettyTable()
                    x.field_names = ["ID Pemukiman", "Nama Pemukiman", "ID Perkotaan", "Jenis Pemukiman", "Akses Air Bersih", "Akses Sanitasi Layak", "ID ADMIN"]
                    x.add_row(data_list[result_index])
                    print(x)
                else:
                    print("Data tidak ditemukan.")
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
    except ValueError:
        print("Input tidak valid.")
    except Error as e:
        print("Error saat membaca data pemukiman:", e)


def tambah_data_pemukiman():
    try:
        nama_pemukiman = input_handler("Masukkan Nama Pemukiman: ",min=5, max=50)
        id_perkotaan = int(input_handler("Masukkan ID Perkotaan: "))
        jenis_pemukiman = input_handler("Masukkan Jenis Pemukiman Formal/informal: ",min=5, max=50)
        akses_air_bersih = input_handler("Masukkan Akses Air Bersih ya/tidak: ",min=5, max=50)
        akses_sanitasi_layak = input_handler("Masukkan Akses Sanitasi Layak ya/tidak: ",min=5, max=50)
        id_admin = int(input_handler("Masukkan ID Admin: "))

        query_check_perkotaan = f"SELECT id_perkotaan FROM perkotaan WHERE id_perkotaan = {id_perkotaan}"
        mycursor.execute(query_check_perkotaan)
        result_perkotaan = mycursor.fetchone()

        if not result_perkotaan:
            print("ID Perkotaan tidak ditemukan dalam database.")
            return

        query_check_admin = f"SELECT id_admin FROM admin WHERE id_admin = {id_admin}"
        mycursor.execute(query_check_admin)
        result_admin = mycursor.fetchone()

        if not result_admin:
            print("ID Admin tidak ditemukan dalam database.")
            return

        query_insert_pemukiman = f"""
        INSERT INTO pemukiman (nama_pemukiman, id_perkotaan, jenis_pemukiman, akses_air_bersih, akses_sanitasi_layak, id_admin)
        VALUES ('{nama_pemukiman}', {id_perkotaan}, '{jenis_pemukiman}', '{akses_air_bersih}', '{akses_sanitasi_layak}', {id_admin})
        """

        mycursor.execute(query_insert_pemukiman)
        mydb.commit()
        print("data berhasil di tambahkan")
    except ValueError as e:
        print("Input tidak valid:", e)

    except Error as e:
        print("Error saat menambahkan data pemukiman:", e)


def hapus_data_pemukiman():
    try:
        id_pemukiman = int(input_handler("Masukkan ID Pemukiman yang ingin dihapus: "))

        query = f"DELETE FROM pemukiman WHERE id_pemukiman = {id_pemukiman}"

        mycursor.execute(query)
        mydb.commit()
        print("Data berhasil dihapus")
    except ValueError:
        print("Input tidak valid.")
    except Error as e:
        print("Error saat menghapus data pemukiman:", e)

def perbarui_data_pemukiman():
    try:
        id_pemukiman = int(input_handler("Masukkan ID Pemukiman yang ingin diperbarui: "))
        nama_pemukiman = input_handler("Masukkan Nama Pemukiman Baru: ",min=5, max=50)
        id_perkotaan = int(input_handler("Masukkan ID Perkotaan Baru: "))
        jenis_pemukiman = input_handler("Masukkan Jenis Pemukiman Baru Formal/informal : ",min=5, max=50)
        akses_air_bersih = input_handler("Masukkan Akses Air Bersih Baru ya/tidak : ",min=5, max=50)
        akses_sanitasi_layak = input_handler("Masukkan Akses Sanitasi Layak Baru ya/tidak : ",min=5, max=50)
        id_admin = int(input_handler("Masukkan ID Admin: "))

        query_check_perkotaan = f"SELECT id_perkotaan FROM perkotaan WHERE id_perkotaan = {id_perkotaan}"
        mycursor.execute(query_check_perkotaan)
        result_perkotaan = mycursor.fetchone()

        if not result_perkotaan:
            print("ID Perkotaan tidak ditemukan dalam database.")
            return
        
        query_check_admin = f"SELECT id_admin FROM admin WHERE id_admin = {id_admin}"
        mycursor.execute(query_check_admin)
        result_admin = mycursor.fetchone()

        if not result_admin:
            print("ID Admin tidak ditemukan dalam database.")
            return
        query = f"""
        UPDATE pemukiman
        SET nama_pemukiman = '{nama_pemukiman}',
        id_perkotaan = {id_perkotaan},
        jenis_pemukiman = '{jenis_pemukiman}',
        akses_air_bersih = '{akses_air_bersih}',
        akses_sanitasi_layak = '{akses_sanitasi_layak}',
        id_admin = {id_admin}
        WHERE id_pemukiman = {id_pemukiman}
        """

        mycursor.execute(query)
        if mycursor.rowcount == 0:
            print("ID Pemukiman tidak ditemukan.")
        else:
            mydb.commit()
            print("Data berhasil diperbarui")
    except ValueError:
        print("Pastikan input berupa bilangan bulat untuk ID pemukiman dan ID perkotaan.")
    except Exception as e:
        print("Terjadi kesalahan:", e)


def read_proyek():
    try:
        mycursor.execute("SELECT * FROM proyek")
        myresult = mycursor.fetchall()
        data_list = []
        for data in myresult:
            data_list.append(data)

        while True:
            print("============================================================")
            print("|                 TAMPILKAN DATA PROYEK                    |")
            print("============================================================")
            print("|   1. Tampilkan Data (urutkan berdasarkan ID - A-Z)       |")
            print("|   2. Tampilkan Data (urutkan berdasarkan ID - Z-A)       |")
            print("|   3. Cari Data (berdasarkan ID)                          |")
            print("|   4. Kembali ke Menu Utama                               |")
            print("============================================================")
            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                sorted_data = quick_sort(data_list, ascending=True)
                ll = LinkedList()
                for data in sorted_data:
                    ll.append(data)
                ll.display_proyek()
            elif pilihan == "2":
                sorted_data = quick_sort(data_list, ascending=False)
                ll = LinkedList()
                for data in sorted_data:
                    ll.append(data)
                ll.display_proyek()
            elif pilihan == "3":
                id_to_search = int(input_handler("Masukkan ID yang ingin dicari: "))
                result_index = jump_search(data_list, id_to_search)
                if result_index != -1:
                    print("Data ditemukan:")
                    x = PrettyTable()
                    x.field_names = ["ID Proyek", "Nama Proyek", "ID Pemukiman", "Deskripsi Proyek", "Jenis Proyek", "Dana Proyek", "Status Proyek", "ID ADMIN"]
                    x.add_row(data_list[result_index])
                    print(x)
                else:
                    print("Data tidak ditemukan.")
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
    except ValueError:
        print("Input tidak valid.")
    except Error as e:
        print("Error saat membaca data proyek:", e)

def tambah_data_proyek():
    try:
        nama_proyek = input_handler("Masukkan Nama Proyek: ", min=5, max=255)
        id_pemukiman = int(input_handler("Masukkan ID Pemukiman: "))
        deskripsi_proyek = input_handler("Masukkan Deskripsi Proyek: ", min=5, max=500)
        jenis_proyek = input_handler("Masukkan Jenis Proyek: " , min=5, max=50)
        dana_proyek = int(input_handler("Masukkan Dana Proyek: "))
        status_proyek = input_handler("Masukkan Status Proyek: ", min=5, max=50)
        id_admin = int(input_handler("Masukkan ID Admin: "))
        
        if dana_proyek < 0:
            raise ValueError("Dana proyek tidak boleh minus")

        query_check_pemukiman = f"SELECT id_pemukiman FROM pemukiman WHERE id_pemukiman = {id_pemukiman}"
        mycursor.execute(query_check_pemukiman)
        result_pemukiman = mycursor.fetchone()

        if not result_pemukiman:
            print("ID pemukiman tidak ditemukan dalam database.")
            return

        query_check_admin = f"SELECT id_admin FROM admin WHERE id_admin = {id_admin}"
        mycursor.execute(query_check_admin)
        result_admin = mycursor.fetchone()

        if not result_admin:
            print("ID admin tidak ditemukan dalam database.")
            return

        query = f"""
        INSERT INTO proyek (nama_proyek, id_pemukiman, deskripsi_proyek, jenis_proyek, dana_proyek, status_proyek, id_admin)
        VALUES ('{nama_proyek}', {id_pemukiman}, '{deskripsi_proyek}', '{jenis_proyek}', {dana_proyek}, '{status_proyek}', {id_admin})
        """

        mycursor.execute(query)
        mydb.commit()
        print("Data berhasil ditambahkan")
    except ValueError:
        print("Input tidak valid.")
    except mysql.connector.Error as e:
        print("Error saat menambahkan data proyek:",e)

def hapus_data_proyek():
    try:
        id_proyek = int(input_handler("Masukkan ID Proyek yang ingin dihapus: "))

        query = f"DELETE FROM proyek WHERE id_proyek = {id_proyek}"

        mycursor.execute(query)
        mydb.commit()
        print("Data berhasil dihapus")
    except ValueError:
        print("Input tidak valid.")
    except Error as e:
        print("Error saat menghapus data proyek:", e)

def perbarui_data_proyek():
    try:
        id_proyek = int(input_handler("Masukkan ID Proyek yang ingin diperbarui: " ))
        nama_proyek = input_handler("Masukkan Nama Proyek Baru: " , min=5, max=255) 
        id_pemukiman = int(input_handler("Masukkan ID Pemukiman Baru: "))
        deskripsi_proyek = input_handler("Masukkan Deskripsi Proyek Baru: " , min=5, max=500)
        jenis_proyek = input_handler("Masukkan Jenis Proyek Baru: " , min=5, max=50)
        dana_proyek = int(input_handler("Masukkan Dana Proyek Baru: "))
        status_proyek = input_handler("Masukkan Status Proyek Baru: " , min=5, max=50)
        id_admin = int(input_handler("Masukkan ID Admin: "))

        if dana_proyek < 0:
            raise ValueError("Dana proyek tidak boleh negatif")
     
        query_check_pemukiman = f"SELECT id_pemukiman FROM pemukiman WHERE id_pemukiman = {id_pemukiman}"
        mycursor.execute(query_check_pemukiman)

        result_pemukiman = mycursor.fetchone()

        if not result_pemukiman:
            print("ID pemukiman tidak ditemukan dalam database.")
            return

        query_check_admin = f"SELECT id_admin FROM admin WHERE id_admin = {id_admin}"
        mycursor.execute(query_check_admin)

        result_admin = mycursor.fetchone()

        if not result_admin:
            print("ID admin tidak ditemukan dalam database.")
            return
        
        query = f"""
        UPDATE proyek
        SET nama_proyek = '{nama_proyek}',
        id_pemukiman = {id_pemukiman},
        deskripsi_proyek = '{deskripsi_proyek}',
        jenis_proyek = '{jenis_proyek}',
        dana_proyek = {dana_proyek},
        status_proyek = '{status_proyek}',
        id_admin = {id_admin}
        WHERE id_proyek = {id_proyek}
        """

        mycursor.execute(query)
        if mycursor.rowcount == 0:
            print("ID Proyek tidak ditemukan.")
        else:
            mydb.commit()
            print("Data berhasil diperbarui")
    except ValueError:
        print("Pastikan input berupa bilangan bulat untuk ID proyek, ID pemukiman, dan dana proyek.")
    except mysql.connector.Error as e:
        print("Terjadi kesalahan SQL:", e)
    except Exception as e:
        print("Terjadi kesalahan:",e)


def menu_utama_admin():
    while True:
        try:
            
            print("============================================================")
            print("|                   DATABASE ADMIN                         |")
            print("============================================================")
            print("|                1. TAMBAH DATA ADMIN                      |")
            print("|                2. HAPUS DATA ADMIN                       |")
            print("|                3. PERBARUI DATA ADMIN                    |")
            print("|                4. TAMPILKAN DATA ADMIN                   |")
            print("|                5. Keluar                                 |")
            print("============================================================")
            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                tambah_data_admin()
            elif pilihan == "2":
                hapus_data_admin()
            elif pilihan == "3":
                perbarui_data_admin()
            elif pilihan == "4":
                read_admin()
            elif pilihan == "5":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except (EOFError, KeyboardInterrupt):
            print("Program keluar.")
            break
            
def menu_utama_perkotaan():
    while True:
        try:
            
            print("============================================================")
            print("|                   DATABASE PERKOTAAN                     |")
            print("============================================================")
            print("|                1. TAMBAH DATA PERKOTAAN                  |")
            print("|                2. HAPUS DATA PERKOTAAN                   |")
            print("|                3. PERBARUI DATA PERKOTAAN                |")
            print("|                4. TAMPILKAN DATA PERKOTAAN               |")
            print("|                5. Keluar                                 |")
            print("============================================================")
            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                tambah_data_perkotaan()
            elif pilihan == "2":
                hapus_data_perkotaan()
            elif pilihan == "3":
                perbarui_data_perkotaan()
            elif pilihan == "4":
                read_perkotaan()
            elif pilihan == "5":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except (EOFError, KeyboardInterrupt):
            print("Program keluar.")
            break

def menu_utama_pemukiman():
    while True:
        try:
            
            print("============================================================")
            print("|                   DATABASE PEMUKIMAN                     |")
            print("============================================================")
            print("|                1. TAMBAH DATA PEMUKIMAN                  |")
            print("|                2. HAPUS DATA PEMUKIMAN                   |")
            print("|                3. PERBARUI DATA PEMUKIMAN                |")
            print("|                4. TAMPILKAN DATA PEMUKIMAN               |")
            print("|                5. Keluar                                 |")
            print("============================================================")
            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                tambah_data_pemukiman()
            elif pilihan == "2":
                hapus_data_pemukiman()
            elif pilihan == "3":
                perbarui_data_pemukiman()
            elif pilihan == "4":
                read_pemukiman()
            elif pilihan == "5":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except (EOFError, KeyboardInterrupt):
            print("Program keluar.")
            break
def menu_utama_proyek():
    while True:
        try:
            
            print("============================================================")
            print("|                   DATABASE PROYEK                        |")
            print("============================================================")
            print("|                1. TAMBAH DATA PROYEK                     |")
            print("|                2. HAPUS DATA PROYEK                      |")
            print("|                3. PERBARUI DATA PROYEK                   |")
            print("|                4. TAMPILKAN DATA PROYEK                  |")
            print("|                5. Keluar                                 |")
            print("============================================================")
            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                tambah_data_proyek()
            elif pilihan == "2":
                hapus_data_proyek()
            elif pilihan == "3":
                perbarui_data_proyek()
            elif pilihan == "4":
                read_proyek()
            elif pilihan == "5":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except (EOFError, KeyboardInterrupt):
            print("Program keluar.")
            break

def menu_utama_SUPER_ADMIN():
    while True:
        try:
            
            print("============================================================")
            print("                  selamat datang:",username                  )
            print("============================================================")
            print("|                1. DATABASE ADMIN                         |")
            print("|                2. DATABASE PERKOTAAN                     |")
            print("|                3. DATABASE PEMUKIMAN                     |")
            print("|                4. DATABASE PROYEK                        |")
            print("|                5. Keluar                                 |")
            print("============================================================")
            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                menu_utama_admin()
            elif pilihan == "2":
                menu_utama_perkotaan()
            elif pilihan == "3":
                menu_utama_pemukiman()
            elif pilihan == "4":
                menu_utama_proyek()
            elif pilihan == "5":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except (EOFError, KeyboardInterrupt):
            print("Program keluar.")
            break

def menu_user():
    while True:
        try:
           
            print("============================================================")
            print("                  selamat datang:",username                  )
            print("============================================================")
            print("|                1. DATABASE PERKOTAAN                     |")
            print("|                2. DATABASE PEMUKIMAN                     |")
            print("|                3. DATABASE PROYEK                        |")
            print("|                4. Keluar                                 |")
            print("============================================================")
            pilihan = input_handler("Masukkan pilihan Anda: ")

            if pilihan == "1":
                read_perkotaan()
            elif pilihan == "2":
                read_pemukiman()
            elif pilihan == "3":
                read_proyek()
            elif pilihan == "4":
                print("Terima kasih!")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")
        except (EOFError, KeyboardInterrupt):
            print("Program keluar.")
            break

class Login:
    def __init__(self, mycursor):
        self.mycursor = mycursor
        self.users = {}

    def register(self, username, password):
        try:
            if username in self.users:
                raise ValueError("Username sudah ada. Silakan pilih username lain.")
            else:
                self.users[username] = password
                print("Pendaftaran berhasil. Silakan login dengan akun baru Anda.")
        except ValueError as e:
            print(e)

    def login(self, username, password):
        try:
            self.mycursor.execute(f"SELECT * FROM admin WHERE `Nama_Admin` = '{username}' AND `Password_Admin` = '{password}'")
            admin = self.mycursor.fetchone()
            if admin:
                print("Login berhasil.")
                role = admin[4]
                if role == "super admin database":
                    menu_utama_SUPER_ADMIN()
                elif role == "perkotaan_database":
                    menu_utama_perkotaan()
                elif role == "pemukiman_database":
                    menu_utama_pemukiman()
                elif role == "proyek_database":
                    menu_utama_proyek()
                else:
                    print("Role tidak valid.")
            elif username in self.users:
                if self.users[username] == password:
                    menu_user()
                else:
                    raise ValueError("Password pengguna salah. Silakan coba lagi.")
            else:
                raise ValueError("Username tidak ditemukan.")
        except ValueError as e:
            print(e)

login = Login(mycursor)

while True:
    try:
        print("============================================================")
        print("|  Sistem Informasi Perkotaan dan Pemukiman Berkelanjutan  |")
        print("============================================================")
        print("|                      1. Login                            |")
        print("|                      2. Buat Akun Baru                   |")
        print("|                      3. Keluar                           |")
        print("============================================================")
        choice = input_handler("Pilih menu: ")

        if choice == "1":
            username = input_handler("Masukkan username: " )
            password = getpass.getpass("Masukkan password: " )
            login.login(username, password)
            
        elif choice == "2":
            username = input_handler("Masukkan username baru: " )
            password = getpass.getpass("Masukkan password baru: " )
            login.register(username, password)
        elif choice == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")
    except (EOFError, KeyboardInterrupt):
        print("Program keluar.")
        break   
