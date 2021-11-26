nama=str(input("Masukkan kalimat awal: "))
kata=input("Masukkan kata untuk disisipkan: ")
indek=int(input("Masukkan index: "))

def sisip():
    hasil= nama[:indek] + kata + nama[indek:]
    print(hasil)

sisip()