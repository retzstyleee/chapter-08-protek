def kuadrat(bil):
    for i in range(len(bil)):
        bil[i] **= 2
    print(bil)

bil = [1,2,3,4,5]
kuadrat(bil)