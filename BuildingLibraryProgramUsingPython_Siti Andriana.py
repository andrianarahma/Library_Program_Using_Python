from tabulate import tabulate
from datetime import datetime as dti, timedelta

#data dummy
semuaBuku = [
    {"Index" : 0,
     "Label" : "FN-A1-9786020822341-1",
     "Letak" : "A1",
     "Genre" : "Fiksi",
     "Subgenre" : "Novel",
     "Judul" : "Tentang Kamu",
     "Penulis" : "Tere Liye",
     "ISBN" : "9786020822341",
     "Ketersediaan" : "Kosong",
     "Nama Peminjam" : "Rania Alisha",
     "No. Anggota" : 133,
     "Kontak" :"081257058231",
     "Alamat" :"Jl. Pangeran Antasari No. 15, Samarinda",
     "Tanggal Pinjam" : "15-09-2024",
     "Maks Tanggal Kembali" : "22-09-2024"
    },
    {"Index" : 1,
     "Label" : "FN-A1-9786020822341-2",
     "Letak" : "A1",
     "Genre" : "Fiksi",
     "Subgenre" : "Novel",
     "Judul" : "Tentang Kamu",
     "Penulis" : "Tere Liye",
     "ISBN" : "9786020822341",
     "Ketersediaan" : "Ada",
     "Nama Peminjam" : "",
     "No. Anggota" : 0,
     "Kontak" :"",
     "Alamat" :"",
     "Tanggal Pinjam" : "",
     "Maks Tanggal Kembali" : ""
    },
    {"Index" : 2,
     "Label" : "FN-A1-9786239554507-1",
     "Letak" : "A1",
     "Genre" : "Fiksi",
     "Subgenre" : "Novel",
     "Judul" : "Pulang",
     "Penulis" : "Tere Liye",
     "ISBN" : "9786239554507",
     "Ketersediaan" : "Kosong",
     "Nama Peminjam" : "Rania Alisha",
     "No. Anggota" : 133,
     "Kontak" :"081257058231",
     "Alamat" :"Jl. Pangeran Antasari No. 15, Samarinda",
     "Tanggal Pinjam" : "15-09-2024",
     "Maks Tanggal Kembali" : "22-09-2024"
    },
    {"Index" : 3,
     "Label" : "FN-A1-9786239554507-2",
     "Letak" : "A1",
     "Genre" : "Fiksi",
     "Subgenre" : "Novel",
     "Judul" : "Pulang",
     "Penulis" : "Tere Liye",
     "ISBN" : "9786239554507",
     "Ketersediaan" : "Ada",
     "Nama Peminjam" : "",
     "No. Anggota" : 0,
     "Kontak" :"",
     "Alamat" :"",
     "Tanggal Pinjam" : "",
     "Maks Tanggal Kembali" : ""
    },
    {"Index" : 4,
     "Label" : "FN-A1-9786239554507-3",
     "Letak" : "A1",
     "Genre" : "Fiksi",
     "Subgenre" : "Novel",
     "Judul" : "Pulang",
     "Penulis" : "Tere Liye",
     "ISBN" : "9786239554507",
     "Ketersediaan" : "Ada",
     "Nama Peminjam" : "",
     "No. Anggota" : 0,
     "Kontak" : "",
     "Alamat" : "",
     "Tanggal Pinjam" : "",
     "Maks Tanggal Kembali" : ""
    },
    {"Index" : 5,
     "Label" : "NP-B20-9786236219577-1",
     "Letak" : "B20",
     "Genre" : "Nonfiksi",
     "Subgenre" : "Psikologi",
     "Judul" : "Terapi Berpikir Positif",
     "Penulis" : "Dr. Ibrahim Elfiky",
     "ISBN" : "9786236219577",
     "Ketersediaan" : "Kosong",
     "Nama Peminjam" : "Rania Alisha",
     "No. Anggota" : 133,
     "Kontak" :"081257058231",
     "Alamat" :"Jl. Pangeran Antasari No. 15, Samarinda",
     "Tanggal Pinjam" : "15-09-2024",
     "Maks Tanggal Kembali" : "22-09-2024"
    },
    {"Index" : 6,
     "Label" : "NP-B20-9786236219577-2",
     "Letak" : "B20",
     "Genre" : "Nonfiksi",
     "Subgenre" : "Psikologi",
     "Judul" : "Terapi Berpikir Positif",
     "Penulis" : "Dr. Ibrahim Elfiky",
     "ISBN" : "9786236219577",
     "Ketersediaan" : "Kosong",
     "Nama Peminjam" : "Zahratunnisa",
     "No. Anggota" : 131,
     "Kontak" : "085652346712",
     "Alamat" : "Jl. KH. Mas Mansyur No. 5, Samarinda",
     "Tanggal Pinjam" : "14-09-2024",
     "Maks Tanggal Kembali" : "21-09-2024"
    },
    {"Index" : 7,
     "Label" : "NP-B20-9786236219577-3",
     "Letak" : "B20",
     "Genre" : "Nonfiksi",
     "Subgenre" : "Psikologi",
     "Judul" : "Terapi Berpikir Positif",
     "Penulis" : "Dr. Ibrahim Elfiky",
     "ISBN" : "9786236219577",
     "Ketersediaan" : "Kosong",
     "Nama Peminjam" : "Ridwansyah",
     "No. Anggota" : 132,
     "Kontak" : "081252346715",
     "Alamat" :"Jl. Basuki Rahmat No. 7, Samarinda",
     "Tanggal Pinjam" : "16-09-2024",
     "Maks Tanggal Kembali" : "23-09-2024"
    },
    {"Index" : 8,
     "Label" : "NS-C15-9786023913657-1",
     "Letak" : "C15",
     "Genre" : "Nonfiksi",
     "Subgenre" : "Sejarah",
     "Judul" : "B.J. Habibie Si Jenius",
     "Penulis" : "Jonar T.H. Situmorang, M.A",
     "ISBN" : "9786023913657",
     "Ketersediaan" : "Ada",
     "Nama Peminjam" : "",
     "No. Anggota" : 0,
     "Kontak" :"",
     "Alamat" :"",
     "Tanggal Pinjam" : "",
     "Maks Tanggal Kembali" : ""
    }
]

