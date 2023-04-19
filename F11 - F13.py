import os
import argparse

def manappend(list, item): # manual append
    index = panjang(list) 
    list[index:index] = [item]

def removebaris(matrix, indexbaris): #menghapus baris dari matrix
    new_matrix = []
    for i in range(panjang(matrix)):
        if i != indexbaris:
            manappend(new_matrix, matrix[i]) 
    return new_matrix

def manstrip(string): # manual strip
    hasil = ""
    for char in string:
        if char != " ":
            hasil += char
    return hasil

def panjang(list): # manual len
    panjang = 0
    for elemen in list:
        panjang += 1
    return panjang

def mansplit(string, pemisah): # manual split
    hasil = []
    sub_string = ""
    for char in string:
        if char == pemisah:
            if sub_string != "":
                hasil += [sub_string]
                sub_string = ""
        else:
            sub_string += char
    if sub_string != "":
        hasil += [sub_string]
    return hasil

def removeinCSV(data: list): # menghapus dari file csv
    f = open("candi.csv", 'w')
    for row in data:
        for i, col in enumerate(row):
            f.write(str(col))
            if i != len(row) - 1:
                f.write(";")
    f.close()

#F11
def hancurkancandi(data:list):
    idCandi = int(input("Masukkan ID candi: "))
    confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {idCandi} (Y/N)?")
    print()
    found = False
    for candi in data:
        if candi[0] == idCandi:
            found = True
            break

    if found == True:
        if confirm == "Y":
            data = removebaris(data,idCandi)
            print("Candi telah berhasil dihancurkan.")
    else:
        print(f"Tidak ada candi dengan ID tersebut.")
    
    return data

#F12
def ayamberkokok(data:list):
    print("Kukuruyuk.. Kukuruyuk..")
    print()
    jmlhcandi = panjang(data) - 1 # baris pertama tidak dihitung
    print(f"Jumlah Candi : {jmlhcandi}")
    print()
    if jmlhcandi < 100 :
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print()
        print("*Bandung Bondowoso angry noise*")
        print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("Yah, Bandung Bondowoso memenangkan permainan!")

# menjalankan program F11 dan F12 secara universal
f = open("test.csv","r") 
data = [manstrip(row) for row in f] # merubah dari file menjadi matrix
f.close() 
data2 = [mansplit(row,";") for row in data]  # split matrix

# Merubah id dari string menjadi int
for i in range(1, panjang(data2)):
    data2[i][0] = int(data2[i][0])

#menjalankan program F11
data2 = hancurkancandi(data2) # menghancurkan candi
removeinCSV(data2) # menghapus dari file csv

# menjalankan program f12
ayamberkokok(data2) 

#F13
def load_data(nama_folder):
    if not os.path.isdir(nama_folder):
        print(f"Folder \"{nama_folder}\" tidak ditemukan.")
        return False

    # Melakukan proses loading data
    print("Loading...")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", nargs="?", help="Nama folder yang berisi file-file penyimpanan")
    args = parser.parse_args()

    if args.nama_folder:
        if load_data(args.nama_folder):
            print("Data telah dimuat.\n")
            print("Selamat datang di program Manajerial Candi!")
            username = input("Silakan masukkan username Anda: ")
    else:
        print("Tidak ada nama folder yang diberikan!")
        print()
        print("Usage: python main.py <nama_folder>")






























