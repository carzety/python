#Membuat Aplikasi Sederhana-01

judul ='\nSLIP GAJI PT. XYZ'
nama =['Ahmad','Alex']
agama =['Islam','Kristen Protestan']
anak = [2 , 5]
gajipokok = [4000000 , 6000000]

#Berhitung
tunjanganjabatan = 20/100*gajipokok[0]
tunjanganjabatan1 = 20/100*gajipokok[1]

tunjangankeluarga = 10/100*gajipokok[0] if anak[0] <= 2 else 20/100*gajipokok[0]
tunjangankeluarga1 = 10/100*gajipokok[1] if anak[1] <= 2 else 20/100*gajipokok[1]

gajikotor = gajipokok[0] + tunjanganjabatan + tunjangankeluarga
gajikotor1 = gajipokok[1] + tunjanganjabatan1 + tunjangankeluarga1

zakat = ((0), (gajikotor*2.5/100)) [agama[0] == 'Islam' and gajikotor > 6000000]
zakat1 = ((0), (gajikotor1*2.5/100)) [agama[1] == 'Islam' and gajikotor1 > 6000000]

gajibersih = gajikotor - zakat
gajibersih1 = gajikotor1 - zakat1

#Mencetak Data

print(judul)
print('--------------------')

print('Nama Pegawai \t\t:',nama[0],
'\nAgama \t\t\t:',agama[0],
'\nJumlah Anak \t\t:',anak[0],
'\nGaji Pokok \t\t: Rp.',gajipokok[0],
'\nTunjangan Jabatan \t: Rp.',tunjanganjabatan,
'\nTunjangan Keluarga \t: Rp.',tunjangankeluarga,
'\nGaji Kotor \t\t: Rp.',gajikotor,
'\nZakat \t\t\t: Rp.',zakat,
'\nTake Home Pay \t\t: Rp.',gajibersih)


print(judul)
print('--------------------')

print('Nama Pegawai \t\t:',nama[1],
'\nAgama \t\t\t:',agama[1],
'\nJumlah Anak \t\t:',anak[1],
'\nGaji Pokok \t\t: Rp.',gajipokok[1],
'\nTunjangan Jabatan \t: Rp.',tunjanganjabatan1,
'\nTunjangan Keluarga \t: Rp.',tunjangankeluarga1,
'\nGaji Kotor \t\t: Rp.',gajikotor1,
'\nZakat \t\t\t: Rp.',zakat1,
'\nTake Home Pay \t\t: Rp.',gajibersih1)