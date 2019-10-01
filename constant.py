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

SKOR_FACTOR = 10
INVALID_MOVE = (-1, -1)

# Value Position Table

TABLE_VALUE = [
    [100, -99, 50, 50, 50, 50, -99, 100],
    [-99, -99, -50, -50, -50, -50, -99, -99],
    [50, -50, 10, 10, 10, 10, -50, 50],
    [50, -50, 10, 10, 10, 10, -50, 50],
    [50, -50, 10, 10, 10, 10, -50, 50],
    [50, -50, 10, 10, 10, 10, -50, 50],
    [-99, -99, -50, -50, -50, -50, -99, -99],
    [100, -99, 50, 50, 50, 50, -99, 100],
]