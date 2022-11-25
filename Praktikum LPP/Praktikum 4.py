import random

#Daftar ini memberikan gambaran tentang waktu acara.
Kalimat_starter = random.randint(1, 3)
if Kalimat_starter == 1 :
    kalimat_1 = ("Pada hari minggu, ")
if Kalimat_starter == 2 :
    kalimat_1 = ("Pada hari sabtu, ")
if Kalimat_starter == 3 :
    kalimat_1 = ("Pada hari jumat, ")

#Daftar ini menceritakan tentang karakter utama dari cerita ini.
karakter = random.randint(1, 3)
if karakter == 1 :
    kalimat_2 = ("jisoo pergi ke bandara ")
if karakter == 2 :
    kalimat_2 = ("jisoo pergi ke bali ")
if karakter == 3 :
    kalimat_2 = ("jisoo pergi ke korea ")

#Daftar ini menentukan hari yang tepat di mana beberapa insiden telah terjadi.
waktu = random.randint(1, 3)
if waktu == 1 :
    kalimat_3 = ("jisoo berangkat pada pukul 6 pagi ")
if waktu == 2 :
    kalimat_3 = ("jisoo berangkat pada pukul 7 sore ")
if waktu == 3 :
    kalimat_3 = ("jisoo berangkat pada pukul 8 malam ")

#Daftar ini mendefinisikan plot cerita.
story_plot = random.randint(1, 3)
if story_plot == 1 :
    kalimat_4 = ("Semuanya berjalan dengan lancar suatu ketika terdapat kejadian yang membuatnya terkejut, ")
if story_plot == 2 :
    kalimat_4 = ("karena ia sedang tidak sibuk, ")
if story_plot == 3 :
    kalimat_4 = ("karena jisoo memiliki pekerjaan, ")

#Daftar ini mendefinisikan tempat di mana insiden itu terjadi.
tempat = random.randint(1, 3)
if tempat == 1 :
    kalimat_5 = ("Di depan gerbang 1 bandara ada seseorang penumpang mengalami pertikaian dengan petugas bandara, ")
if tempat == 2 :
    kalimat_5 = ("Di depan gerbang 2 bandara ada seseorang penumpang mengalami pertikaian dengan petugas bandara, ")
if tempat == 3 :
    kalimat_5 = ("Di depan gerbang 3 bandara ada seseorang penumpang mengalami pertikaian dengan petugas bandara, ")

#Daftar ini mendefinisikan karakter kedua dari cerita.
second_character = random.randint(1, 3)
if second_character == 1 :
    kalimat_6 = ("Petugas dan penumpang itu bertikai karena pesawat terlambat hingga 6 jam ")
if second_character == 2 :
    kalimat_6 = ("Petugas dan penumpang itu bertikai karena pesawat terlambat hingga 7 jam ")
if second_character == 3 :
    kalimat_6 = ("Petugas dan penumpang itu bertikai karena pesawat terlambat hingga 8 jam ")

#Daftar ini mendefinisikan usia karakter kedua.
usia = random.randint(1, 3)
if usia == 1 :
    kalimat_7 = ("Mereka terlihat berusia sekitar 25 tahun-an ")
if usia == 2 :
    kalimat_7 = ("Mereka terlihat berusia sekitar 35 tahun-an ")
if usia == 3 :
    kalimat_7 = ("Mereka terlihat berusia sekitar 45 tahun-an ")

#Daftar ini menceritakan tentang pekerjaan yang dilakukan karakter kedua.
pekerjaan = random.randint(1, 3)
if pekerjaan == 1 :
    kalimat_8 = ("petugas itu tidak henti-hentinya mengeluarkan argumen.")
if pekerjaan == 2 :
    kalimat_8 = ("petugas itu tidak henti-hentinya mengeluarkan argumen dan bersih keras ")
if pekerjaan == 3 :
    kalimat_8 = ("petugas itu tidak henti-hentinya mengeluarkan argumen ")

print (kalimat_1, kalimat_2, kalimat_3, kalimat_4, kalimat_5, kalimat_6, kalimat_7, kalimat_8)
