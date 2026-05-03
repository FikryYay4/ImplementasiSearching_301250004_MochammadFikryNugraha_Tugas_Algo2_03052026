#Nama Program : Linear Search
#NIM          : 301250004
#Nama         : Mochammad Fikry Nugraha
#Tanggal Pembuatan : 03-Mei-2026
#Nama File    : LinearSearch_301250004_MochammadFikryNugraha_Tugas_Algo2_03052026.py
import random
import os
from looping_linear import linear_search

def input_data():
    # Input
    #menggunakan library random untuk mengenerate data secara acak
    jumlah = int(input("Masukkan jumlah elemen (min 20): "))
    data = random.sample(range(1, 201), jumlah)
    return data
 
def tampil_hasil(data, target, indeks):
    # Output
    print("\n===== HASIL LINEAR SEARCH =====")
    print(f"Data   : {data}")
    print(f"Target : {target}")
    if indeks != -1:
        print(f"Hasil  : Ditemukan di indeks {indeks}")
    else:
        print(f"Hasil  : Data tidak ditemukan")

def main():
    data = input_data()
    print(f"Data yang digenerate : {data}")
    target = int(input("Masukkan nilai yang dicari: "))

    # Process
    indeks = linear_search(data, target)

    tampil_hasil(data, target, indeks)

main()
console = input("Tekan Enter untuk melanjutkan...")
os.system("cls" if os.name == "nt" else "clear")