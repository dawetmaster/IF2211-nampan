from wadah import *

def greedy_by_area(ukuran_wadah, list_barang):
    petak_wadah = [[" " for _ in range(ukuran_wadah[0])] for _ in range(ukuran_wadah[1])]
    solution = []
    sorted_list = sortir_luas(list_barang)
    x = 0
    y = 0
    for i in range(len(sorted_list)):
        # cek apakah barang bisa dimasukkan secara landscape
        if sorted_list[i][0] + x < len(petak_wadah[y]) and sorted_list[i][1] + y < len(petak_wadah) and cek_ruang(petak_wadah, sorted_list[i], (x, y), "landscape"):
            isi_petak(petak_wadah, sorted_list[i], (x, y), "landscape", chr(i+0x41))
            solution.append((sorted_list[i], (x, y), "landscape"))
            x += sorted_list[i][0]
        # cek apakah barang bisa dimasukkan secara portrait
        elif sorted_list[i][0] + x < len(petak_wadah[y]) and sorted_list[i][1] + y < len(petak_wadah) and cek_ruang(petak_wadah, sorted_list[i], (x, y), "portrait"):
            isi_petak(petak_wadah, sorted_list[i], (x, y), "portrait", chr(i+0x41))
            solution.append((sorted_list[i], (x, y), "portrait"))
            x += sorted_list[i][1]
        # jika tidak bisa, cek dimensi barang berikutnya jika masih ada
        elif i < len(sorted_list) - 1:
            x = 0
            panjang_berikutnya = sorted_list[i+1][0]
            while not cek_ruang(petak_wadah, (panjang_berikutnya, 1), (0, y), "landscape"):
                y += 1
    return petak_wadah, solution

def greedy_by_length(ukuran_wadah, list_barang):
    petak_wadah = [[" " for _ in range(ukuran_wadah[0])] for _ in range(ukuran_wadah[1])]
    solution = []
    sorted_list = sortir_panjang(list_barang)
    x = 0
    y = 0
    for i in range(len(sorted_list)):
        # cek apakah barang bisa dimasukkan secara landscape
        if sorted_list[i][0] + x < len(petak_wadah[y]) and sorted_list[i][1] + y < len(petak_wadah) and cek_ruang(petak_wadah, sorted_list[i], (x, y), "landscape"):
            isi_petak(petak_wadah, sorted_list[i], (x, y), "landscape", chr(i+0x41))
            solution.append((sorted_list[i], (x, y), "landscape"))
            x += sorted_list[i][0]
        # cek apakah barang bisa dimasukkan secara portrait
        elif sorted_list[i][0] + x < len(petak_wadah[y]) and sorted_list[i][1] + y < len(petak_wadah) and cek_ruang(petak_wadah, sorted_list[i], (x, y), "portrait"):
            isi_petak(petak_wadah, sorted_list[i], (x, y), "portrait", chr(i+0x41))
            solution.append((sorted_list[i], (x, y), "portrait"))
            x += sorted_list[i][1]
        # jika tidak bisa, cek dimensi barang berikutnya jika masih ada
        elif i < len(sorted_list) - 1:
            x = 0
            panjang_berikutnya = sorted_list[i+1][0]
            while not cek_ruang(petak_wadah, (panjang_berikutnya, 1), (0, y), "landscape"):
                y += 1
    return petak_wadah, solution

def greedy_by_ratio(ukuran_wadah, list_barang):
    petak_wadah = [[" " for _ in range(ukuran_wadah[0])] for _ in range(ukuran_wadah[1])]
    solution = []
    sorted_list = sortir_rasio(list_barang)
    x = 0
    y = 0
    for i in range(len(sorted_list)):
        # cek apakah barang bisa dimasukkan secara landscape
        if sorted_list[i][0] + x < len(petak_wadah[y]) and sorted_list[i][1] + y < len(petak_wadah) and cek_ruang(petak_wadah, sorted_list[i], (x, y), "landscape"):
            isi_petak(petak_wadah, sorted_list[i], (x, y), "landscape", chr(i+0x41))
            solution.append((sorted_list[i], (x, y), "landscape"))
            x += sorted_list[i][0]
        # cek apakah barang bisa dimasukkan secara portrait
        elif sorted_list[i][0] + x < len(petak_wadah[y]) and sorted_list[i][1] + y < len(petak_wadah) and cek_ruang(petak_wadah, sorted_list[i], (x, y), "portrait"):
            isi_petak(petak_wadah, sorted_list[i], (x, y), "portrait", chr(i+0x41))
            solution.append((sorted_list[i], (x, y), "portrait"))
            x += sorted_list[i][1]
        # jika tidak bisa, cek dimensi barang berikutnya jika masih ada
        elif i < len(sorted_list) - 1:
            x = 0
            panjang_berikutnya = sorted_list[i+1][0]
            while not cek_ruang(petak_wadah, (panjang_berikutnya, 1), (0, y), "landscape"):
                y += 1
    return petak_wadah, solution