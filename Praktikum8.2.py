def dataStat(x):
    list_x = ["a","b","c"]
    list_x[0] = sum(x)/len(x)
    list_x[1] = max(x)
    list_x[2] = min(x)
    return list_x

try:
    jumlah = int(input("Jumlah : "))
    data = []
    for i in range(jumlah):
        data.append(int(input("Data ke {} : ".format(i+1))))
    print(dataStat(data))
except:
    print("Input tidak Valid")