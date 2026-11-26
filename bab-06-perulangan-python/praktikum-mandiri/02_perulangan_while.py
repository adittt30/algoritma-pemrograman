x = 2
angka = 1
jumlah_tampil = 0
angka_lewati = x + 1
angka_berhenti = x + 10
print("X =", x)
print("Angka dilewati: ", angka_lewati)
print("Angka berhenti: ", angka_berhenti)

while angka <= 100:
    if angka == angka_berhenti:
      break
    if angka == angka_lewati:
       angka += 1
       continue
    print(angka)
    jumlah_tampil += 1
    angka += 1

print("Jumlah bilangan:", jumlah_tampil)
print("Program selesai.")