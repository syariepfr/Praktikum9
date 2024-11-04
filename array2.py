#Deklarasi Matriks pertama dan kedua
matriks1 = []
matriks2 = []

#Meminta input untuk matriks pertama
print("Masukan elemen untuk matriks pertama (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukan elemen baris (i+1), kolom (j+1): "))
        baris.append(nilai)
    matriks1.append(baris)

#Meminta input untuk matriks kedua
print("Masukan elemen untuk matriks pertama (3x3):")
for i in range(3):
    baris = []
    for j in range(3):
        nilai = int(input(f"Masukan elemen baris (i+1), kolom (j+1): "))
        baris.append(nilai)
    matriks2.append(baris)

#Meminta input jenis operasi
operasi = input("\nPilih operasi (penjumlahan/pengurangan/perkalian): ").lower()

#Melakukan operasi berdasarkan pilihan
hasil = []
if operasi == 'penjumlahan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks1[i][j] + matriks2[i][j])
        hasil.append(baris)
elif operasi == 'pengurangan':
    for i in range(3):
        baris = []
        for j in range(3):
            baris.append(matriks1[i][j] - matriks2[i][j])
        hasil.append(baris)
elif operasi == 'perkalian':
    for i in range(3):
        baris = []
        for j in range(3):
            nilai = 0
            for k in range(3):
                nilai += matriks1[i][k] * matriks2[k][j]
            baris.append(nilai)
        hasil.append(baris)
else :
    print("Operasi tidka valid.")

#Menampilkan hasil operasi
if hasil:
    print(f"\nHasil {operasi} matriks:")
    for baris in hasil:
        print(baris)