semuaAnggota=[
    {"No. Anggota" : 131,
     "Nama" : "Zahratunnisa",
     "Alamat" : "Jl. KH. Mas Mansyur No. 5, Samarinda",
     "Kontak" : "085652346712",
     "NIK" : "6472010567899002"
    },
    {"No. Anggota" : 132,
     "Nama" : "Ridwansyah",
     "Alamat" : "Jl. Basuki Rahmat No. 7, Samarinda",
     "Kontak" : "081252346715",
     "NIK" : "6472050986699001"
    },
    {"No. Anggota" : 133,
     "Nama" : "Rania Alisha",
     "Alamat" : "Jl. Pangeran Antasari No. 15, Samarinda",
     "Kontak" : "081257058231",
     "NIK" : "6472050776899001"
    }
]

cartPinjam=[]
cartKembali=[]

#fungsi untuk menampilkan data buku
def lihatData(listData) : 
    print(tabulate(listData, headers="keys",maxcolwidths=15,tablefmt="fancy_grid"))

#buat list ISBN yang unique
def cekDupIsbn() :
    isbn=[]
    isbnUnik=[]
    for i in range(len(semuaBuku)):
        isbn.append(semuaBuku[i]["ISBN"])
        for i in isbn :
            if i not in isbnUnik:
                isbnUnik.append(i)
    return(isbnUnik)

#hitung stok tiap ISBN
def updateStok() :
    ISBN =cekDupIsbn()
    semuaISBN=[]
    for i in range(len(semuaBuku)):
        semuaISBN.append(semuaBuku[i]['ISBN'])
    stok=[]
    for j in range(len(ISBN)):
        stok.append(semuaISBN.count(ISBN[j]))
    return(stok)

#hitung jumlah yang bisa dipinjam
def updateKetersediaan() :
    ISBN =cekDupIsbn()
    jmlTersedia=[]
    for i in range(len(ISBN)):
        jmlKetersediaan = 0
        for j in range(len(semuaBuku)):
            if ISBN[i]==semuaBuku[j]["ISBN"]:
                if semuaBuku[j]["Ketersediaan"]=="Ada":
                    jmlKetersediaan+=1
        jmlTersedia.append(jmlKetersediaan)
    return(jmlTersedia)

