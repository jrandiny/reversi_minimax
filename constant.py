DIM = 8  # dimensi global papan yang digunakan
BLACK = "x"  # konstan yang melambangkan hitam, jalan pertama
WHITE = "o"  # konstan yang melambangkan putih
EMPTY = " "  # konstan yang melambangkan petka kosong
ARAH = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0],
        [-1, -1]]  # arah yang dicek dari sebuah posisi
'''
    -1,-1   0,-1    1,-1
    -1, 0   0, 0    1, 0
    -1, 1   0, 1    1, 1
'''
HINT = "*"  # konstan untuk melambangkan hint

# masukan yang valid
HINTKEY = ["hint", "h"]
QUITKEY = ["quit", "q", "x"]

#Value Position Table
TABLE_VALUE = [[100, 52, 46, 38, 38, 46, 52, 100],
               [52, 52, 26, 18, 18, 26, 52, 52],
               [46, 26, 26, 10, 10, 26, 26, 46],
               [38, 18, 10, 10, 10, 10, 18, 38],
               [38, 18, 10, 10, 10, 10, 18, 38],
               [46, 26, 26, 10, 10, 26, 26, 46],
               [52, 52, 26, 18, 18, 26, 52, 52],
               [100, 52, 46, 38, 38, 46, 52, 100]]
# TABLE_VALUE = [[0] * DIM for x in range(DIM)]
# TABLE_VALUE = [[19, 15, 13, 19, 22, 30, 25, 31],
#                [18, 27, 30, 30, 29, 30, 22, 19],
#                [36, 30, 24, 14, 31, 22, 44, 31], [44, 27, 37, 0, 0, 8, 19, 32],
#                [31, 30, 32, 0, 0, 32, 30, 38], [35, 24, 29, 19, 56, 5, 46, 27],
#                [34, 28, 43, 22, 33, 34, 14, 29],
#                [41, 10, 47, 15, 51, 10, 40, 38]]
# TABLE_VALUE = [[17, 11, 7, 16, 20, 25, 19,
#                 25], [13, 24, 28, 29, 26, 25, 19, 15],
#                [31, 28, 17, 7, 24, 18, 36, 29], [40, 23, 28, 0, 0, 8, 17, 25],
#                [27, 27, 30, 0, 0, 26, 25, 33], [27, 17, 24, 16, 47, 5, 37, 23],
#                [29, 20, 36, 20, 28, 30, 14, 24],
#                [37, 9, 40, 10, 44, 5, 32, 37]]
SKOR_FACTOR = 10
INVALID_MOVE = (-1, -1)
