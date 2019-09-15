# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import sys
from math import log10
from constant import *


def cetakPapan(papan):
    # Prosedur untuk menampilkan kondisi papan ke layar
    # I.S. papan terdefinisi sebagai matriks persegi
    # F.S. papan tercetak di layar

    dim = len(papan)
    ORD = int(log10(dim))+1  # ordo dari dimensi papan
    SPACE = " "*ORD  # jumlah spasi
    GARISH = " "+SPACE+(("+--"+"-"*ORD)*(dim))+"+"  # garis horizontal
    GARISV = " "+SPACE+(("|  "+" "*ORD)*(dim))+"|"  # garis vertikal
    offset = int(1 + (ORD/2))  # offset karakter dari border
    tail = (2 + ORD) - (offset+1)  # jumlah spasi di belakang karakter

    # cetak koordinat X
    print("   ", end=SPACE)
    for i in range(dim):
        ordoI = int(log10(i+1))
        print(f"{i+1}  "+" "*(ORD-ordoI), end="")

    # cetak Isi
    print("\n"+GARISH)
    for y in range(dim):
        print(GARISV)
        ordoY = int(log10(y+1))
        # cetak koordinat Y
        print(y+1, end=" "*(ORD-ordoY))
        # cetak isi papan
        for x in papan[y]:
            print("|"+" "*offset+x, end=" "*tail)
        print("|")
        print(GARISV)
        print(GARISH)


def buatPapanKosong(dim):
    # Fungsi untuk membuat papan kosong sesuai ukuran dimensi
    return [[KOSONG] * dim for i in range(dim)]


def resetPapanReversi(papan):
    # Prosedur untuk membuat papan yang ada menjadi papan reversi standar
    # I.S. papan terdefinisi sebagai matrik persegi dengan
    #      panjang sisi genap dan >= 2
    # F.S. papan menjadi papan reversi standar dengan x = hitam, o = putih
    #      terletak di tengah papan

    # mengosongkan papan
    for row in papan:
        for col in row:
            col = KOSONG
    dim = len(papan)
    mid = int((dim/2)-1)
    # menetapkan kondisi awal reversi
    papan[mid][mid] = papan[mid+1][mid+1] = PUTIH
    papan[mid+1][mid] = papan[mid][mid+1] = HITAM


def dalamPapan(x, y):
    # Fungsi untuk memeriksa apakah indeks x dan y ada dalam jangkauan papan
    return x >= 0 and x <= DIM - 1 and y >= 0 and y <= DIM-1


def lawanGiliran(giliran):
    # Fungsi yang mengembalikan lawan dari giliran sekarang
    if giliran == HITAM:
        lawan = PUTIH
    else:
        # giliran putih
        lawan = HITAM
    return lawan


def cekGerakanValid(papan, giliran, posX, posY):
    # Fungsi untuk memeriksa apakah langkah pada posX dan posY adalah valid pada giliran "giliran"
    # Mengembalikan false jika tidak valid atau posisi disk yang bersebarangan jika true
    if (not dalamPapan(posX, posY) or papan[posY][posX] != KOSONG):
        # print(1)
        return False
    else:
        # posisi di dalam papan dan petak dalam keadaan kosong
        papan[posY][posX] = giliran  # set sementara untuk pemeriksaan
        lawan = lawanGiliran(giliran)
        lokasi = []
        for arahX, arahY in ARAH:
            # cek pada semua arah
            x, y = posX, posY
            x += arahX
            y += arahY
            if not dalamPapan(x, y):
                continue
            else:
                # masih dalam papan
                if papan[y][x] == lawan:
                    # sebelah pertama harus lawan
                    while papan[y][x] == lawan:
                        x += arahX
                        y += arahY
                        if not dalamPapan(x, y):
                            break
                    if dalamPapan(x, y):
                        # x,y masih dalam papan
                        if papan[y][x] == giliran:
                            # menemukan seberangnya
                            lokasi.append([x, y])
        papan[posY][posX] = KOSONG  # dikosongkan kembali
        if len(lokasi) == 0:
            # tidak ada disk di seberang
            return False
        else:
            # ada disk di seberang
            return lokasi