#fungsi untuk update nomor index
def updateIndex(listData):
    for i in range(len(listData)):
        listData[i]['Index']=i

#buat rekap koleksi buku
listBuku = []
def rekapBuku() :
    ISBN =cekDupIsbn()
    stok=updateStok()
    ketersediaan = updateKetersediaan()
    for j in range(len(ISBN)):
        for i in range(len(semuaBuku)):
            if ISBN[j] == semuaBuku[i]["ISBN"]:
                listBuku.append(
                    {
                        'Index' : j,
                        'Letak' : semuaBuku[i]['Letak'],
                        'Genre' : semuaBuku[i]['Genre'],
                        'Subgenre' : semuaBuku[i]['Subgenre'],
                        'Judul' : semuaBuku[i]['Judul'],
                        'Penulis' : semuaBuku[i]['Penulis'],
                        'ISBN' : semuaBuku[i]['ISBN'],
                        'Ketersediaan' : ketersediaan[j], 
                        'Stok' : stok[j]
                    }
                )
                break
    return(listBuku)

#buat rekap koleksi buku dengan yang ditampilkan hanya sebagian data saja
listBukuSebagian = []
def bukuSebagian() :
    for i in range(len(semuaBuku)):
        listBukuSebagian.append(
            {
                'Index' : i,
                'Label' : semuaBuku[i]['Label'],
                'Letak' : semuaBuku[i]['Letak'],
                'Genre' : semuaBuku[i]['Genre'],
                'Subgenre' : semuaBuku[i]['Subgenre'],
                'Judul' : semuaBuku[i]['Judul'],
                'Penulis' : semuaBuku[i]['Penulis'],
                'ISBN' : semuaBuku[i]['ISBN']
            }
        )
    # updateIndex(listBukuSebagian)
    return(listBukuSebagian)

#create list buku berdasarkan judul
listJudul = []
def buatListJudul(judul) :
    for i in range(len(semuaBuku)):
        if judul == semuaBuku[i]['Judul']:
            listJudul.append({
                'Label' : semuaBuku[i]['Label'],
                'Genre' : semuaBuku[i]['Genre'],
                'Subgenre' : semuaBuku[i]['Subgenre'],
                'Judul' : semuaBuku[i]['Judul'],
                'Penulis' : semuaBuku[i]['Penulis'],
                'ISBN' : semuaBuku[i]['ISBN'],
                'Ketersediaan' : semuaBuku[i]['Ketersediaan'],
                'Nama Peminjam' : semuaBuku[i]['Nama Peminjam'],
                'No. Anggota' : semuaBuku[i]['No. Anggota'],
                'Maks Tanggal Kembali' : semuaBuku[i]['Maks Tanggal Kembali']
            })
    return(listJudul)

#create list buku available
listAvailable = []
def listBukuTersedia() :
    for i in range(len(semuaBuku)):
        if semuaBuku[i]["Ketersediaan"] == "Ada":
            listAvailable.append({
                'Index' : i,
                'Label' : semuaBuku[i]['Label'],
                'Genre' : semuaBuku[i]['Genre'],
                'Subgenre' : semuaBuku[i]['Subgenre'],
                'Judul' : semuaBuku[i]['Judul'],
                'Penulis' : semuaBuku[i]['Penulis'],
                'ISBN' : semuaBuku[i]['ISBN']
            })
        updateIndex(listAvailable)
    return(listAvailable)

#create list buku berdasarkan ISBN
listByIsbn=[]
def cekByIsbn(isbn) :
    listBukuTersedia()
    for i in range(len(listAvailable)):
        if isbn == listAvailable[i]['ISBN']:
            listByIsbn.append({
                'Index' : i,
                'Label' : listAvailable[i]['Label'],
                'Genre' : listAvailable[i]['Genre'],
                'Subgenre' : listAvailable[i]['Subgenre'],
                'Judul' : listAvailable[i]['Judul'],
                'Penulis' : listAvailable[i]['Penulis'],
                'ISBN' : listAvailable[i]['ISBN']
            })
        updateIndex(listByIsbn)
    listAvailable.clear()
    return(listByIsbn)

