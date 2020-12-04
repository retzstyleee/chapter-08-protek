def termahal(buah):
    harga = max(buah.values())
    for a,b in buah.items():
        if b == harga:
            print(a)

buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
termahal(buah)