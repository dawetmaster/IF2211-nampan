import random
from copy import deepcopy
from greedy import *

# fungsi generator barang
def buat_barang(ukuran_wadah, banyak_barang):
    # inisialisasi
    barang = []
    luas_wadah = ukuran_wadah[0] * ukuran_wadah[1]
    # buat barang, maksimum luas barang adalah setengah luas wadah dan panjang >= lebar
    jml_barang = 0
    while jml_barang < banyak_barang:
        panjang = random.randint(1, ukuran_wadah[0])
        lebar = random.randint(1, ukuran_wadah[1])
        if panjang * lebar <= luas_wadah / 2 and panjang >= lebar:
            barang.append((panjang, lebar))
            jml_barang += 1
    return barang

# fungsi penggambaran
def gambar_wadah(ukuran_wadah, petak_wadah):
    sisi_atas_bawah = "#" + "=" * ukuran_wadah[0] + "#"
    print(sisi_atas_bawah)
    for i in range(ukuran_wadah[1]):
        print("|" + "".join(petak_wadah[i]) + "|")
    print(sisi_atas_bawah)

# fungsi penyortiran, ada tiga:
# 1. penyortiran dari luas barang tertinggi
# 2. penyortiran dari sisi panjang terpanjang
# 3. penyortiran dari rasio panjang terhadap lebar tertinggi

# penyortiran dari luas barang tertinggi
def sortir_luas(daftar_barang):
    result = deepcopy(daftar_barang)
    result.sort(key=lambda x: x[0] * x[1], reverse=True)
    return result

# penyortiran dari sisi panjang terpanjang
def sortir_panjang(daftar_barang):
    result = deepcopy(daftar_barang)
    result.sort(key=lambda x: x[0], reverse=True)
    return result

# penyortiran dari rasio panjang terhadap lebar tertinggi
def sortir_rasio(daftar_barang):
    result = deepcopy(daftar_barang)
    result.sort(key=lambda x: x[0] / x[1], reverse=True)
    return result

# fungsi cek kekosongan, asumsi barang memiliki panjang >= lebar
def cek_ruang(petak_wadah, barang, posisi, orientasi):
    # init
    area_kosong = True

    if orientasi == "landscape":
        y = posisi[1]
        while (area_kosong and y < min(len(petak_wadah), posisi[1] + barang[1])):
            x = posisi[0]
            while (area_kosong and x < min(len(petak_wadah[y]), posisi[0] + barang[0])):
                area_kosong = petak_wadah[y][x] == " "
                x += 1
            y += 1

    elif orientasi == "portrait":
        y = posisi[1]
        while (area_kosong and y < min(len(petak_wadah), posisi[1] + barang[0])):
            x = posisi[0]
            while (area_kosong and x < min(len(petak_wadah[y]), posisi[0] + barang[1])):
                area_kosong = petak_wadah[y][x] == " "
                x += 1
            y += 1
        
    return area_kosong

# fungsi isi petak dengan simbol
def isi_petak(petak_wadah, barang, posisi, orientasi, simbol="*"):
    if orientasi == "landscape":
        for y in range(posisi[1], posisi[1] + barang[1]):
            for x in range(posisi[0], posisi[0] + barang[0]):
                petak_wadah[y][x] = simbol

    elif orientasi == "portrait":
        for y in range(posisi[1], posisi[1] + barang[0]):
            for x in range(posisi[0], posisi[0] + barang[1]):
                petak_wadah[y][x] = simbol
    

# DEFINISI UKURAN WADAH
# Nyatakan ukuran wadah dalam (panjang, lebar)

UKURAN_WADAH = (20, 15)
petak_wadah = [[" " for _ in range(UKURAN_WADAH[0])] for _ in range(UKURAN_WADAH[1])]

# DEFINISI BARANG
# nyatakan dimensi barang-barang dalam (panjang, lebar) dengan catatan panjang > lebar
list_barang = buat_barang(UKURAN_WADAH, 10)

# program utama
if __name__ == '__main__':
    print(list_barang)
    print(list_barang[0])
    print(sortir_panjang(list_barang))
    print(sortir_luas(list_barang))
    print(sortir_rasio(list_barang))
    gambar_wadah(UKURAN_WADAH, petak_wadah)
    petak_new, solusi = greedy_by_area(UKURAN_WADAH, list_barang)
    gambar_wadah(UKURAN_WADAH, petak_new)
    print(solusi)
    petak_new, solusi = greedy_by_ratio(UKURAN_WADAH, list_barang)
    gambar_wadah(UKURAN_WADAH, petak_new)
    print(solusi)
    petak_new, solusi = greedy_by_length(UKURAN_WADAH, list_barang)
    gambar_wadah(UKURAN_WADAH, petak_new)
    print(solusi)