listByNoAnggota = []
def cekNoAnggota(nomor) :
    print(f"Nomor Kawan Baca : {nomor}")
    for i in range(len(semuaBuku)):
        if semuaBuku[i]["No. Anggota"] == nomor:
            listByNoAnggota.append({
                'Index' : i,
                'Label' : semuaBuku[i]['Label'],
                'Genre' : semuaBuku[i]['Genre'],
                'Subgenre' : semuaBuku[i]['Subgenre'],
                'Judul' : semuaBuku[i]['Judul'],
                'Penulis' : semuaBuku[i]['Penulis'],
                'ISBN' : semuaBuku[i]['ISBN'],
                'Tanggal Pinjam' : semuaBuku[i]['Tanggal Pinjam'],
                'Maks Tanggal Kembali' : semuaBuku[i]['Maks Tanggal Kembali']
            })
        updateIndex(listByNoAnggota)
    return(listByNoAnggota)

listByTglKembali = []
def cekTglKembali(tanggal) :
    print(f"Maksimal Tanggal Kembali: {tanggal}")
    for i in range(len(semuaBuku)):
        if semuaBuku[i]["Maks Tanggal Kembali"] == tanggal:
            listByTglKembali.append({
                'Index' : i,
                'Nama Peminjam' : semuaBuku[i]['Nama Peminjam'],
                'No. Anggota' : semuaBuku[i]['No. Anggota'],
                'Kontak': semuaBuku[i]['Kontak'],
                'Alamat' : semuaBuku[i]['Alamat'],
                'Label' : semuaBuku[i]['Label'],
                'Genre' : semuaBuku[i]['Genre'],
                'Subgenre' : semuaBuku[i]['Subgenre'],
                'Judul' : semuaBuku[i]['Judul'],
                'Penulis' : semuaBuku[i]['Penulis'],
                'ISBN' : semuaBuku[i]['ISBN']
            })
        updateIndex(listByTglKembali)
    return(listByTglKembali)

def tambahBuku() :
    isbnBuku = input("Masukkan nomor ISBN buku : ")
    ISBN=cekDupIsbn()
    stokBuku = int(input("Masukkan jumlah buku : "))
    for i in range(len(ISBN)):
        if isbnBuku == ISBN[i]:
            for j in range(updateStok()[i]+1,updateStok()[i]+stokBuku+1):
                label = semuaBuku[i]['Genre'][0]+semuaBuku[i]['Subgenre'][0]+"-"+semuaBuku[i]['Letak']+"-"+isbnBuku+"-"+str(j)
                semuaBuku.append({
                    'Genre' : semuaBuku[i]['Genre'],
                    'Subgenre' : semuaBuku[i]['Subgenre'],
                    'Judul' : semuaBuku[i]['Judul'],
                    'Penulis' : semuaBuku[i]['Penulis'],
                    'Letak' : semuaBuku[i]['Letak'],
                    'ISBN' : isbnBuku,
                    'Ketersediaan' : "Ada",
                    'Label' : label,
                    "Nama Peminjam" : "",
                    "No. Anggota" : 0,
                    "Kontak" : "",
                    "Alamat" : "",
                    "Tanggal Pinjam" : "",
                    "Maks Tanggal Kembali" : ""
                })
            break 
    else:
        while True:
            genreBuku = input("Masukkan genre buku (fiksi/nonfiksi) : ").capitalize()
            if genreBuku == "Fiksi" or genreBuku == "Nonfiksi":
                break
            else :
                (print("Masukkan genre buku yang benar"))

        subgenreBuku = input("Masukkan subgenre buku : ").capitalize()
        judulBuku = input("Masukkan judul buku : ")
        penulisBuku = input("Masukkan nama penulis : ")
        letakBuku = input("Masukkan letak buku akan disimpan : ").capitalize()
        
        for i in range(1,stokBuku+1):
            label = genreBuku[0]+subgenreBuku[0]+"-"+letakBuku+"-"+isbnBuku+"-"+str(i)
            semuaBuku.append({
                    'Genre' : genreBuku,
                    'Subgenre' : subgenreBuku,
                    'Judul' : judulBuku,
                    'Penulis' : penulisBuku,
                    'Letak' : letakBuku,
                    'ISBN' : isbnBuku,
                    'Ketersediaan' : "Ada",
                    'Label' : label,
                    "Nama Peminjam" : "",
                    "No. Anggota" : 0,
                    "Kontak" : "",
                    "Alamat" : "",
                    "Tanggal Pinjam" : "",
                    "Maks Tanggal Kembali" : ""
                })
    updateIndex(semuaBuku)
    bukuSebagian()
    lihatData(listBukuSebagian)
    listBukuSebagian.clear()

