def termahal(buah):
    harga = max(buah.values())
    for a,b in buah.items():
        if b == harga:
            print("Barang dengan harga tertinggi adalah {}".format(a))
def rata(buah):
    a = 0
    for i in buah.values():
        a += i
    print("Rata rata seluruh harga pada menu adalah Rp.{}".format(a/len(buah)))

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
termahal(buah)
rata(buah)