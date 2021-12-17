import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import os

#os.system('cls')
fname = 'produksi_minyak_mentah.csv' # membaca file csv nya
df = pd.read_csv('produksi_minyak_mentah.csv')

with open('kode_negara_lengkap.json') as fjson : # membaca file json
    kode_negara = json.load(fjson)

index_negara = dict()
z = 0
for x in df.kode_negara : # iterasi untuk membuat index dimana saja data suatu negara berada di file csv
    if x not in index_negara : 
        index_negara[x] = [z]
    else : 
        index_negara[x].append(z)
    z = z + 1

index_tahun = dict()
constant = 0
for year in df.tahun : 
    if year not in index_tahun : 
        index_tahun[year] = [constant]
    else : 
        index_tahun[year].append(constant)
    constant = constant + 1

def daftar_negara() : 
    b = list()
    for a in index_negara : 
        b.append(a)
    list_negara = list()
    for c in b : 
        for d in kode_negara : 
            if c == d['alpha-3'] : 
                list_negara.append(d['name'])
    return list_negara      

def soal_pertama(N) : 
    N = N.lower()
    N = N.split()
    c = 0
    while c < len(N) : 
        N[c] = N[c].capitalize()
        if 'Of' in N[c] or 'And' in N[c] or 'The' in N[c] or 'Da' in N[c] or 'Part' in N[c] : 
            N[c] = N[c].lower()
        elif '(' in N[c] : 
            N[c] = N[c].replace(N[c][1], N[c][1].capitalize()) 
        c = c + 1
    N = ' '.join(N)
    kode = str()
    for k in kode_negara : 
        if k['name'] == N : 
            kode = k['alpha-3']
    daftar_index = list()
    for j in index_negara : 
        if j == kode : 
            daftar_index = index_negara[kode] 
    produksi = list()
    tahun = list()
    for asd in daftar_index : 
        produksi.append(df.produksi[asd])
        tahun.append(df.tahun[asd])
    return[tahun, produksi]

def produksi_terbesar(yr) : 
    produksi_ = list()
    for i in index_tahun[yr] : 
        produksi_.append((df.produksi[i], i))
    
    terkecil = sorted(produksi_)
    index_awal_kecil = list()
    produksi_awal_kecil = list()
    kode_negara_awal_kecil = list()
    for (c, d) in terkecil : 
        kode_negara_awal_kecil.append(df.kode_negara[d])
        index_awal_kecil.append(d)
        produksi_awal_kecil.append(c)
    
    index_corrected_kecil = list()
    produksi_corrected_kecil = list()
    negara_corrected_kecil = list()
    new_code_kecil = list()
    region_kecil = list()
    sub_region_kecil = list()
    constant3_kecil = 0
    for cod in kode_negara_awal_kecil : 
        for cods in kode_negara : 
            if cod == cods['alpha-3']: 
                index_corrected_kecil.append(index_awal_kecil[constant3_kecil])
                produksi_corrected_kecil.append(produksi_awal_kecil[constant3_kecil])
                negara_corrected_kecil.append(cods['name'])
                new_code_kecil.append(cod)
                region_kecil.append(cods['region'])
                sub_region_kecil.append(cods['sub-region'])
        constant3_kecil = constant3_kecil + 1

    produksi_ = sorted(produksi_, reverse = True)
    
    index_awal = list()
    produksi_awal = list()
    kode_negara_awal = list()
    for (a,b) in produksi_ : 
        kode_negara_awal.append(df.kode_negara[b])
        index_awal.append(b)
        produksi_awal.append(a)
    
    index_corrected = list()
    produksi_corrected = list()
    negara_corrected = list()
    new_code = list()
    region = list()
    sub_region = list()
    constant3 = 0
    for code in kode_negara_awal : 
        for codes in kode_negara : 
            if code == codes['alpha-3']: 
                index_corrected.append(index_awal[constant3])
                produksi_corrected.append(produksi_awal[constant3])
                negara_corrected.append(codes['name'])
                new_code.append(code)
                region.append(codes['region'])
                sub_region.append(codes['sub-region'])
        constant3 = constant3 + 1
    return[negara_corrected, produksi_corrected, new_code, region, sub_region, negara_corrected_kecil, produksi_corrected_kecil, new_code_kecil, region_kecil, sub_region_kecil]

