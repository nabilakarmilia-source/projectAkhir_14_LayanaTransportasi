from datetime import datetime

pengurus = "admin123"
pengguna = []
diskon = {}
tiket = []
terminal = {
    "pamekasan": 50000,
    "surabaya": 100000,
    "gresik": 125000,
    "mojokerto": 150000,
    "sidoarjo": 200000
}
bis ={
    "yudistira": datetime.strptime("07:00", "%H:%M").time(),
    "bima": datetime.strptime("09:00", "%H:%M").time(),
    "arjuna": datetime.strptime("12:00", "%H:%M").time(),
    "nakula": datetime.strptime("15:00", "%H:%M").time(),
    "sadewa": datetime.strptime("18:00", "%H:%M").time()
}
name = None

def registrasi():
    print("\n=== REGISTRASI ===")
    username = input("masukkan username baru: ").lower()
    if username in pengguna:
        print("username sudah terdaftar!")
        return
    pengguna.append(username)
    print("username baru telah ditambahkan!")

def login():
    global name
    print("\n=== LOGIN ===")
    name = input("masukkan username: ").lower()

    if name == pengurus:
        print("login admin berhasil!")
        return "admin"

    if name in pengguna:
        print("login pengguna berhasil!")
        return "user"

    print("username tidak terdaftar!")
    return None

def tambah_tujuan():
    print("\n=== TAMBAH TUJUAN ===")
    tujuan = input("masukkan tujuan baru: ").lower()
    if tujuan in terminal:
        print("tujuan sudah ada!")
        return
    harga = input("masukkan harga: ")

    terminal[tujuan] = harga
    print(f"tujuan {tujuan} berhasil ditambahkan!")


def hapus_tujuan():
    print("\n=== HAPUS TUJUAN ===")
    hapus = input("masukkan tujuan yang akan dihapus: ").lower()
    if hapus not in terminal:
        print("tujuan tidak ditemukan!")
        return
    
    del terminal[hapus]
    print(f"tujuan {hapus} berhasil dihapus!")

def tambah_bis():
    print("\n=== TAMBAH BIS ===")
    nama = input("masukkan nama bis: ").lower()
    jam = input("masukkan jam keberangkatan (hh:mm): ")

    bis[nama] = datetime.strptime(jam, "%H:%M").time()
    print(f"bis {nama} berhasil ditambahkan!")

def hapus_bis():
    print("\n=== HAPUS BIS ===")
    hapus = input("masukkan nama bis yang akan dihapus: ").lower()
    if hapus not in bis:
        print("bis tidak ditemukan!")
        return
    
    del bis[hapus]
    print(f"bis {hapus} berhasil dihapus!")

def tambah_kupon():
    print("\n=== TAMBAH KUPON ===")
    kupon = input("masukkan kode kupon: ")
    
    try:
        persen = int(input("diskon berapa (%): "))
    except ValueError:
        print("diskon harus angka!")
        return

    diskon[kupon] = persen
    print("kupon berhasil ditambahkan!")

def hapus_kupon():
    print("\n=== HAPUS KUPON ===")
    hapus = input("masukkan kupon yang akan dihapus: ")
    if hapus not in diskon:
        print("kupon  tidak ditemukan!")
        return
    
    del diskon[hapus]
    print("kupon berhasil ditambahkan!")

def jadwal():
    print("\n=== JADWAL KEBERANGKATAN BIS BANGKALAN ===")
    waktu_sekarang = datetime.now().time()

    for bus, jam in bis.items():
        if waktu_sekarang >= jam:
            print(f"bis {bus} sudah berangkat (jadwal {jam}).")
        else:
            print(f"bis {bus} belum berangkat (jadwal {jam}).")

def lihat_terminal():
    print("\n=== SELURUH TUJUAN ===")
    for i, tujuan in enumerate(terminal.items(), start=1):
        print(f"tujuan {tujuan}, estimasi waktu {i} jam")

def lihat_tiket():
    print("\n=== SEMUA TIKET ===")
    if not tiket:
        print("belum ada pemesanan tiket!")
    else:
        for t in tiket:
            print(f"nama   : {t['nama']}")
            print(f"tujuan : {t['tujuan']}")
            print(f"bis    : {t['nama_bis']}")
            print(f"harga  : {t['harga']:,}\n")

def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("0. tambah tujuan baru")
        print("1. hapus tujuan")
        print("2. tambah bis baru")
        print("3. hapus bis")
        print("4. tambah kupon diskon")
        print("5. hapus kupon diskon")
        print("6. lihat terminal tujuan")
        print("7. lihat jadwal bis")
        print("8. lihat semua tiket")
        print("9. logout")
        pilih = input("pilih menu: ")

        if pilih == "o":
            tambah_tujuan()
        elif pilih == "1":
            hapus_tujuan()
        elif pilih == "2":
            tambah_bis()
        elif pilih == "3":
            hapus_bis()
        elif pilih == "4":
            tambah_kupon()
        elif pilih == "5":
            hapus_kupon()
        elif pilih == "6":
            lihat_terminal()
        elif pilih == "7":
            jadwal()
        elif pilih == "8":
            lihat_tiket()
        elif pilih == "9":
            break
        else:
            print("pilihan tidak valid!")

def pesan_tiket():
    global name
    print("\n=== PEMESANAN TIKET BIS BANGKALAN ===")

    lihat_terminal()
    tujuan = input("masukkan tujuan anda: ").lower()
    if tujuan not in terminal:
        print("tujuan tidak tersedia!")
        return

    jadwal()
    pilih = input("pilih bis mana: ").lower()
    if pilih not in bis:
        print("bis tidak tersedia!")
        return

    kupon = input("masukkan kupon (jika ada): ")

    harga = terminal[tujuan]

    if kupon in diskon:
        dskn = diskon[kupon]
        total = harga - (harga * dskn / 100)
    else:
        total = harga

    tiket.append({
        "nama": name,
        "tujuan": tujuan,
        "nama_bis": pilih,
        "harga": int(total)
    })

    print("tiket berhasil dipesan!")

def tiket_saya():
    global name
    print("\n=== TIKET ANDA ===")
    ditemukan = False
    for t in tiket:
        if t['nama'] == name:
            print(f"nama   : {t['nama']}")
            print(f"tujuan : {t['tujuan']}")
            print(f"bis    : {t['nama_bis']}")
            print(f"harga  : {t['harga']:,}")
            print()
            ditemukan = True
    
    if not ditemukan:
        print("Anda belum memiliki tiket.")
 
def menu_pengguna():
    while True:
        print("\n=== MENU PENGGUNA ===")
        print("1. pesan tiket")
        print("2. lihat terminal tujuan")
        print("3. lihat jadwal bis")
        print("4. lihat tiket saya")
        print("5. logout")
        pilih = input("pilih menu: ")

        if pilih == "1":
            pesan_tiket()
        elif pilih == "2":
            lihat_terminal()
        elif pilih == "3":
            jadwal()
        elif pilih == "4":
            tiket_saya()
        elif pilih == "5":
            break
        else:
            print("pilihan tidak valid!")

while True:
    print("\n==== LAYANAN TRANSPORTASI BIS BANGKALAN ====")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu: ")

    if pilih == "1":
        user = login()
        if user == "admin":
            menu_admin()
        elif user == "user":
            menu_pengguna()
    elif pilih == "2":
        registrasi()
    elif pilih == "3":
        print("terima kasih, semoga hari anda menyenangkan")
        break
    else:
        print("pilihan tidak valid!")