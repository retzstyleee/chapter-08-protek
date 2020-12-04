def tampilkan_menu():
    print("Ini daftar menu nya Tuan..")
    for i in sayuran:
        print("[{}] {}".format((sayuran.index(i)+1),i))

def tambah_menu():
    global sayuran
    tambahan = input("Masukan menu yang ingin ditambahkan : ")
    print("Oke")
    sayuran.append(tambahan)
def hapus_menu():
    global sayuran
    hapus = input("Masukan menu yang ingin dihapus : ")
    print("Oke")
    try:
        sayuran.remove(hapus)
    except :
        print("Maaf, tidak ditemukan dalam menu")

sayuran = ["Bayam","Kangkung","Wortel","Selada"]

while True:
    print("-"*50)    
    tampilkan_menu()

    print("Ada yang bisa saya bantu ?")
    print("[1] Tambah Menu \n[2] Hapus Menu \n[3] Tidak, Terima kasih")

    pilihan = input("Pilihan sesuai nomor : ")
    if pilihan == "1":
        tambah_menu()
    elif pilihan == "2":
        hapus_menu()
    elif pilihan == "3":
        print("Oke :)")
        break
    else:
        print("Maaf tuan, saya tidak memahami pilihan anda")