def produksi_kecil(yr2) : 
    konstanta = 0
    negara_baru = list()
    produksi_baru = list()
    code_baru = list()
    region_baru = list()
    subregion_baru = list()
    for produk in produksi_terbesar(yr2)[6] : 
        if produk != 0 : 
            negara_baru.append(produksi_terbesar(yr2)[5][konstanta])
            produksi_baru.append(produksi_terbesar(yr2)[6][konstanta])
            code_baru.append(produksi_terbesar(yr2)[7][konstanta])
            region_baru.append(produksi_terbesar(yr2)[8][konstanta])
            subregion_baru.append(produksi_terbesar(yr2)[9][konstanta])
        konstanta = konstanta + 1
    return[negara_baru, produksi_baru, code_baru, region_baru, subregion_baru]

def produksi_nol(yr3) : 
    konstanta = 0
    negara_baru = list()
    produksi_baru = list()
    code_baru = list()
    region_baru = list()
    subregion_baru = list()
    for produk in produksi_terbesar(yr3)[6] : 
        if produk == 0 : 
            negara_baru.append(produksi_terbesar(yr3)[5][konstanta])
            produksi_baru.append(produksi_terbesar(yr3)[6][konstanta])
            code_baru.append(produksi_terbesar(yr3)[7][konstanta])
            region_baru.append(produksi_terbesar(yr3)[8][konstanta])
            subregion_baru.append(produksi_terbesar(yr3)[9][konstanta])
        konstanta = konstanta + 1
    return[negara_baru, produksi_baru, code_baru, region_baru, subregion_baru]

def jumlah_kumulatif() : 
    v1 = dict()
    for k in index_negara :
        c1 = 0 
        for j in index_negara[k] : 
            c1 = c1 + df.produksi[j]
        v1[k] = c1
    
    v2 = list()
    for a, b in v1.items() : 
        v2.append((b, a))

    v2_kecil = sorted(v2)
    v3_negara_kecil = list()
    v4_kecil = list()
    v5_produksi_kecil = list()
    v6_region_kecil = list()
    v7_sub_region_kecil = list()
    for (c, d) in v2_kecil : 
        for g in kode_negara : 
            if d == g['alpha-3'] : 
                v3_negara_kecil.append(g['name'])
                v4_kecil.append(g['alpha-3'])
                v5_produksi_kecil.append(c)
                v6_region_kecil.append(g['region'])
                v7_sub_region_kecil.append(g['sub-region'])

    v2 = sorted(v2, reverse = True)
    v3_negara = list()
    v4 = list()
    v5_produksi = list()
    v6_region = list()
    v7_sub_region = list()
    for (q, w) in v2 : 
        for p in kode_negara : 
            if w == p['alpha-3'] : 
                v3_negara.append(p['name'])
                v4.append(p['alpha-3'])
                v5_produksi.append(q)
                v6_region.append(p['region'])
                v7_sub_region.append(p['sub-region'])
    return[v3_negara, v5_produksi, v4, v6_region, v7_sub_region, v3_negara_kecil, v5_produksi_kecil, v4_kecil, v6_region_kecil, v7_sub_region_kecil]

def kumulatif_kecil(): 
    negara_kecil = list()
    produksikecil = list()
    code_kecil = list()
    region_kecil = list()
    subregion_kecil = list()
    konstanta = 0
    for f in jumlah_kumulatif()[6] : 
        if f != 0 : 
            negara_kecil.append(jumlah_kumulatif()[5][konstanta])
            produksikecil.append(jumlah_kumulatif()[6][konstanta])
            code_kecil.append(jumlah_kumulatif()[7][konstanta])
            region_kecil.append(jumlah_kumulatif()[8][konstanta])
            subregion_kecil.append(jumlah_kumulatif()[9][konstanta])
        konstanta = konstanta + 1
    return[negara_kecil, produksikecil, code_kecil, region_kecil, subregion_kecil]
