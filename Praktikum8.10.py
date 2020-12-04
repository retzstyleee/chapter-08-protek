def tampilkan_menu():
    print("Daftar menu :")
    print("-"*50)
    i = 1
    for a,b in buah.items():
        print("[{}] {} (Rp.{} / kg)".format(i,a,b))
        i += 1
def membeli():
    try:
        global harga_total
        tampilkan_menu()
        beli = input("Nama buah yang ingin dibeli : ")
        kg = float(input("Berapa kg ? : "))
        harga = buah.get(beli)
        int(harga)
        print("Harga total untuk {} {} kg adalah Rp.{}".format(beli,kg,harga*kg))
        print("-"*50)
        semua.append(beli)
        kg_total.append(kg)
        harga_total.append(harga*kg)
    except:
        print("Maaf data tidak valid")
def tambah_menu():
    global buah
    buah_tambahan = input("Masukan Nama buah : ").lower()
    harga_tambahan = int(input("Masukan harganya per Kg: "))
    if buah_tambahan in buah:
        print("Buah sudah ada")
    else:
        buah[buah_tambahan] = harga_tambahan
def hapus_menu():
    global buah
    buah_hapus = input("Masukan nama buah : ").lower()
    if buah_hapus in buah:
        buah.pop(buah_hapus)
    else:
        print("Buah memang tidak ada")

#----------------------------------------------------------------------------    

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
semua = []
kg_total = []

while True:
    try:
        harga_total = []
        tampilkan_menu()
        
        print("Selamat datang, ada yang bisa saya bantu ?")
        menu = int(input("[1] Tambah menu \n[2] Hapus Menu \n[3] Beli \n[4] Exit \nInput : "))
        if menu == 1:
            tambah_menu()
        elif menu == 2:
            hapus_menu()
        elif menu == 3:
            while True:
                membeli()
                pesan = input("Beli lagi ? (y/n)")
                if pesan == "y":
                    continue
                else:
                    break
        elif menu == 4:
            print("Terima kasih")
            break
        else:
            print("Something wrong")
            break

        if menu == 1:
            pass
        elif menu == 2:
            pass
        elif menu == 3:
            print("Anda membeli :")
            for i in range(len(semua)):
                print("[{}] {} sebanyak {} kg harga Rp.{}".format(i+1,semua[i],kg_total[i],harga_total[i]))
            print("Total harga yang harus dibayar adalah Rp.{}".format(sum(harga_total)))
        elif menu == 4:
            print("Terima kasih")
        else:
            break
    except:
        print("Something Wrong")