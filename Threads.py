from threading import Thread

# a = 1 
# b = 2
# c = 3

# def task1(a,b):
#     print(a+b)

# def task2(a,b,c):
#     print (a + b + c) 

# t1 = Thread(target=task1,args=(a,b,))
# t2 = Thread(target=task2,args=(a,b,c,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

from threading import Thread  # Mengimpor modul Thread dari library threading untuk membuat thread

# Fungsi untuk menghitung jumlah dari 'start' hingga 'end' dan menyimpan hasilnya di 'result' pada posisi 'index'
def sums(start, end, result, index):
    total = 0  # Inisialisasi variabel total
    for i in range(start, end + 1):  # Loop dari nilai start sampai end (inklusif)
        total += i  # Menambahkan nilai i ke total
    result[index] = total  # Menyimpan hasil penjumlahan di list result pada posisi index

# Meminta input dari pengguna untuk nilai awal, akhir, dan jumlah thread
awal = int(input("Masukan nilai awal: "))  # Input nilai awal
akhir = int(input("Masukan nilai akhir: "))  # Input nilai akhir
jumlah_t = int(input("Masukan jumlah thread: "))  # Input jumlah thread

# Menghitung rentang (step) yang akan dihitung oleh setiap thread
step = (akhir - awal + 1) // jumlah_t  # Menentukan jumlah elemen yang akan diproses oleh setiap thread
threads = []  # List untuk menyimpan objek thread
result = [0] * jumlah_t  # List untuk menyimpan hasil penjumlahan tiap thread, diinisialisasi dengan 0

# Membuat dan memulai thread
for i in range(jumlah_t):  # Loop sebanyak jumlah thread
    start = awal + (i * step)  # Menentukan nilai start untuk thread ke-i
    end = awal + ((i + 1) * step - 1) if i < jumlah_t - 1 else akhir  # Menentukan nilai end untuk thread ke-i
    t = Thread(target=sums, args=(start, end, result, i))  # Membuat objek thread dengan target fungsi sums
    threads.append(t)  # Menambahkan thread ke dalam list threads
    t.start()  # Memulai eksekusi thread

# Menunggu semua thread selesai
for t in threads:  # Loop untuk setiap thread dalam list threads
    t.join()  # Menunggu thread selesai

# Menampilkan hasil dari setiap thread
for j in range(jumlah_t):  # Loop untuk menampilkan hasil dari setiap thread
    print("Thread ", j + 1, " : ", result[j])  # Menampilkan hasil penjumlahan dari thread ke-j

# Menghitung total dari semua hasil thread
hasil = sum(result)  # Menghitung total dari semua elemen dalam list result
print("Total: ", hasil)  # Menampilkan hasil total

