# Tugas Besar Intelegensi Buatan #1
# Tanggal   : Kamis, 12 Sept 2019
# Deskripsi : back engine reversi
# Support   : Python reversi engine module, command base
# Interface : gtk

import random
from math import log10
from constant import *
from utils import *
from player.random_bot import RandomBot
from player.human_player import HumanPlayer


def cetakPapan(papan):
    # Prosedur untuk menampilkan kondisi papan ke layar
    # I.S. papan terdefinisi sebagai matriks persegi
    # F.S. papan tercetak di layar

    dim = len(papan)
    ORD = int(log10(dim)) + 1  # ordo dari dimensi papan
    SPACE = " " * ORD  # jumlah spasi
    GARISH = " " + SPACE + (("+--" + "-" * ORD) *
                            (dim)) + "+"  # garis horizontal
    GARISV = " " + SPACE + (("|  " + " " * ORD) *
                            (dim)) + "|"  # garis vertikal
    offset = int(1 + (ORD / 2))  # offset karakter dari border
    tail = (2 + ORD) - (offset + 1)  # jumlah spasi di belakang karakter

    # cetak koordinat X
    print("   ", end=SPACE)
    for i in range(dim):
        ordoI = int(log10(i + 1))
        print(f"{i+1}  " + " " * (ORD - ordoI), end="")

    # cetak Isi
    print("\n" + GARISH)
    for y in range(dim):
        print(GARISV)
        ordoY = int(log10(y + 1))
        # cetak koordinat Y
        print(y + 1, end=" " * (ORD - ordoY))
        # cetak isi papan
        for x in papan[y]:
            print("|" + " " * offset + x, end=" " * tail)
        print("|")
        print(GARISV)
        print(GARISH)


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


def isFinish(papan, giliran):
    # Fungsi yang mengembalikan nilai True jika permainan berakhir dan False jika tidak
    skor = hitungSkor(papan)
    gerakan = gerakanTersedia(papan, giliran)
    totalPetak = len(papan)**2
    if totalPetak - (skor[HITAM] + skor[PUTIH]) == 0:
        # tidak kotak lagi
        return True
    elif len(gerakan) == 0:
        # tidak ada gerakan tersedia
        return True
    else:
        return False


def cetakSkor(nHitam, nPutih):
    # Prosedur untuk mencetak skor sekarang ke layar
    # I.S. skor terdefinisi
    # F.S. skor tercetak ke layar sesuai kondisi papan
    print(f"Skor sekarang {HITAM}: {nHitam}, {PUTIH}: {nPutih}")


def tentukanPemenang(nHitam, nPutih):
    # Fungsi yang mengebalikan pemenang berdasarkan skor
    if nHitam > nPutih:
        # hitam menang
        return HITAM
    elif nHitam < nPutih:
        # putih menang
        return PUTIH
    else:
        # seri
        return "draw"


def bergerak(papan, giliran, posX, posY, lokasi):
    # Prosedur yang dijalankan untuk bergerak
    # I.S. semua parameter terdefinisi, posX posY adalah lokasi yang valid
    # F.S. terjadi gerakan di posX posY, jika permainan berakhir kembalikan feedback false
    #       jika tidak kembalikan feedback true
    revers(papan, giliran, lokasi, posX, posY)
    giliran = lawanGiliran(giliran)
    if isFinish(papan, giliran):
        return False
    else:
        return True


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


def gerakanRandom(papan, giliran):
    # Prosedur untuk melakukan gerakan random pada giliran "giliran"
    # I.S. papan dan giliran terdefinisi
    # F.S. dilakukan gerakan random pada papan
    gerakan = gerakanTersedia(papan, giliran)
    random.shuffle(gerakan)
    terpilih = gerakan[0]
    x = terpilih[0]
    y = terpilih[1]
    lokasi = cekGerakanValid(papan, giliran, x, y)
    print(f"bot bergerak [{masukan['x']+1},{masukan['y']+1}]")
    return {"x": x, "y": y, "lokasi": lokasi}


if __name__ == "__main__":
    # main program
    papan = buatPapanKosong(DIM)
    resetPapanReversi(papan)
    giliran = HITAM
    hint = False
    play = True
    turn = 1  # menyatakan giliran sekarang
    # players = [RandomBot, HumanPlayer]
    players = [gerakanRandom, validasiMasukan]
    while play:
        print()
        if not hint:
            cetakPapan(papan)
        else:
            cetakPapan(papanBerhint(papan, giliran))
        print("Sekarang giliran " + giliran)
        skor = hitungSkor(papan)
        cetakSkor(skor[HITAM], skor[PUTIH])

        # turn ganjil = player
        masukan = players[turn % 2](papan, giliran)

        if not bergerak(papan, giliran, masukan["x"], masukan["y"],
                        masukan["lokasi"]):
            # permainan selesai
            play = False
        else:
            giliran = lawanGiliran(giliran)
            turn += 1

    if masukan != "quit":
        print("\npermainan berkahir")
        cetakPapan(papan)
        skor = hitungSkor(papan)
        cetakSkor(skor[HITAM], skor[PUTIH])
        pemenang = tentukanPemenang(skor[HITAM], skor[PUTIH])
        if pemenang == "draw":
            print("hasilnya draw")
        else:
            print("pemenangnya adalah " + pemenang)
    print("Terimakasih terlah bermain")
