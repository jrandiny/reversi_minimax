from constant import *


def getAvailableMove(board, turn):
    # Fungsi yang menghasilkan semua titik gerakan yang mungkin dilakukan pada turn "turn"
    move = []
    for y in range(len(board)):
        for x in range(len(board)):
            if len(getFlippableTile(board, turn, x, y)) != 0:
                # ada gerakan yang mungkin
                move.append([x, y])
    return move


def copyBoard(board):
    # Fungsi yang mengembalikan salinan dari board masukan
    copy = newBoard(len(board))

    for row in range(len(board)):
        for col in range(len(board)):
            copy[row][col] = board[row][col]
    return copy


def getFlippableTile(board, turn, posX, posY):
    # Fungsi untuk memeriksa apakah langkah pada posX dan posY adalah valid pada giliran "turn"
    # Mengembalikan list kosong jika tidak valid atau tile yang harus di flip jika valid
    flippableTile = []
    if validTile(posX, posY) and board[posY][posX] == EMPTY:
        # posisi di dalam board dan petak dalam keadaan kosong
        board[posY][posX] = turn  # set sementara untuk pemeriksaan
        opponent = nextTurn(turn)
        for dirX, dirY in ARAH:
            # cek pada semua arah
            x, y = posX, posY
            x += dirX
            y += dirY
            if not validTile(x, y):
                continue
            else:
                # masih dalam batas
                if board[y][x] == opponent:
                    # sebelah pertama harus opponent
                    while board[y][x] == opponent:
                        x += dirX
                        y += dirY
                        if not validTile(x, y):
                            break
                    if validTile(x, y):
                        # x,y masih dalam batas
                        if board[y][x] == turn:
                            # menemukan seberangnya
                            while (x, y) != (posX, posY):
                                # menambah semua tile yang perlu di balik
                                x -= dirX
                                y -= dirY
                                flippableTile.append([x, y])
        board[posY][posX] = EMPTY  # dikosongkan kembali

    return flippableTile


def newBoard(dim):
    # Fungsi untuk membuat papan kosong sesuai ukuran dimensi
    return [[EMPTY] * dim for i in range(dim)]


def resetBoard(board):
    # Prosedur untuk membuat board yang ada menjadi board reversi standar
    # I.S. board terdefinisi sebagai matrik persegi dengan
    #      panjang sisi genap dan >= 2
    # F.S. board menjadi board reversi standar dengan x = hitam, o = putih
    #      terletak di tengah board

    # mengosongkan board
    for row in board:
        for col in row:
            col = EMPTY
    dim = len(board)
    mid = int((dim / 2) - 1)
    # menetapkan kondisi awal reversi
    board[mid][mid] = board[mid + 1][mid + 1] = WHITE
    board[mid + 1][mid] = board[mid][mid + 1] = BLACK


def validTile(x, y):
    # Fungsi untuk memeriksa apakah indeks x dan y ada dalam jangkauan papan
    return x >= 0 and x <= DIM - 1 and y >= 0 and y <= DIM - 1


def nextTurn(turn):
    # Fungsi yang mengembalikan lawan dari turn sekarang
    if turn == BLACK:
        opponent = WHITE
    else:
        # turn putih
        opponent = BLACK
    return opponent


def makeMove(board, turn, posX, posY):
    # Prosedur yang dijalankan untuk bergerak dan dapat mengembalikan feedback
    # I.S. semua parameter terdefinisi
    # F.S. jika posX dan posY valid maka akan terjadi gerakan dan mengembalikan True
    #       jika tidak maka akan mengembalikan False

    flippableTile = getFlippableTile(board, turn, posX, posY)

    if len(flippableTile) != 0:
        # titik valid
        board[posY][posX] = turn
        for x, y in flippableTile:
            board[y][x] = turn
        turn = nextTurn(turn)
        return True
    else:
        return False


def getWinner(blackPoint, whitePoint):
    # Fungsi yang mengebalikan pemenang berdasarkan skor
    if blackPoint > whitePoint:
        # hitam menang
        return BLACK
    elif blackPoint < whitePoint:
        # putih menang
        return WHITE
    else:
        # seri
        return "draw"


# def getHintedBoard(papan, giliran):
#     # Fungsi yang mengembalikan papan dengan hint yang diberikan
#     #       bagi giliran "giliran"
#     salinan = copyBoard(papan)

#     for x, y in getAvailableMove(papan, giliran):
#         salinan[y][x] = HINT
#     return salinan


def countScore(board):
    # Fungsi yang mengembalikan skor pada board dalam map
    nHitam = nPutih = 0
    for row in board:
        for col in row:
            if col == BLACK:
                nHitam += 1
            elif col == WHITE:
                nPutih += 1
    return {BLACK: nHitam, WHITE: nPutih}


def isFinish(board, turn):
    # Fungsi yang mengembalikan nilai True jika permainan berakhir dan False jika tidak
    skor = countScore(board)
    firstMove = getAvailableMove(board, turn)
    opponent = nextTurn(turn)
    secondMove = getAvailableMove(board, opponent)
    totalPetak = len(board)**2
    if totalPetak - (skor[BLACK] + skor[WHITE]) == 0:
        # Tidak ada kotak lagi
        return True
    elif len(firstMove) == 0 and len(secondMove) == 0:
        # Tidak ada gerakan tersedia
        return True
    else:
        return False