#fungsi untuk menghapus koleksi buku
def hapusBuku() :
    bukuSebagian()
    lihatData(listBukuSebagian)
    indexBuku = int(input("Masukkan index buku yang mau dihapus: "))
    del listBukuSebagian[indexBuku]
    del semuaBuku[indexBuku]
    updateIndex(semuaBuku)
    updateIndex(listBukuSebagian)
    lihatData(listBukuSebagian)
    listBukuSebagian.clear()

#fungsi untuk validasi nomor anggota (memunculkan langsung nama anggota setelah input nomor anggota)
def validAnggota(noAnggota):
    for i in range(len(semuaAnggota)):
        if noAnggota == semuaAnggota[i]["No. Anggota"]:
            namaLengkap = semuaAnggota[i]["Nama"]
            break
    return namaLengkap

#fungsi untuk meminjam buku
def pinjamBuku() :
    noAnggota = int(input("Masukkan nomor anggota : "))
    for i in range(len(semuaAnggota)):
        if noAnggota == semuaAnggota[i]["No. Anggota"]:
            while True:
                try:
                    namaLengkap = validAnggota(noAnggota)
                    print(f"Nama : {namaLengkap}")
                    ISBN = input("Masukkan ISBN buku yang mau dipinjam : ")
                    cekByIsbn(ISBN)
                    updateIndex(listByIsbn)
                    lihatData(listByIsbn)
                    
                    indexBuku=int(input("Masukkan index buku yang mau dipinjam : "))

                    cartPinjam.append({
                        'Label' : listByIsbn[indexBuku]['Label'],
                        'Judul' : listByIsbn[indexBuku]['Judul'],
                        'Penulis' : listByIsbn[indexBuku]['Penulis'],
                        'ISBN' : listByIsbn[indexBuku]['ISBN']
                    })

                    for i in range(len(cartPinjam)):
                        for j in range(len(semuaBuku)):
                            if cartPinjam[i]['Label'] == semuaBuku[j]['Label']:
                                semuaBuku[j]["Ketersediaan"] = "Kosong"
                    
                    del listByIsbn[indexBuku]
                    updateIndex(listByIsbn)

                    print("Isi Keranjang : ".center(55))
                    lihatData(cartPinjam)
                    
                    check = input("Mau pinjam yang lain? (Y/T) : ").upper()
                    if check =="T":
                        break
                except:
                    print("Tidak ada buku tersedia")
            
            print("\nDaftar Pinjaman Buku\n")

            print(f"Nama : {namaLengkap}")
            print(f"No. Anggota : {noAnggota}")

            tglPinjam = dti.now()
            print(f"Tanggal Pinjam : {tglPinjam.strftime("%d-%m-%Y")}")
            tglKembali = tglPinjam + timedelta(days=7)
            print(f"Maksimal Tanggal Kembali : {tglKembali.strftime("%d-%m-%Y")}")
            lihatData(cartPinjam)
            
            for i in range(len(cartPinjam)):
                for j in range(len(semuaBuku)):
                    if cartPinjam[i]['Label'] == semuaBuku[j]['Label']:
                        semuaBuku[j]['Nama Peminjam'] = namaLengkap
                        semuaBuku[j]['No. Anggota'] = noAnggota
                        semuaBuku[j]['Tanggal Pinjam'] = tglPinjam.strftime("%d-%m-%Y")
                        semuaBuku[j]['Maks Tanggal Kembali'] = tglKembali.strftime("%d-%m-%Y")
            break
    else:
        print("Nomor tidak terdaftar")
    cartPinjam.clear()
    listByIsbn.clear()

