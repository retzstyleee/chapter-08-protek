myData = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print("-----------------------------------")
print("PROGRAM MENGHITUNG TOTAL HARGA BUAH")
print("-----------------------------------")
brp = []
total = []
while True:
	menu = input("\nMenu :\nA. Tambah data buah\nB. Beli buah\n\nPilihan menu : ")
	if menu == 'A' or menu == 'a':
		tabuh = str(input("\nMasukkan nama buah	: "))
		if (tabuh in myData):
			print("Buah sudah ada dalam data")
			continue
		try:
			habuh = int(input("Masukkan harga satuan	: "))
			myData.update({tabuh:habuh})
			print("\nData buah :")
			for x, y in myData.items():
				print("\n- ", x, "( Harga Rp" + str(y) + ")")
				continue
		except ValueError:
			print("Input tidak valid")
			continue
	elif menu == 'B' or menu == 'b':
		while True:
			buah = input("\nBuah yang akan dibeli		: ")
			if (buah in myData):
				try:
					juml = int(input("Berapa kg yang akan dibeli?	: "))
				except ValueError:
					print("Input tidak valid")
					continue
				lagi = input("\nBeli buah yang lain? (y/n)	: ")
				if lagi == 'y':
					total = (myData[buah] * juml)
					brp.append(total)
					continue
				elif lagi == 'n':
					total = (myData[buah] * juml)
					brp.append(total)
					print("-----------------------------------------")
					print("Total harga			: ", sum(brp))
					break
				else:
					print("Input tidak valid")
					continue
			else:
				print("Buah tidak tersedia")
				continue
	else:
		print("Input tidak valid")
		continue
	break