# NAMA : MOHAMMAD RAIYAN
# NIM: F55123001
# KELAS : A
# pseudocode untuk algortma merge sort
# MERGE-SORT(A, kiri, kana):
#     if left < right:
#         nilaiTengah = (kiri + kanan) dibagi 2
#         MERGE-SORT(A, kiri, kanan) // penggunaan rekursif
#         MERGE-SORT(A, nilaiTengah+1, kanan)
#         MERGE(A, kiri, nilaiTenagh, kanan)

# MERGE(A, left, mid, right): menggabungkan nilai setelah di divide
#     buat L = A[kiri...nilaiTengah]
#     buat R = A[nilaiTengah+1...kanan]
#     i = 0
#     j = 0
#     k = kiri
#     while i < length(L) dan j < length(R):
#         if L[i] <= R[j]:
#             A[k] = L[i]
#             i = i + 1
#         else:
#             A[k] = R[j]
#             j = j + 1
#         k = k + 1
#    untuk kompleksitas waktunya itu O(n log n). artinya n itu angka elemen. Dan saat dibagi itu arraynya menjadi 2 bagian dan kemudian di gabungkan.
#   unutk big theta nya itu 0(n log n) karena pertumbuhannya selalu sama baik best case, worst case, dan average case. 
#
#pseudocode untuk algoritma bubble sort  
# BUBBLE-SORT(A):
#     for i = 0 to length(A) - 1:
#         for j = 0 to length(A) - i - 2:
#             if A[j] > A[j+1]:
#                 ditukar(A[j], A[j+1])
#    untuk big O nya bubble sort itu O(n^2) karena pertumbuhan inputnya itu kuadratik menggunakan 2 for loop.
#    untuk big theta nya itu O(n^2) 
import random
import time
x = []
while len(x) < 100:
    x.append(random.randint(1, 100))


def merge(daftar):
    if len(daftar) > 1:
        tengah = len(daftar) // 2
        kiri = daftar[:tengah]
        kanan = daftar[tengah:]
        
        merge(kiri)
        merge(kanan)
        
        i = j = k = 0
        while i < len(kiri) and j < len(kanan):
            if kiri[i] < kanan[j]:
                daftar[k] = kiri[i]
                i += 1
            else:
                daftar[k] = kanan[j]
                j += 1
            k += 1
        
        while i < len(kiri):
            daftar[k] = kiri[i]
            i += 1
            k += 1
        
        while j < len(kanan):
            daftar[k] = kanan[j]
            j += 1
            k += 1


def bubble(daftar):
    panjang = len(daftar)
    i = 0
    while i < panjang:
        j = 0
        while j < panjang - i - 1:
            if daftar[j] > daftar[j+1]:
                daftar[j], daftar[j+1] = daftar[j+1], daftar[j]
            j += 1
        i += 1


salinan_daftar1 = x.copy()
salinan_daftar2 = x.copy()

# Pengurutan Merge Sort
waktu_mulai = time.perf_counter()
merge(salinan_daftar1)
waktu_pengurutan_merge = (time.perf_counter() - waktu_mulai) * 1000  

# Pengurutan Bubble Sort
waktu_mulai = time.perf_counter()
bubble(salinan_daftar2)
waktu_pengurutan_bubble = (time.perf_counter() - waktu_mulai) * 1000  

# Menampilkan hasil
print("Daftar Asli:", x)
print("Hasil Pengurutan Merge:", salinan_daftar1)
print("Waktu Pengurutan Merge:", waktu_pengurutan_merge, "milidetik")
print("Hasil Pengurutan Bubble:", salinan_daftar2)
print("Waktu Pengurutan Bubble:", waktu_pengurutan_bubble, "milidetik")



