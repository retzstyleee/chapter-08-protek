try:
    jumlah = int(input("Jumlah : "))
    data = []
    for i in range(jumlah):
        data.append(input("Data ke {} : ".format(i+1)))
    data.sort()
    for i in data:
        print("[{}] {} ({} karakter)".format(data.index(i),i,len(i)))
except:
    print("Input tidak Valid")