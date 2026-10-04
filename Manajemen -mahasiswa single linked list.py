# ============================================================
# PROGRAM MANAJEMEN DATA MAHASISWA
# IMPLEMENTASI SINGLE LINKED LIST
# ============================================================

class Node:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    # --------------------------------------------------------
    # MENAMBAH DATA DI AWAL
    # --------------------------------------------------------
    def tambah_awal(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        new_node.next = self.head
        self.head = new_node
        print("Data berhasil ditambahkan di awal.")

    # --------------------------------------------------------
    # MENAMBAH DATA DI AKHIR
    # --------------------------------------------------------
    def tambah_akhir(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)

        if self.head is None:
            self.head = new_node
            print("Data berhasil ditambahkan di akhir.")
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        print("Data berhasil ditambahkan di akhir.")

    # --------------------------------------------------------
    # MENAMBAH DATA DI TENGAH BERDASARKAN URUTAN NIM
    # --------------------------------------------------------
    def tambah_urut_nim(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)

        # Jika list kosong atau NIM lebih kecil dari head
        if self.head is None or nim < self.head.nim:
            new_node.next = self.head
            self.head = new_node
            print("Data berhasil ditambahkan berdasarkan urutan NIM.")
            return

        current = self.head

        while current.next is not None and current.next.nim < nim:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        print("Data berhasil ditambahkan berdasarkan urutan NIM.")

    # --------------------------------------------------------
    # MENGHAPUS DATA BERDASARKAN NIM
    # --------------------------------------------------------
    def hapus_nim(self, nim):
        if self.head is None:
            print("Data mahasiswa masih kosong.")
            return

        # Jika data yang dihapus adalah head
        if self.head.nim == nim:
            self.head = self.head.next
            print("Data dengan NIM", nim, "berhasil dihapus.")
            return

        current = self.head

        while current.next is not None:
            if current.next.nim == nim:
                current.next = current.next.next
                print("Data dengan NIM", nim, "berhasil dihapus.")
                return

            current = current.next

        print("Data dengan NIM", nim, "tidak ditemukan.")

    # --------------------------------------------------------
    # MENCARI DATA BERDASARKAN NIM
    # --------------------------------------------------------
    def cari_nim(self, nim):
        current = self.head

        while current is not None:
            if current.nim == nim:
                print("\nData ditemukan!")
                print("NIM     :", current.nim)
                print("Nama    :", current.nama)
                print("Jurusan :", current.jurusan)
                return

            current = current.next

        print("Data dengan NIM", nim, "tidak ditemukan.")

    # --------------------------------------------------------
    # MENAMPILKAN SEMUA DATA
    # --------------------------------------------------------
    def tampilkan_semua(self):
        if self.head is None:
            print("Data mahasiswa masih kosong.")
            return

        current = self.head
        nomor = 1

        print("\n==============================================================")
        print("                 DATA MAHASISWA")
        print("==============================================================")

        while current is not None:
            print("Data ke-", nomor)
            print("NIM     :", current.nim)
            print("Nama    :", current.nama)
            print("Jurusan :", current.jurusan)
            print("--------------------------------------------------------------")

            current = current.next
            nomor += 1


# ============================================================
# DATA AWAL MAHASISWA
# ============================================================

data_mahasiswa = [
    ("257111075", "Imelda Lawanggomang", "Pendidikan Informatika"),
    ("257111076", "Romanterius Karmoi", "Pendidikan Informatika"),
    ("257111077", "Ayedija Doku Bani", "Pendidikan Informatika"),
    ("257111057", "Rafika Lanan Soge", "Pendidikan Informatika"),
    ("257111066", "Verselia Suherdis", "Pendidikan Informatika"),
    ("257111082", "Natiab Tefbana", "Pendidikan Informatika"),
    ("257111065", "Verselia Bouk", "Pendidikan Informatika"),
    ("257111078", "Christyvora R. L. Rendo", "Pendidikan Informatika"),
    ("257111059", "Elfi S. Amheka", "Pendidikan Informatika"),
    ("257111064", "Thomas N. Labina", "Pendidikan Informatika"),
    ("257111063", "Andrew G. G. Assan", "Pendidikan Informatika"),
    ("257111072", "Kura Daku", "Pendidikan Informatika"),
    ("257111071", "Tiara Calysta Tadji Lena", "Pendidikan Informatika"),
    ("257111069", "Noldi Fernandes Bana", "Pendidikan Informatika"),
    ("257111074", "Patrik Maki", "Pendidikan Informatika"),
    ("257111067", "Thimotia Benu", "Pendidikan Informatika"),
    ("257111083", "Veronika Hendrigues", "Pendidikan Informatika")
]


# ============================================================
# PROGRAM UTAMA
# ============================================================

linked_list = SingleLinkedList()

# Memasukkan data awal secara berurutan berdasarkan NIM
for nim, nama, jurusan in data_mahasiswa:
    linked_list.tambah_urut_nim(nim, nama, jurusan)


while True:
    print("\n==============================================================")
    print("       PROGRAM MANAJEMEN DATA MAHASISWA")
    print("             SINGLE LINKED LIST")
    print("==============================================================")
    print("1. Tambah data di awal")
    print("2. Tambah data berdasarkan urutan NIM")
    print("3. Tambah data di akhir")
    print("4. Hapus data berdasarkan NIM")
    print("5. Cari data berdasarkan NIM")
    print("6. Tampilkan semua data")
    print("7. Keluar")
    print("==============================================================")

    pilihan = input("Pilih menu [1-7]: ")

    if pilihan == "1":
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan nama: ")
        jurusan = input("Masukkan jurusan: ")

        linked_list.tambah_awal(nim, nama, jurusan)

    elif pilihan == "2":
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan nama: ")
        jurusan = input("Masukkan jurusan: ")

        linked_list.tambah_urut_nim(nim, nama, jurusan)

    elif pilihan == "3":
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan nama: ")
        jurusan = input("Masukkan jurusan: ")

        linked_list.tambah_akhir(nim, nama, jurusan)

    elif pilihan == "4":
        nim = input("Masukkan NIM yang ingin dihapus: ")
        linked_list.hapus_nim(nim)

    elif pilihan == "5":
        nim = input("Masukkan NIM yang ingin dicari: ")
        linked_list.cari_nim(nim)

    elif pilihan == "6":
        linked_list.tampilkan_semua()

    elif pilihan == "7":
        print("Program selesai. Terima kasih.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-7.")