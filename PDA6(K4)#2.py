'''
    Nama  : Elsa Aiziyah
    Kelas : Matematika E
    NIM   : 21305144025
    
    TUGAS PDA#6 
    KEGIATAN #4
'''
#===========PROGRAM NOMOR 2============#
print('='*50)
print('PROGRAM CAKRAM'.center(50))
print('='*50)

#kesalahan pada saat proses

# perbaikan
langkah = 0
def hanoi ( n, asal, tujuan, antara):
    global langkah
    if n == 1:
        langkah+=1
        print (f'{langkah}. Pindahkan cakram {n} dari tiang {asal} ke tiang {tujuan}')
    else:
        hanoi (n-1, asal, antara, tujuan)
        langkah +=1
        print (f'{langkah}. Pindahkan cakram {n} dari tiang {asal} ke tiang {tujuan}')
        hanoi (n-1, antara, tujuan, asal)
hanoi(3, 'A', 'C', 'B')        
print(f'Banyak langkah yang dibutuhkan adalah {langkah}')