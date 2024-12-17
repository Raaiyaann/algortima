from datetime import datetime

# Fungsi Insertion Sort untuk mengurutkan barang berdasarkan tanggal kedaluwarsa
def insertion_sort(items):
    n = len(items)
    for i in range(1, n):
        key = items[i]
        j = i - 1
        # Bandingkan tanggal kedaluwarsa
        while j >= 0 and items[j]['expiry_date'] > key['expiry_date']:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

# Fungsi Brute Force untuk mencari barang expired
def find_expired_items(items, today):
    expired_items = []
    for item in items:
        if item['expiry_date'] < today:
            expired_items.append(item)
    return expired_items

# Data contoh barang
products = [
    {"name": "Susu UHT", "expiry_date": datetime(2024, 6, 1)},
    {"name": "Roti Tawar", "expiry_date": datetime(2024, 5, 15)},
    {"name": "Yogurt", "expiry_date": datetime(2024, 6, 25)},
    {"name": "Telur", "expiry_date": datetime(2024, 5, 20)},
    {"name": "Keju", "expiry_date": datetime(2024, 5, 10)},
]

# Tanggal hari ini (misalkan hari ini adalah 2024-06-01)
today_date = datetime(2024, 6, 1)

# Urutkan produk berdasarkan tanggal kedaluwarsa menggunakan Insertion Sort
print("Sebelum diurutkan:")
for product in products:
    print(f"{product['name']} - {product['expiry_date'].strftime('%Y-%m-%d')}")

insertion_sort(products)

print("\nSetelah diurutkan berdasarkan tanggal kedaluwarsa:")
for product in products:
    print(f"{product['name']} - {product['expiry_date'].strftime('%Y-%m-%d')}")

# Cari barang yang sudah expired menggunakan Brute Force
expired_products = find_expired_items(products, today_date)

print("\nBarang yang sudah expired:")
if expired_products:
    for product in expired_products:
        print(f"{product['name']} - Kedaluwarsa pada {product['expiry_date'].strftime('%Y-%m-%d')}")
else:
    print("Tidak ada barang yang expired.")
