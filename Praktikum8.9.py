def tampilkan_menu():
    print("Daftar menu :")
    print("-"*50)
    for a,b in buah.items():
        print("{} (Rp.{} / kg)".format(a,b))
def membeli():
    try:
        harga = buah.get(beli)
        int(harga)
        print("Harga total untuk {} {} kg adalah Rp.{}".format(beli,kg,harga*kg))
        print("-"*50)
    except:
        print("Maaf data tidak valid")

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

tampilkan_menu()

beli = input("Nama buah yang ingin dibeli : ")
kg = float(input("Berapa kg ? : "))

membeli()