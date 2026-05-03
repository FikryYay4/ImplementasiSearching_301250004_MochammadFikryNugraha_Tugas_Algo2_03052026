#Nama Program : Binary Search
#NIM          : 301250004
#Nama         : Mochammad Fikry Nugraha
#Tanggal Pembuatan : 03-Mei-2026
#Nama File    : BinarySearch_301250004_MochammadFikryNugraha_Tugas_Algo2_03052026.py
import os
import random
from looping_binary import binary_search

def generate_data(jumlah):
    data = []
    for i in range(jumlah):
        angka = random.randint(1, 200)
        data.append(angka)
    return data

def tampil_hasil(data, data_urut, target, indeks):
    # Output
    print("\n===== HASIL BINARY SEARCH =====")
    print(f"Data asli  : {data}")
    print(f"Data urut  : {data_urut}")
    print(f"Target     : {target}")
    if indeks != -1:
        print(f"Hasil      : Ditemukan di indeks {indeks} (data terurut)")
    else:
        print(f"Hasil      : Data tidak ditemukan")

def main():
    # Input
    jumlah = int(input("Masukkan jumlah elemen (min 20): "))
    data = generate_data(jumlah)
    print(f"Data yang digenerate : {data}")
    target = int(input("Masukkan nilai yang dicari: "))

    # Process
    data_urut = sorted(data)
    indeks = binary_search(data_urut, target)

    tampil_hasil(data, data_urut, target, indeks)

main()
console = input("Tekan Enter untuk melanjutkan...")
os.system("cls" if os.name == "nt" else "clear")