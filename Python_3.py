# Input jumlah bangun datar (n)
n = int(input("Masukkan jumlah bangun datar: "))

# Inisialisasi daftar untuk menyimpan luas bangun datar
luas_bangun_datar = []

# Meminta input dan menghitung luas untuk masing-masing bangun datar
for i in range(n):
    jenis_bangun = input("Masukkan jenis bangun datar (persegi/persegi panjang/segitiga/lingkaran/trapesium): ")

    if jenis_bangun == 'persegi':
        sisi = float(input("Masukkan panjang sisi: "))
        bangun = Persegi(sisi)
    elif jenis_bangun == 'persegi panjang':
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        bangun = PersegiPanjang(panjang, lebar)
    elif jenis_bangun == 'segitiga':
        alas = float(input("Masukkan alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        bangun = Segitiga(alas, tinggi)
    elif jenis_bangun == 'lingkaran':
        radius = float(input("Masukkan radius: "))
        bangun = Lingkaran(radius)
    elif jenis_bangun == 'trapesium':
        sisi1 = float(input("Masukkan panjang sisi pertama: "))
        sisi2 = float(input("Masukkan panjang sisi kedua: "))
        tinggi = float(input("Masukkan tinggi: "))
        bangun = Trapesium(sisi1, sisi2, tinggi)
    else:
        print("Jenis bangun datar tidak valid")
        continue

    luas = bangun.hitung_luas()
    luas_bangun_datar.append((jenis_bangun, luas))

# Mengurutkan daftar luas bangun datar dari terkecil hingga terbesar
luas_bangun_datar.sort(key=lambda x: x[1])

# Menampilkan hasil
print("\nLuas Bangun Datar:")
total_luas = 0
for jenis, luas in luas_bangun_datar:
    print(f"{jenis}: {luas}")
    total_luas += luas

print("\nTotal Luas Bangun Datar:", total_luas)