def kembalikanBuku(): 
    noAnggota = int(input("Masukkan nomor anggota : "))

    for i in range(len(semuaAnggota)):
        if noAnggota == semuaAnggota[i]["No. Anggota"]:
            while True:
                try:
                    namaLengkap = validAnggota(noAnggota)
                    print(f"Nama : {namaLengkap}")
                    cekNoAnggota(noAnggota)
                    lihatData(listByNoAnggota)
                    indexBuku = int(input("Masukkan index buku yang dikembalikan : "))

                    cartKembali.append({
                            'Label' : listByNoAnggota[indexBuku]['Label'],
                            'Judul' : listByNoAnggota[indexBuku]['Judul'],
                            'Penulis' : listByNoAnggota[indexBuku]['Penulis'],
                            'ISBN' : listByNoAnggota[indexBuku]['ISBN']
                        })
                    
                    for i in range(len(cartKembali)):
                        for j in range(len(semuaBuku)):
                            if cartKembali[i]['Label'] == semuaBuku[j]['Label']:
                                semuaBuku[j]["Ketersediaan"] = "Ada"
                                semuaBuku[j]['Nama Peminjam'] = ""
                                semuaBuku[j]['No. Anggota'] = 0
                                semuaBuku[j]['Tanggal Pinjam'] = ""
                                semuaBuku[j]['Maks Tanggal Kembali'] = ""

                    del listByNoAnggota[indexBuku]
                    updateIndex(listByNoAnggota)

                    print("Isi Keranjang Pengembalian : ".center(55))
                    lihatData(cartKembali)
                        
                    check = input("Masih ada buku yang mau dikembalikan? (Y/T) : ").upper()
                    if check =="T":
                        break
                except:
                    print("Semua buku sudah dikembalikan. Terima kasih.")
                    break
        
            print("\nDaftar Pengembalian Buku\n")

            print(f"Nama : {namaLengkap}")
            print(f"No. Anggota : {noAnggota}")

            tglKembali = dti.now()
            print(f"Tanggal Pengembalian : {tglKembali.strftime("%d-%m-%Y")}")
            lihatData(cartKembali)

            print("Terima kasih sudah mengembalikan bukunya. Semoga anda selalu bahagia!")
            break
    else :
        print("Nomor yang ada masukkan tidak terdaftar")

    listByNoAnggota.clear()

def daftarJadiAnggota():
    nama = input("Masukkan nama lengkap : ")
    alamat = input("Masukkan alamat lengkap domisili : ")
    kontak = input("Masukkan nomor yang bisa dihubungi : ")
    nik = input("Masukkan NIK : ")
    for i in range(len(semuaAnggota)):
        noAnggota = semuaAnggota[i]["No. Anggota"]+1
    semuaAnggota.append({
        "Nama" : nama,
        "Alamat" : alamat,
        "Kontak" : kontak,
        "NIK" : nik,
        "No. Anggota" : noAnggota
    }
    )
    print(f'\nSelamat!\nKamu sudah menjadi Kawan Baca di Perpustakaan "Bahagia" dengan nomor : {noAnggota}')

listDenganNik=[]
def cekNik(NIK) :
    for i in range(len(semuaAnggota)):
        if NIK == semuaAnggota[i]['NIK']:
            listDenganNik.append(
                {"Nama" : semuaAnggota[i]['Nama'],
                 "Alamat" : semuaAnggota[i]['Alamat'],
                 "Kontak" : semuaAnggota[i]['Kontak'],
                 "NIK" : semuaAnggota[i]['NIK'],
                 "No. Anggota" : semuaAnggota[i]['No. Anggota']  
                }
            )
    return(listDenganNik)

def tampilkanMenuUtama() :
    menuUtama = input('''
            Selamat Datang di Perpustakaan "Bahagia"
      
            List Menu :
            1. Menampilkan Daftar Buku
            2. Menambah Buku
            3. Menghapus Buku
            4. Meminjam Buku
            5. Mengembalikan Buku
            6. Daftar Menjadi Kawan Baca
            7. Cek Keanggotaan
            8. Exit Program
      
            Masukkan menu yang diinginkan : ''')
    return menuUtama

