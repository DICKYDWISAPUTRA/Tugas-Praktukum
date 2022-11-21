#GAME TEBAK ANGKA
import random
angka_tersembunyi = random.randint(1, 100)
print ("="*40)
print("Selamat datang di Game Tebak Angka")
print ("="*40)
print("\n")
print ("angka sudah menentukan angka yang harus ditebak, masukan angka tebakan anda :")
batas_percobaan = 8
for percobaan in range(batas_percobaan) :
    jawaban = int(input(f'\n[Percobaan ke {percobaan + 1}] Masukkan angka: '))
    if jawaban == angka_tersembunyi :
        print ("Selamat Kamu benar, Angka rahasianya adalah =", angka_tersembunyi)
        break
    else :
        if jawaban < angka_tersembunyi :
            print ("Angka tebakan anda terlalu kecil silahkan coba kembali")
        if jawaban > angka_tersembunyi :
            print ("Angka tebakan anda terlalu besar silahkan coba kembali")
else : 
    print ("\n")
    print ("Kesempatan anda untuk menebak sudah habis, kamu sudah salah menebak sebanyak " + str(batas_percobaan) + "!!")