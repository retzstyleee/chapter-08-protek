def sortStringByChar(myData):
    myData.sort(key=len,reverse=True)
    return myData

myData = ["Duku","Duren","Manggis","Semangka","Kelengkeng","Naga"]
print(sortStringByChar(myData))