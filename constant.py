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
HINT = "*"
