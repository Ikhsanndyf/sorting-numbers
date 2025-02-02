import os

# Dapatkan direktori dari file script yang sedang dijalankan
script_dir = os.path.dirname(os.path.abspath(__file__))


def tukar(data, i, j):
    """
    Menukar dua angka dalam array.
    
    Parameters:
        data (list): List angka yang akan diubah.
        i (int): Indeks pertama.
        j (int): Indeks kedua.
    """
    data[i], data[j] = data[j], data[i]


def bubble_sort(data):
    """
    Mengurutkan list angka menggunakan metode Bubble Sort secara ascending.
    
    Parameters:
        data (list): List angka yang akan diurutkan.
    
    Returns:
        list: List angka yang sudah diurutkan secara ascending.
    """
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:  # Jika elemen saat ini lebih besar dari yang berikutnya, tukar
                tukar(data, j, j + 1)
    return data


def simpan_ke_file(data, filename="sorted_numbers.txt"):
    """
    Menyimpan angka yang sudah diurutkan ke dalam file.
    
    Parameters:
        data (list): List angka yang sudah diurutkan.
        filename (str): Nama file tempat angka akan disimpan. Default: "sorted_numbers.txt".
    """
    file_path = os.path.join(script_dir, filename)
    with open(file_path, "w") as file:
        file.write(",".join(map(str, data)))  # Simpan angka dalam format CSV
    print("\nData telah disimpan ke dalam file:", file_path)


def baca_dari_file(filename="sorted_numbers.txt"):
    """
    Membaca angka yang tersimpan dalam file.
    
    Parameters:
        filename (str): Nama file tempat angka tersimpan. Default: "sorted_numbers.txt".
    
    Returns:
        list: List angka yang sudah diurutkan atau list kosong jika file tidak ditemukan atau kosong.
    """
    file_path = os.path.join(script_dir, filename)
    if not os.path.exists(file_path):
        print("\nFile tidak ditemukan. Silakan input angka terlebih dahulu.")
        return []
    
    with open(file_path, "r") as file:
        content = file.read()
        return list(map(int, content.split(","))) if content.strip() else []


def tampilkan_menu():
    """
    Menampilkan menu utama untuk mengelola pilihan pengguna.
    """
    while True:
        print("\nMENU PILIHAN")
        print("1. Input angka")
        print("2. Tampil hasil pengurutan")
        print("3. Selesai")

        pilihan = input("Masukkan pilihan [1/2/3]: ")

        if pilihan == "1":
            jumlah = int(input("\nMasukkan jumlah angka yang akan diinput: "))
            angka = [int(input(f"Angka {i + 1}: ")) for i in range(jumlah)]
            angka_terurut = bubble_sort(angka)
            simpan_ke_file(angka_terurut)
        
        elif pilihan == "2":
            angka_terurut = baca_dari_file()
            if angka_terurut:
                print("\nTAMPIL HASIL PENGURUTAN")
                print("Nilai tugas:", ", ".join(map(str, angka_terurut)))
        
        elif pilihan == "3":
            print("Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    tampilkan_menu()
