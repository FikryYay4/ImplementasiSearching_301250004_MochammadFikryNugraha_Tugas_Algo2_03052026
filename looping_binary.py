def binary_search(data, target):
    kiri = 0
    kanan = len(data) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2

        if data[tengah] == target:
            return tengah
        elif target < data[tengah]:
            kanan = tengah - 1
        else:
            kiri = tengah + 1

    return -1