while True : 
    menuUtama = tampilkanMenuUtama()
    
    if menuUtama == "1":
        while True:
            menu1 = input('''
                Pilih data:
                1. Berdasarkan Judul Buku
                2. Data Peminjaman Buku
                3. Data Buku yang Tersedia 
                4. Ringkasan Data Buku
                5. Menu utama
                        
                Masukkan data yang mau ditampilkan : ''')
            if menu1=="1" :
                try : 
                    buatListJudul(input("Masukkan judul buku dengan penulisan yang tepat : "))
                    print("\nData Hasil Pencarian\n".center(45))
                    lihatData(listJudul)
                    listJudul.clear()
                except:
                    print("Mohon maaf, buku belum tersedia".center(45))
    
            elif menu1=="2" :
                while True:
                    menu1_2 = input('''
                        Pilih data:
                        1. Berdasarkan No. Kawan Baca
                        2. Berdasarkan Maksimal Tanggal Kembali
                        3. Menu sebelumnya
                                
                        Masukkan data yang mau ditampilkan : ''')
                    if menu1_2=="1" :
                        nomor = int(input("Masukkan nomor kawan baca : "))
                        cekNoAnggota(nomor)
                        for j in range(len(semuaAnggota)):
                            if nomor == semuaAnggota[j]["No. Anggota"]:
                                print(f"Nama : {semuaAnggota[j]['Nama']}")
                                print(f"Kontak : {semuaAnggota[j]['Kontak']}")
                                print(f"Alamat: {semuaAnggota[j]['Alamat']}")
                                print("\nData Hasil Pencarian\n".center(45))
                                lihatData(listByNoAnggota)
                                break
                        else: 
                            print("Nomor belum terdaftar")
                        listByNoAnggota.clear()

                    elif menu1_2=="2":
                        tglKembali = input("Masukkan maksimal tanggal kembali (contoh : 21-09-2024) : ")
                        cekTglKembali(tglKembali)
                        for i in range(len(semuaBuku)):
                            if tglKembali == semuaBuku[i]["Maks Tanggal Kembali"]:
                                print("\nData Hasil Pencarian\n".center(100))
                                lihatData(listByTglKembali)
                                break
                        else:
                            print(f"Tidak ada buku yang harus dikembalikan pada tanggal {tglKembali}")
                        listByTglKembali.clear()

                    elif menu1_2=="3" :
                        break
            
            elif menu1=="3":
                listBukuTersedia()
                print("\nData Hasil Pencarian\n".center(100))
                lihatData(listAvailable)
                listAvailable.clear()
            elif menu1=="4" :
                rekapBuku()
                print("\nData Hasil Pencarian\n".center(100))
                lihatData(listBuku)
                listBuku.clear()
            elif menu1=="5" :
                break
    
    elif menuUtama == "2":
        tambahBuku()
    elif menuUtama == "3":
        hapusBuku()
    elif menuUtama == "4":
        pinjamBuku()
    elif menuUtama == "5":
        kembalikanBuku()
    elif menuUtama == "6":
        daftarJadiAnggota()
    elif menuUtama == "7":
        while True:
            menu7 = input('''
                Pilih data:
                1. Berdasarkan NIK
                2. Semua Data
                3. Menu utama
                        
                Masukkan data yang mau ditampilkan : ''')
            if menu7=="1" : 
                nik = (input("Masukkan NIK : "))
                cekNik(nik)
                for i in range(len(semuaAnggota)):
                    if nik == semuaAnggota[i]["NIK"] :
                        print("\nData Hasil Pencarian\n".center(45))
                        lihatData(listDenganNik)
                        break
                else : 
                    print("Mohon maaf, data anda belum terdaftar sebagai Kawan Baca".center(45))                
                listDenganNik.clear()
                
            elif menu7=="2" :
                print("\nData Hasil Pencarian\n".center(100))
                lihatData(semuaAnggota)
            elif menu7=="3" :
                break
    elif menuUtama == "8":
        break
    else:
        print("Menu yang anda masukkan belum tersedia")