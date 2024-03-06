class kalkulator :
        
    def penjumlahan(self, x, y):
        hasil = x+y
        return print(f'Hasil penjumlahan dari {x} + {y}\n adalah {hasil}')
    
    def pengurangan(self, x, y):
        hasil = x - y
        return print(f'Hasil pengurangan dari {x} - {y}\n adalah {hasil}')
    
    def perkalian(self, x, y):
        hasil = x*y
        return print(f'Hasil perkalian dari {x} x {y}\n adalah {hasil}')
    
    def pembagian(self, x):
        hasil = x/y
        return print (f'Hasil Pembagian dari {x} : {y}\n adalah {hasil}')
    def pangkat(self,x):
        hasil = x*x
        return print(f'Hasil perpangkatan 2 dari {x} adalah {hasil}')
    
def main():
    kalk = kalkulator()
    while True :
        #welcome message
        print('=====================================')
        print("Selamat Datang Di Aplikasi Kalkulator")
        print("-------------------------------------")
        print('-------Silahkan Masukkan Angka-------')
        angka1 = int(input('=> Masukkan angka pertama :'))
        angka2 = int(input('=> Masukkan angka kedua :'))
        print("\n-------------------------------------")
        
        #tampilan pilihan operasi
        print("\n=====================================")
        print('=====Operasi Aplikasi Kalkulator=====')
        print('-------Silahkan Memilih Operasi------\n')
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Pangkat 2")
        print("0. Keluar")
        print("Untuk memilih operasi, anda dapat\nmemilih menggunakan nomor operasi\ncontoh: (1/2/3/4)")
        print('Jika memilih operasi perpangkatan\nmaka hanya nilai pertama yang dieksekusi')
        print("NB : Hanya boleh memilih salah satu!")
        
        #input pilihan operasi dan perkondisian pilihan
        operasi = input("\nMasukkan pilihan operasi :")
        
        if operasi == '1':
            print("\n=====================================")
            print("Anda memilih operasi penjumlahan\n\n")
            kalk.penjumlahan(angka1, angka2)
            print("-------------------------------------\n\n\n")
        
        elif operasi == '2':
            print("\n=====================================")
            print("Anda memilih operasi pengurangan\n\n")
            kalk.pengurangan(angka1, angka2)
            print("-------------------------------------\n\n\n")
            
        elif operasi == '3':
            print("\n=====================================")
            print("Anda memilih operasi perkalian\n\n")
            kalk.perkalian(angka1, angka2)
            print("-------------------------------------\n\n\n")
            
        elif operasi == '4':
            print("\n=====================================")
            print("Anda memilih operasi pembagian\n\n")
            floatAngka1 = float(angka1)
            floatAngka2 = float(angka2)
            if floatAngka2 == 0:
                
                print(f"Hasil pembagian dari {floatAngka1}:{floatAngka2}\nadalah TIdak terdefinisi")
            else:
                kalk.pembagian(floatAngka1, floatAngka2)
            print("-------------------------------------\n\n\n")
        
        elif operasi == '5':
            print("\n=====================================")
            print("Anda memilih operasi pangkat 2\n\n")
            angkaPangkat=float(input("Masukkan angka yang akan di pangkat 2 :"))
            kalk.pangkat(angkaPangkat)
        
        elif operasi == '0':
            print("\n=====================================")
            print("=======Keluar Aplikasi=======")
            print("-------------------------------------\n")
            print("Terima kasih telah menggunakan aplikasi kalkulator")
            print("Anda telah keluar aplikasi kalkulator")
            print("\n-------------------------------------\n\n\n")
            break
        
        else:
            print("\n=====================================")
            print("Pilihan tidak valid !")
            print("mohon pilih kembali, pastikan pilihan anda benar!")
            
if __name__ == "__main__":
    main()
        
        
            
        
        
        
    
        