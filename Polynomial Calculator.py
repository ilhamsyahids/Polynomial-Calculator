print("==========================")
print("[Program Polinomial]\n")
print("Deskripsi :")
print("Program ini dibuat untuk mencetak dan mengoperasikan dua polinomial dari suatu masukkan")
print("Program ini hanya bisa menerima input polinomial dengan suku maksimal 99 dan minimal 0\n")
print("Petunjuk input :")
print("Silahkan masukkan beberapa input dengan format <suku,koefisien>\n")
print("Sebagai contoh :\n\nInput :\n1,3\n2,4\n\nOutput :\n4x^2+3x^1\n")
print("Keterangan :")
print("Akhiri masukkan dengan mengetik suku menjadi -999")
print("suku yang melebih batas atau kurang dari batas akan diabaikan")
print("suku yang lebih dari 1 kali diinputnya, maka akan diambil input terakhir\n")
print("==========================")

def buat_polinom(a): # fungsi untuk membuat polinom
    				 # a sebagai parameter adalah list dari koefisen-koefisien polinom
    hasil = "" 
    for i in range(len(a)-1,-1,-1):
        if a[i] == 0:
            continue
        if a[i] > 0:
            hasil += "+"
        if i == 1:
        	if str(a[i]) == "1":
        		hasil += "x"
        	else:
        		hasil += str(a[i])+"x"
        elif i == 0:
        	hasil += str(a[i])
        else:
        	hasil += str(a[i])+"x^"+str(i)
    if len(hasil) == 0:
        return "0"
    elif hasil[0] == "+":
        return hasil[1:]
    else:
        return hasil

def jumlah(a,b):
    c = [0 for i in range(100)]
    for i in range(100):
        c[i] = a[i]+b[i]
    return buat_polinom(c)

def kurang(a,b):
    c = [0 for i in range(100)]
    for i in range(100):
        c[i] = a[i]-b[i]
    return buat_polinom(c)

def turunan(a):
    c = [0 for i in range(100)]
    for i in range(1,100):
        c[i-1] = a[i]*i
    return buat_polinom(c)

polinom_1 = [0 for i in range(100)]

print("Masukkan beberapa input untuk polinomial pertama :")

while True:
    a = input("Masukkan input <suku,koefisien> : ").split(",")
    if a[0] == "-999":
        break
    elif int(a[0]) > 100 or int(a[0]) < 0:
        print("Input salah, silahkan masukkan input lagi")
        continue
    polinom_1[int(a[0])] = int(a[1])

polinom_pertama = buat_polinom(polinom_1)

print("\nPolinomal pertama berhasil disimpan!\n")

print("Masukkan beberapa input untuk polinom kedua :")
polinom_2 = [0 for i in range(100)]

while True:
    a = input("Masukkan input <suku,koefisien> : ").split(",")
    if a[0] == "-999":
        break
    elif int(a[0]) > 100 or int(a[0]) < 0:
        continue
    polinom_2[int(a[0])] = int(a[1])
polinom_kedua = buat_polinom(polinom_2)

print("\nPolinomal kedua berhasil disimpan!\n")
print("Sekarang Anda bisa memilih menu\n")

while True:
    print("Pilihan Menu")
    print("Menu 1 : Mencetak polinomial pertama dan polinomial kedua")
    print("Menu 2 : Menjumlahkan polinomial pertama dengan polinomial kedua")
    print("Menu 3 : Mengurangi polinomial pertama dengan polinomial kedua")
    print("Menu 4 : Mencetak hasil turunan pertama dari polinomial pertama dan polinomial kedua")
    print("Menu 0 : Mengakhiri program")
    menu = int(input("Pilih menu yang diinginkan : "))
    if menu == 0:
        print()
        print("Terima kasih sudah menggunakan program ini :)")
        print()
        break
    elif menu == 1:
        print()
        print("P1(x) =",polinom_pertama)
        print("P2(x) =",polinom_kedua)
        print()
    elif menu == 2:
        print()
        print("P3(x) :",jumlah(polinom_1,polinom_2))
        print()
    elif menu == 3:
        print()
        print("P3(x) =",kurang(polinom_1,polinom_2))
        print()
    elif menu == 4:
        print()
        print("P1'(x) =",turunan(polinom_1))
        print("P2'(x) =",turunan(polinom_2))
        print()