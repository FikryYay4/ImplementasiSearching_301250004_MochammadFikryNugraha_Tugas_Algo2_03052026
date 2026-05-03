#Nama Program : Perbandingan Langkah
#NIM          : 301250004
#Nama         : Mochammad Fikry Nugraha
#Tanggal Pembuatan : 03-Mei-2026
#Nama File    : PerbandinganLangkah_301250004_MochammadFikryNugraha_Tugas_Algo2_03052026.py
import random
from looping_linear import linear_search
from looping_binary import binary_search

def generate_data(jumlah):
    data = []
    for i in range(jumlah):
        angka = random.randint(1, 200)
        data.append(angka)
    return data

def hitung_langkah_linear(data, target):
    langkah = 0
    for i in range(len(data)):
        langkah += 1
        if data[i] == target:
            return i, langkah
    return -1, langkah

def hitung_langkah_binary(data, target):
    kiri = 0
    kanan = len(data) - 1
    langkah = 0

    while kiri <= kanan:
        langkah += 1
        tengah = (kiri + kanan) // 2
        if data[tengah] == target:
            return tengah, langkah
        elif target < data[tengah]:
            kanan = tengah - 1
        else:
            kiri = tengah + 1

    return -1, langkah

def tampil_perbandingan(data, data_urut, target, hasil_linear, hasil_binary):
    # Output
    indeks_l, langkah_l = hasil_linear
    indeks_b, langkah_b = hasil_binary

    print("\n========================================")
    print("   PERBANDINGAN LINEAR vs BINARY SEARCH")
    print("========================================")
    print(f"Data asli : {data}")
    print(f"Data urut : {data_urut}")
    print(f"Target    : {target}")
    print("----------------------------------------")
    print(f"{'':20} {'Linear':>10} {'Binary':>10}")
    print(f"{'Jumlah Langkah':20} {langkah_l:>10} {langkah_b:>10}")

    hasil_l = f"indeks {indeks_l}" if indeks_l != -1 else "tidak ada"
    hasil_b = f"indeks {indeks_b}" if indeks_b != -1 else "tidak ada"
    print(f"{'Hasil':20} {hasil_l:>10} {hasil_b:>10}")
    print("----------------------------------------")

    selisih = langkah_l - langkah_b
    if selisih > 0:
        print(f"Binary Search lebih efisien {selisih} langkah.")
    elif selisih < 0:
        print(f"Linear Search lebih efisien {abs(selisih)} langkah.")
    else:
        print("Keduanya membutuhkan langkah yang sama.")

def main():
    # Input
    jumlah = int(input("Masukkan jumlah elemen (min 20): "))
    data = generate_data(jumlah)
    print(f"Data yang digenerate : {data}")
    target = int(input("Masukkan nilai yang dicari: "))

    # Process
    data_urut = sorted(data)
    hasil_linear = hitung_langkah_linear(data, target)
    hasil_binary = hitung_langkah_binary(data_urut, target)

    tampil_perbandingan(data, data_urut, target, hasil_linear, hasil_binary)

main()