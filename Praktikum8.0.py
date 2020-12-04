a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]

a.insert(3,10)
b.insert(2,15)
print(a,"\n",b)
print("-"*50)

a.append(4)
b.append(8)
print(a,"\n",b)
print("-"*50)

a.sort()
b.sort()
print(a,"\n",b)
print("-"*50)

c = a[0:8]
d = b[2:10]
print(c,"\n",d)
print(len(c),len(d))
print("-"*50)

e = c.copy()
for m in range(len(d)):
    e[m] += d[m]
print(e)
print("-"*50)

e = tuple(e)
print(e)
print(type(e))
print("Nilai Min : ",min(e))
print("Nilai Max : ",max(e))
print("Jumlah total : ",sum(e))
print("-"*50)

mystring = "Python adalah bahasa pemrograman yang menyenangkan"
f = set(mystring)
print("Total ada {} karakter".format(len(f)))
f = list(f)
f.sort()
print(f)