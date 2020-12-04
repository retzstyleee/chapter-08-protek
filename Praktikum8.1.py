try:
    jumlah = int(input("Jumlah : "))
    data = []
    for i in range(jumlah):
        data.append(int(input("Data ke {} : ".format(i+1))))
    data.sort(reverse=True)
    print(data)
except:
    print("Input tidak Valid")