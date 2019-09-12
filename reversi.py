# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import sys
from math import log10

DIM = 8  # dimensi global papan yang digunakan


def cetakPapan(papan):
    # prosedur untuk menampilkan kondisi papan ke layar
    # I.S. papan terdefinisi sebagai matriks persegi
    # F.S. papan tercetak di layar

    dim = len(papan)
    ORD = int(log10(dim))+1  # Ordo dari dimensi papan
    SPACE = " "*ORD  # Jumlah spasi
    GARISH = " "+SPACE+(("+--"+"-"*ORD)*(dim))+"+"  # Garis horizontal
    GARISV = " "+SPACE+(("|  "+" "*ORD)*(dim))+"|"  # Garis vertikal

    # Cetak koordinat X
    print("   ", end=SPACE)
    for i in range(dim):
        ordoI = int(log10(i+1))
        print(f"{i+1}  "+" "*(ORD-ordoI), end="")

    # Cetak Isi
    print("\n"+GARISH)
    for y in range(dim):
        print(GARISV)
        ordoY = int(log10(y+1))
        # Cetak koordinat Y
        print(y+1, end=" "*(ORD-ordoY))
        # Cetak isi papan
        for x in papan[y]:
            print(f"| {x}", end=" "*ORD)
        print("|")
        print(GARISV)
        print(GARISH)


def buatPapanKosong(dim):
    # Fungsi untuk membuat papan kosong sesuai ukuran dimensi
    return [[" "] * dim for i in range(dim)]


def resetPapanReversi(papan):
    # Prosedur untuk membuat papan yang ada menjadi papan reversi standar
    # I.S. papan terdefinisi sebagai matrik persegi dengan
    #      panjang sisi genap dan >= 2
    # F.S. papan menjadi papan reversi standar dengan x = hitam, o = putih
    #      terletak di tengah papan

    # Mengosongkan papan
    for row in papan:
        for col in row:
            col = " "
    dim = len(papan)
    mid = int((dim/2)-1)
    # Menge-set kondisi awal reversi
    papan[mid][mid] = papan[mid+1][mid+1] = "x"
    papan[mid+1][mid] = papan[mid][mid+1] = "o"


if __name__ == "__main__":
    # main program
    papan = buatPapanKosong(DIM)
    resetPapanReversi(papan)
    cetakPapan(papan)