def revers(papan, giliran, lokasi, posX, posY):
    # Prosedur untuk membalikan semua disk dari posX, posY
    #       sampai semua titik di lokasi
    # I.S. papan, giliran, lokasi, posX, dan posY terdefinisi,
    #       posX an posY adalah posisi yang valid
    # F.S. semua disk dari posX, posY hingga semua titik di lokasi dibalik
    #       berlawanan dengan giliran
    lawan = lawanGiliran(giliran)
    papan[posY][posX] = giliran
    for akhirX, akhirY in lokasi:
        x, y = posX, posY
        arahX = int(akhirX - posX)
        arahY = int(akhirY - posY)
        # ubah ke arah satuan
        if arahX != 0:
            arahX //= abs(arahX)
        if arahY != 0:
            arahY //= abs(arahY)
        x += arahX
        y += arahY
        # balikan semua disk yang lawan
        while papan[y][x] == lawan:
            papan[y][x] = giliran
            x += arahX
            y += arahY


def copyPapan(papan):
    # Fungsi yang mengembalikan salinan dari papan masukan
    copy = buatPapanKosong(len(papan))

    for row in range(len(papan)):
        for col in range(len(papan)):
            copy[row][col] = papan[row][col]
    return copy


def gerakanTersedia(papan, giliran):
    # Fungsi yang menghasilkan semua titik gerakan yang mungkin dilakukan pada giliran "giliran"
    tersedia = []
    for y in range(len(papan)):
        for x in range(len(papan)):
            if cekGerakanValid(papan, giliran, x, y) != False:
                tersedia.append([x, y])
    return tersedia


def papanBerhint(papan, giliran):
    # Fungsi yang mengembalikan papan dengan hint yang diberikan
    #       bagi giliran "giliran"
    salinan = copyPapan(papan)

    for x, y in gerakanTersedia(papan, giliran):
        salinan[y][x] = HINT
    return salinan


def hitungSkor(papan):
    # Fungsi yang mengembalikan skor pada papan dalam map
    nHitam = nPutih = 0
    for row in papan:
        for col in row:
            if col == HITAM:
                nHitam += 1
            elif col == PUTIH:
                nPutih += 1
    return {HITAM: nHitam, PUTIH: nPutih}


def validasiMasukan(papan, giliran):
    # Prosedur yang mengatur input pada saat giliran "giliran"
    # I.S. papan dan giliran terdefinisi
    # F.S. mengembalikan input hint/ quit/
    #       titik disk yang diterima yang valid untuk gerakan dan titik seberangnya
    valid = False
    while not valid:
        masukan = input("masukan: ").lower()
        if masukan in HINTKEY:
            return "hint"
        elif masukan in QUITKEY:
            return "quit"
        else:
            titik = masukan.split()
            if len(titik) == 2:
                if titik[0].isdigit() and titik[1].isdigit():
                    # kedua input adalah integer
                    x = int(titik[0]) - 1
                    y = int(titik[1]) - 1
                    lokasi = cekGerakanValid(papan, giliran, x, y)
                    if lokasi != False:
                        # titik yang valid
                        valid = True
                    else:
                        print("titik tidak valid")
                else:
                    print("masukan koordinat angka")
            else:
                print("input tidak valid")
    return {"x": x, "y": y, "lokasi": lokasi}


if __name__ == "__main__":
    # main program
    papan = buatPapanKosong(DIM)
    resetPapanReversi(papan)
    giliran = HITAM
    hint = False
    while True:
        if not hint:
            cetakPapan(papan)
        else:
            cetakPapan(papanBerhint(papan, giliran))
        print("Sekarang giliran "+giliran)
        skor = hitungSkor(papan)
        print(
            f"Skor sekarang {HITAM}: {skor[HITAM]}, {PUTIH}: {skor[PUTIH]}")
        masukan = validasiMasukan(papan, giliran)
        # masukan pasti valid
        if masukan == "hint":
            hint = not hint
        elif masukan == "quit":
            break
        else:
            x = masukan["x"]
            y = masukan["y"]
            lokasi = masukan["lokasi"]
            revers(papan, giliran, lokasi, x, y)
            giliran = lawanGiliran(giliran)
