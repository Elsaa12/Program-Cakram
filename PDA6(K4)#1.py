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

cakram = int (input('Masukan banyak cakram: '))
def banyak_min (cakram):
    if cakram == 1:
        return 1
    else:
        return 2*banyak_min(cakram-1)+1
print(f'Banyak minimum langkah yang diperlukan untuk menyelesaikan {cakram} adalah {banyak_min(cakram)}')
       