#UTS-02

#Judul
print('###----- TOKO ELEKTRONIK CAHAYA BINTANG -----###')

#Data-Data
hargakotorKipasAngin = 1000000
hargakotorTV = 2000000
hargakotorMesinCuci = 3000000
hargakotorAC = 4000000
hargakotorKulkas = 5000000

namapelanggan =input("Masukkan Nama Pelanggan :")
namabarang =input("Masukkan Produk Pilihan : ")
pembelian =input("Masukkan Jumlah Barang :")
pembelianasli =int(pembelian)

#Berhitung
if namabarang =='Kipas Angin':
    pembelianKipasAngin = hargakotorKipasAngin * pembelianasli
    diskonKipasAngin = pembelianKipasAngin * (5/100)
    PPNKipasAngin = (pembelianKipasAngin - diskonKipasAngin) *  (10/100)
    hargabersihKipasAngin = pembelianKipasAngin - diskonKipasAngin + PPNKipasAngin
    print("### NOTA PEMBELIAN BARANG ###")
    print("Nama Pelanggan :",namapelanggan)
    print("Produk Pilihan : Kipas Angin")
    print("Jumlah Beli :",pembelian)
    print("Harga Kotor :",hargakotorKipasAngin)
    print("Diskon 5% :",diskonKipasAngin)
    print("PPN 10% :",PPNKipasAngin)
    print("Harga Bersih :",hargabersihKipasAngin)

elif namabarang =='TV':
    pembelianTV = hargakotorTV * pembelianasli
    diskonTV = pembelianTV * (5/100)
    PPNTV = (pembelianTV - diskonTV) *  (10/100)
    hargabersihTV = pembelianTV - diskonTV + PPNTV
    print("### NOTA PEMBELIAN BARANG ###")
    print("Nama Pelanggan :",namapelanggan)
    print("Produk Pilihan : TV")
    print("Jumlah Beli :",pembelian)
    print("Harga Kotor :",hargakotorTV)
    print("Diskon 5% :",diskonTV)
    print("PPN 10% :",PPNTV)
    print("Harga Bersih :",hargabersihTV)

elif namabarang =='Mesin Cuci':
    pembelianMesinCuci = hargakotorMesinCuci * pembelianasli
    diskonMesinCuci = pembelianMesinCuci * (5/100)
    PPNMesinCuci = (pembelianMesinCuci - diskonMesinCuci) * (10/100)
    hargabersihMesinCuci = pembelianMesinCuci - diskonMesinCuci + PPNMesinCuci
    print("### NOTA PEMBELIAN BARANG ###")
    print("Nama Pelanggan :",namapelanggan)
    print("Produk Pilihan : Mesin Cuci")
    print("Jumlah Beli :",pembelian)
    print("Harga Kotor :",hargakotorMesinCuci)
    print("Diskon 5% :",diskonMesinCuci)
    print("PPN 10% :",PPNMesinCuci)
    print("Harga Bersih :",hargabersihMesinCuci)

elif namabarang =='AC':
    if pembelianasli > 2:
     pembelianAC = hargakotorAC * pembelianasli
     diskonAC = pembelianAC * (10/100)
     PPNAC = (pembelianAC - diskonAC) * (10/100)
     hargabersihAC = pembelianAC - diskonAC + PPNAC
     print("### NOTA PEMBELIAN BARANG ###")
     print("Nama Pelanggan :",namapelanggan)
     print("Produk Pilihan : AC")
     print("Jumlah Beli :",pembelian)
     print("Harga Kotor :",hargakotorAC)
     print("Diskon 5% :",diskonAC)
     print("PPN 10% :",PPNAC)
     print("Harga Bersih :",hargabersihAC)
    else:
         pembelianAC = hargakotorAC * pembelianasli
         diskonAC = pembelianAC * (5/100)
         PPNAC = (pembelianAC - diskonAC) * (10/100)
         hargabersihAC = pembelianAC - diskonAC + PPNAC
         print("== NOTA PEMBELIAN BARANG ==\n")
         print("Nama Pembeli :",namapelanggan)
         print("Produk Pilihan : AC")
         print("Jumlah Beli : ",pembelian)
         print("Harga Kotor : ",hargakotorAC)
         print("Diskon 5% : ",diskonAC)
         print("PPN 10% : ",PPNAC)
         print("Harga Bersih : ",hargabersihAC)

elif namabarang =='Kulkas':
    if pembelianasli > 4:
     pembelianKulkas = hargakotorKulkas * pembelianasli
     diskonKulkas = pembelianKulkas * (20/100)
     PPNKulkas = (pembelianKulkas - diskonKulkas) * (10/100)
     hargabersihKulkas = pembelianKulkas - diskonKulkas + PPNKulkas
     print("### NOTA PEMBELIAN BARANG ###")
     print("Nama Pelanggan :",namapelanggan)
     print("Produk Pilihan : Kulkas")
     print("Jumlah Beli :",pembelian)
     print("Harga Kotor :",hargakotorKulkas)
     print("Diskon 5% :",diskonKulkas)
     print("PPN 10% :",PPNKulkas)
     print("Harga Bersih :",hargabersihKulkas)
    else:
         pembelianKulkas = hargakotorKulkas * pembelianasli
         diskonKulkas = pembelianKulkas * (5/100)
         PPNKulkas = (pembelianKulkas - diskonKulkas) * (10/100)
         hargabersihKulkas = pembelianKulkas - diskonKulkas + PPNKulkas
         print("== NOTA PEMBELIAN BARANG ==\n")
         print("Nama Pembeli :",namapelanggan)
         print("Produk Pilihan : Kulkas")
         print("Jumlah Beli : ",pembelian)
         print("Harga Kotor : ",hargakotorKulkas)
         print("Diskon 5% : ",diskonKulkas)
         print("PPN 10% : ",PPNKulkas)
         print("Harga Bersih : ",hargabersihKulkas)

else:
    print('Produk Tidak Tersedia')