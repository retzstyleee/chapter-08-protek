Mhs = [
    {'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
    {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
    {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
    {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}
    ]

Nilai_Akhir_semua = []

def get_nilai_akhir():
    for orang in Mhs:
        nilai_akhir_orang = (orang.get('mid') + 2 * orang.get('uas')) // 3
        Nilai_Akhir_semua.append(nilai_akhir_orang)
        orang["akhir"] = nilai_akhir_orang
def get_rata_rata_semua():
    print("Rata - rata semuanya adalah ",sum(Nilai_Akhir_semua)/len(Nilai_Akhir_semua))
def get_nilai_tertinggi():
    tertinggi = max(Nilai_Akhir_semua)
    for orang in Mhs:
        if tertinggi == orang.get('akhir'):
            print("Orang terbaik adalah {} (NIM : {}) dengan nilai akhir {}".format(orang.get('nama'),orang.get('nim'),tertinggi))
def get_nilai_terendah():
    terendah = min(Nilai_Akhir_semua)
    for orang in Mhs:
        if terendah == orang.get('akhir'):
            print("Orang terendah adalah {} (NIM : {}) dengan nilai akhir {}".format(orang.get('nama'),orang.get('nim'),terendah))

get_nilai_akhir()
get_rata_rata_semua()
get_nilai_tertinggi()
get_nilai_terendah()