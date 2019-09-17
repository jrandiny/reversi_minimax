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
TABLE_VALUE = [[40, 40, 40, 40, 40, 40, 40, 40],
               [40, 30, 30, 30, 30, 30, 30, 40],
               [40, 30, 20, 20, 20, 20, 30, 40],
               [40, 30, 20, 0, 0, 20, 30, 40], [40, 30, 20, 0, 0, 20, 30, 40],
               [40, 30, 20, 20, 20, 20, 30, 40],
               [40, 30, 30, 30, 30, 30, 30, 40],
               [40, 40, 40, 40, 40, 40, 40, 40]]
