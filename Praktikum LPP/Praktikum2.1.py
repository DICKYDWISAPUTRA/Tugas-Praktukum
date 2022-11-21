# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 18:47:22 2022

@author: dicky
"""

import random
angka_rahasia = random.randint(1, 100)
print('=' * 40)
print('Kami telah memiliki angka, silakan tebak!')
print('=' * 40)
while True:
  jawaban = int(input('\nMasukkan angka: '))

  if jawaban == angka_rahasia:
    print('Selamat, tebakanmu benar!')
    break # berhenti paksa
  else:
    print(
      'Tebakanmu terlalu',
      'kecil' if jawaban < angka_rahasia else 'besar'
    )
    batas_percobaan = 8

for percobaan in range(batas_percobaan):
  jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: '))

  if jawaban == angka_rahasia:
    print('Selamat, tebakanmu benar!')
    break
  else:
    print(
      'Tebakanmu terlalu',
      'kecil' if jawaban < angka_rahasia else 'besar'
    )
else:
  print(f'\nSayang sekali, kamu sudah salah menebak sebanyak {batas_percobaan}x!')