def kumulatif_nol(): 
    negara_nol = list()
    produksinol = list()
    code_nol = list()
    region_nol = list()
    subregion_nol = list()
    konstanta = 0
    for f in jumlah_kumulatif()[6] : 
        if f == 0 : 
            negara_nol.append(jumlah_kumulatif()[5][konstanta])
            produksinol.append(jumlah_kumulatif()[6][konstanta])
            code_nol.append(jumlah_kumulatif()[7][konstanta])
            region_nol.append(jumlah_kumulatif()[8][konstanta])
            subregion_nol.append(jumlah_kumulatif()[9][konstanta])
        konstanta = konstanta + 1
    return[negara_nol, produksinol, code_nol, region_nol, subregion_nol]

print('SELAMAT DATANG DI PROGRAM DATA PRODUKSI PERMINYAKAN DUNIA\n')
print('Pada program ini akan disediakan beberapa fitur, diantaranya : \n1. Daftar negara yang bisa dilihat jumlah produksinya\n2. Jumlah produksi tiap-tiap negara\n3. Jumlah kumulatif produksi tiap-tiap negara\n4. Dan lain-lain')
print('untuk lebih lengkapnya bisa di cek pada menu dibawah\n')
print('MENU')
print('1. Daftar negara yang tersedia\n2. Jumlah produksi suatu negara\n3. Negara-negara pemuncak produksi pada suatu tahun\n4. Negara-negara pemuncak produksi kumulatif\n5. Informasi negara produksi terbesar pada suatu tahun\n6. Informasi negara produksi terendah pada suatu tahun\n7. Informasi suatu negara dengan produksi nol pada suatu tahun\n8. Keluar')
print('PETUNJUK : PILIH SESUAI DENGAN NOMOR MENU, CONTOH TEKAN 1 UNTUK MENU NOMOR 1')
opsi = input('Pilihan menu : ')
while opsi != '8' : 
    if opsi == '1' : 
        os.system('cls')
        print(daftar_negara())
    elif opsi == '2' : 
        os.system('cls')
        nama = input('Masukkan nama negara yang ingin anda lihat produksinya : ')
        list_baru = list()
        for nilai in soal_pertama(nama)[1] : 
            v = nilai / 100000
            list_baru.append(v)
        fig, ax = plt.subplots()
        ax.bar(soal_pertama(nama)[0], list_baru)
        ax.set_title('Grafik Produksi (Produksi X 100000)')
        ax.set_xlabel('Tahun', fontsize = 12)
        ax.set_ylabel('Produksi', fontsize = 12)
        plt.show()
    elif opsi == '3' : 
        os.system('cls')
        yr = int(input('Masukkan tahun yang ingin dilihat datanya : '))
        cr = int(input('Jumlah negara pemuncak : '))
        konstanta = 0
        list_baru_soal2 = list()
        while konstanta < cr : 
            list_baru_soal2.append((produksi_terbesar(yr)[1][konstanta])/100000)
            konstanta = konstanta + 1
        figu, pl = plt.subplots()
        pl.bar(produksi_terbesar(yr)[0][:cr], list_baru_soal2)
        pl.set_title('Grafik Produksi (Produksi X 100000)')
        pl.set_xlabel('Negara')
        pl.set_ylabel('Produksi')
        plt.show()
    elif opsi == '4' : 
        os.system('cls')
        total = int(input('Masukkan jumlah negara pemuncak : '))
        list_baru_soal3 = list()
        konstant = 0
        while konstant < total : 
            list_baru_soal3.append((jumlah_kumulatif()[1][konstant])/1000000)
            konstant = konstant + 1
        figur, plo = plt.subplots()
        plo.bar(jumlah_kumulatif()[0][:total], list_baru_soal3)
        plo.set_title('Grafik Produksi (Produksi X 1000000)')
        plo.set_xlabel('Negara')
        plo.set_ylabel('Produksi')
        plt.show()
    elif opsi == '5' : 
        os.system('cls')
        a = int(input('Input tahun yang ingin dilihat datanya : '))
        print('Data Negara Produksi Tertinggi : ')
        print('Nama Negara = ', produksi_terbesar(a)[0][0])
        print('Jumlah Produksi = ', produksi_terbesar(a)[1][0])
        print('Kode Negara = ', produksi_terbesar(a)[2][0])
        print('Region Negara = ', produksi_terbesar(a)[3][0])
        print('Sub-Region Negara = ', produksi_terbesar(a)[4][0], '\n')
        print('Data Produksi Terbesar Secara Kumulatif : ')
        print('Nama Negara = ', jumlah_kumulatif()[0][0])
        print('Jumlah Produksi = ', jumlah_kumulatif()[1][0])
        print('Kode Negara = ', jumlah_kumulatif()[2][0])
        print('Region Negara = ', jumlah_kumulatif()[3][0])
        print('Sub-Region Negara = ', jumlah_kumulatif()[4][0])
    elif opsi == '6' : 
        os.system('cls')
        c = int(input('Input tahun yang ingin dilihat datanya : '))
        print('Nama Negara = ', produksi_kecil(c)[0][0])
        print('Jumlah Produksi = ', produksi_kecil(c)[1][0])
        print('Kode Negara = ', produksi_kecil(c)[2][0])
        print('Region Negara = ', produksi_kecil(c)[3][0])
        print('Sub-Region Negara = ', produksi_kecil(c)[4][0], '\n')
        print('Data Produksi Terkecil Secara Kumulatif : ')
        print('Nama Negara = ', kumulatif_kecil()[0][0])
        print('Jumlah Produksi = ', kumulatif_kecil()[1][0])
        print('Kode Negara = ', kumulatif_kecil()[2][0])
        print('Region Negara = ', kumulatif_kecil()[3][0])
        print('Sub-Region Negara = ', kumulatif_kecil()[4][0])
    elif opsi == '7'  :
        os.system('cls')
        d = int(input('Input tahun yang ingin dilihat datanya : '))
        print('Nama Negara = ', produksi_nol(d)[0][0])
        print('Jumlah Produksi = ', produksi_nol(d)[1][0])
        print('Kode Negara = ', produksi_nol(d)[2][0])
        print('Region Negara = ', produksi_nol(d)[3][0])
        print('Sub-Region Negara = ', produksi_nol(d)[4][0], '\n')
        print('Data Jumlah Produksi nol secara kumulatif : ')
        print('Nama Negara = ', kumulatif_nol()[0][0])
        print('Jumlah Produksi = ', kumulatif_nol()[1][0])
        print('Kode Negara = ', kumulatif_nol()[2][0])
        print('Region Negara = ', kumulatif_nol()[3][0])
        print('Sub-Region Negara = ', kumulatif_nol()[4][0])
    else : 
        os.system('cls')
        print('Pilihan menu yang anda pilih tidak tersedia')
        print('Silakan input dengan benar sesuai dengan nomor pada menu')
    print('MENU')
    print('1. Daftar negara yang tersedia\n2. Jumlah produksi suatu negara\n3. Negara-negara pemuncak produksi pada suatu tahun\n4. Negara-negara pemuncak produksi kumulatif\n5. Informasi negara produksi terbesar pada suatu tahun\n6. Informasi negara produksi terendah pada suatu tahun\n7. Informasi suatu negara dengan produksi nol pada suatu tahun\n8. Keluar')
    print('PETUNJUK : PILIH SESUAI DENGAN NOMOR MENU, CONTOH TEKAN 1 UNTUK MENU NOMOR 1')
    opsi = input('Pilihan menu : ')

print('----------')
print('----------')
print('----------')    
print('TERIMA KASIH TELAH MENCOBA PROGRAM SAYA')

