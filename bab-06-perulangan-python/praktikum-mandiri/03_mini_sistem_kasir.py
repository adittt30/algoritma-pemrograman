x = 2
z = 12
total_belanja = 0
jumlah_transaksi = 0
persen_diskon = 5 + x
batas_diskon = 50000 + z * 1000
print("X =", x, "Z =", z, "| Diskon: ", persen_diskon, "%", "| Batas: Rp",batas_diskon)
print("1. Nasi Goreng - Rp12000")
print("2. Mie Goreng - Rp10000")
print("3. Es Teh - Rp3000")
print("4. Es Jeruk - Rp5000")
print("0. Selesai")

while True:
    pilihan = int(input("Pilih menu: "))
    if pilihan == 0:
        break
    if pilihan == 1:
        harga = 12000
    elif pilihan == 2:
        harga = 10000
    elif pilihan == 3:
        harga = 3000
    elif pilihan == 4:
        harga = 5000
    else:
        print("Pilihan menu tidak valid.")
        continue
    jumlah = int(input("Jumlah pembelian: "))
    if jumlah < 1:
        print("Jumlah pembelian minimal 1.")
        continue

    subtotal = harga * jumlah
    total_belanja += subtotal
    jumlah_transaksi += 1
    print("Subtotal: Rp", subtotal)

if total_belanja >= batas_diskon:
    diskon = total_belanja * persen_diskon // 100
else:
    diskon = 0

total_bayar = total_belanja - diskon
print("Jumlah transaksi: ", jumlah_transaksi)
print("Total sebelum diskon: Rp", total_belanja)
print("Diskon: Rp", diskon)
print("Total bayar: Rp", total_bayar)
print("Pesanan selesai.")