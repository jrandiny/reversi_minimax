# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import sys
from math import log10

DIM = 8  # dimensi global papan yang digunakan
HITAM = "x"  # konstan yang melambangkan hitam, jalan pertama
PUTIH = "o"  # konstan yang melambangkan putih
KOSONG = " "  # konstan yang melambangkan petka kosong
ARAH = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1],
        [-1, 0], [-1, -1]]  # arah yang dicek dari sebuah posisi
'''
    -1,-1   0,-1    1,-1
    -1, 0   0, 0    1, 0
    -1, 1   0, 1    1, 1
'''


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


def negasiGiliran(giliran):
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
        lawan = negasiGiliran(giliran)
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
    lawan = negasiGiliran(giliran)
    papan[posY][posX] = giliran
    for akhirX, akhirY in lokasi:
        x, y = posX, posY
        arahX = int(akhirX - posX)
        arahY = int(akhirY - posY)
        # print(arahX, " ", arahY)
        if arahX != 0:
            arahX //= abs(arahX)
        if arahY != 0:
            arahY //= abs(arahY)
        # print(arahX, " ", arahY)
        x += arahX
        y += arahY
        # print(x, " ", y)
        while papan[y][x] == lawan:
            papan[y][x] = giliran
            x += arahX
            y += arahY


if __name__ == "__main__":
    # main program
    papan = buatPapanKosong(DIM)
    resetPapanReversi(papan)
    giliran = HITAM
    # print(papan)
    while True:
        cetakPapan(papan)
        print("Sekarang giliran "+giliran)
        langkah = input("langkah: ").split()
        x = int(langkah[0])-1
        y = int(langkah[1])-1
        # print(f"x: {x},y: {y}")
        lokasi = cekGerakanValid(papan, giliran, x, y)
        if lokasi != False:
            print(lokasi)
            revers(papan, giliran, lokasi, x, y)
        else:
            print("tidak valid")
        # cetakPapan(papan)
        giliran = negasiGiliran(giliran)
