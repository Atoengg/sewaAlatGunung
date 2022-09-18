def garis ():
    print('=======================================================================')
def daftarharga():
    if (listbarang[i]==1):
        jenisbarang.append('kompor')
        listharga.append(7000)
    elif (listbarang[i]==2):
        jenisbarang.append('matras')
        listharga.append(3000)
    elif (listbarang[i]==3):
        jenisbarang.append('tenda')
        listharga.append(25000)
    elif (listbarang[i]==4):
        jenisbarang.append('sleeping bag')
        listharga.append(6000)
    elif (listbarang[i]==5):
        jenisbarang.append('flysheet')
        listharga.append(10000)
    elif (listbarang[i]==6):
        jenisbarang.append('tracking pole')
        listharga.append(5000)
    else:
        jenisbarang.append('headlamp')
        listharga.append(4000)
def data():
    pemesan = str(input('masukan nama penyewa: '))
    identitas = str(input('identitas anda\nlaki-laki/perempuan? '))
    while identitas not in ['laki-laki','perempuan']:
        print('maaf identitas tidak diketahui')
        identitas = str(input('identitas anda\nlaki-laki/perempuan? '))
    nomorhp = int(input('nomer hp\n+62 '))
    berangkat = int(input("tanggal berangkat mendaki(1-31): "))
    while berangkat not in range(1,32):
        print('maaf tanggal tidak tersedia')
        berangkat = int(input("tanggal berangkat mendaki(1-31): "))
    bulan = int(input('bulan(1-12): '))
    while bulan not in range(1,13):
        print('maaf Bulan tidak tersedia')
        bulan = int(input('bulan(1-12): '))
    tahun = int(input('tahun: '))
    while tahun <= 2020:
        print('maaf tahun sudah kadaluarsa')
        tahun = int(input('tahun: '))
    print()
    pulang = int(input('tanggal pulang mendaki(1-31): '))
    while pulang not in range(1,32):
        print('maaf tanggal tidak tersedia')
        pulang = int(input("tanggal pulang mendaki(1-31): "))
    bulan = int(input('bulan(1-12): '))
    while bulan not in range(1,13):
        print('maaf Bulan tidak tersedia')
        bulan = int(input('bulan(1-12): '))
    tahun = int(input('tahun: '))
    while tahun <= 2020:
        print('maaf tahun sudah kadaluarsa')
        tahun = int(input('tahun: '))
    nama_pemesan.append(pemesan)
    nama_pemesan.append(identitas)
    nama_pemesan.append(nomorhp)
    tgl_berangkat.append(berangkat)
    tgl_berangkat.append(bulan)
    tgl_berangkat.append(tahun)
    tgl_pulang.append(pulang)
    tgl_pulang.append(bulan)
    tgl_pulang.append(tahun)
def pembayaran():
    stop = False
    while (not stop):
        bayar = int(input('masukan uang pembayaran Rp.'))
        print('transaksi anda sedang diproses\nmohon ditunggu....')
        time.sleep(4)
        if bayar > total_semua:
            kembali = bayar - total_semua
            print('uang kembalian anda Rp.',kembali)
            stop = True
        elif bayar == total_semua:
            print('uang kembalian anda Rp.0')
            stop = True
        else:
            print('mohon maaf uang anda tidak cukup, silahkan bayar ulang!')

garis()
print('SEWA ALAT OUTDOOR PENDAKI GUNUNG'.center(60))
print('SELAMAT DATANG DI ATOENG_RENTAL ALAT PENDAKIAN GUNUNG'.center(60))
garis()

listbarang = []
jenisbarang = []
listharga = []
banyaksewa = []
listtb = []
nama_pemesan = []
tgl_berangkat = []
tgl_pulang = []
hari = []
total_sewa = 0
total = 0
jumlah = 0

import time
tanya = 'ya'
tanya = str(input("apakah anda ingin sewa alat pendakian gunung(ya/no): "))
while tanya == 'ya':
    garis()
    print('Berikut Alat Outdoor Pendaki Gunung Yang Disewakan ')
    print('No | Barang \t\t\t  Daftar Harga')
    print("1. | kompor\t\t:",'\tRp',7000,"per hari")
    print("2. | matras\t\t:",'\tRp',3000,"per hari")
    print("3. | tenda\t\t:",'\tRp',25000,"per hari")
    print("4. | sleeping bag\t:",'\tRp',6000,"per hari")
    print("5. | flysheet\t\t:",'\tRp',10000,"per hari")
    print("6. | tracking pole\t:",'\tRp',5000,"per hari")
    print("7. | headlamp\t\t:",'\tRp',4000,"per hari")
    garis()


    stop = False
    while (not stop):
        a = int(input('berapa banyak data alat yang anda sewa dari menu di atas? '))
        for i in range(a):
            barang = int(input('pilih alat yang akan disewa(1-7): '))
            while barang not in range(1,8):
                print('maaf menu pilihan tidak tersedia')
                barang = int(input('pilih alat yang akan disewa(1-7): '))
            listbarang.append(barang)
            sewa = int(input('banyak alat yang disewa: '))
            banyaksewa.append(sewa)
            daftarharga()
            listtb.append(banyaksewa[i]*listharga[i])
        stop = True
    print()

    data()
    jml_hari = tgl_pulang[0] - tgl_berangkat[0]
    hari.append(jml_hari)

    print()
    garis()
    print('STRUK HASIL ALAT YANG DISEWA'.center(60))
    garis()
    print('No.  alat\t  Harga\t    banyak sewa\t  total bayar')
    for i in range(a):
        print('%d.  %s\t     Rp.%d\t  %d\t    Rp.%d'%(i+1,jenisbarang[i],listharga[i],banyaksewa[i],listtb[i]))
        total_sewa = total_sewa + banyaksewa[i]
        jumlah = jumlah + listtb[i]
        total = total + (listtb[i]*hari[0])
    garis()
    print('jumlah =\t\t\t\t\tRp.',jumlah,
    '\nHari =\t\t\t\t\t\t', hari[0]
    )
    garis()
    print('Total semuanya =\t\t\t\tRp.', total)
    print()

    print('nama penyewa :', nama_pemesan[0],
    '\nidentitas :', nama_pemesan[1],
    '\nnomer hp:+62',nama_pemesan[2],
    '\nberangkat mendaki tgl/Bulan/Tahun: ', tgl_berangkat[0],'/',tgl_berangkat[1],'/',tgl_berangkat[2],
    '\npulang mendaki tgl/Bulan/Tahun: ', tgl_pulang[0],'/',tgl_pulang[1],'/',tgl_pulang[2],
    '\nmelakukan pendakian selama:',hari[0],'hari'
    )
    print('total sewa alat: %d ' % total_sewa)

    if total_sewa > 5 :
       diskon = 0.25*total
       total_semua = total - diskon 
       print('karena total sewa alat lebih dari 5\nselamat anda mendapat diskon tahun baru sebesar 25%')
       print('total semuanya setelah mendapatkan diskon Rp.',total_semua)
    else:
        print('anda tidak mendapatkan diskon tahun baru!')
        total_semua = total 
    print()
    pembayaran()
    break
print('TERIMA KASIH')