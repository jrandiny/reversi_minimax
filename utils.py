from constant import *


def gerakanTersedia(papan, giliran):
    # Fungsi yang menghasilkan semua titik gerakan yang mungkin dilakukan pada giliran "giliran"
    tersedia = []
    for y in range(len(papan)):
        for x in range(len(papan)):
            if cekGerakanValid(papan, giliran, x, y) != False:
                tersedia.append([x, y])
    return tersedia


def copyPapan(papan):
    # Fungsi yang mengembalikan salinan dari papan masukan
    copy = buatPapanKosong(len(papan))

    for row in range(len(papan)):
        for col in range(len(papan)):
            copy[row][col] = papan[row][col]
    return copy


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
    mid = int((dim / 2) - 1)
    # menetapkan kondisi awal reversi
    papan[mid][mid] = papan[mid + 1][mid + 1] = PUTIH
    papan[mid + 1][mid] = papan[mid][mid + 1] = HITAM


def dalamPapan(x, y):
    # Fungsi untuk memeriksa apakah indeks x dan y ada dalam jangkauan papan
    return x >= 0 and x <= DIM - 1 and y >= 0 and y <= DIM - 1


def lawanGiliran(giliran):
    # Fungsi yang mengembalikan lawan dari giliran sekarang
    if giliran == HITAM:
        lawan = PUTIH
    else:
        # giliran putih
        lawan = HITAM
    return lawan
