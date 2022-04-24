harga_tiket_kendaraan = [
    [1, "Sepeda", "I", 22000],
    [2, "Motor", "II", 51000],
    [3, "Motor Roda 3", "III", 114000],
    [4, "Avanza dan Sejenisnya", "IV A", 374000],
    [5, "Pick Up", "IV B", 326000],
    [6, "Bus Sedang < 7 meter", "V A", 774000],
    [7, "Colt Diesel", "V B", 645000],
    [8, "Bus Besar > 7 meter", "VI A", 1301000],
    [9, "Truk Besar", "VI B", 998000],
    [10, "Tronton", "VII", 1406000],
    [11, "Trailer", "VIII", 2080000],
    [12, "Trailer > 16 meter", "IX", 3251000]
]
kata = "HARGA TIKET KENDARAAN"

print("")
print(" %s " %(kata).center(60))
print("")
print("="*60)
print("{:^5}{:^25}{:^15}{:^20}" .format("No","Jenis Kendaraan","Golongan", "Harga"))
print("="*60)
for i in range(12):
    harga1 = harga_tiket_kendaraan[i][3]
    harga2 = f"{harga1:,}"
    harga3 = "Rp. " + harga2
    print("{:^5}{:<25}{:^10}{:>20}" .format(harga_tiket_kendaraan[i][0],
    harga_tiket_kendaraan[i][1],harga_tiket_kendaraan[i][2], harga3))
print("="*60)
print("")