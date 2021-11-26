kal= input("Masukkan kalimat untuk dihitung: ")

def hitung(kal):
    jumlahkal=len(kal)
    return jumlahkal * 2/3
    
print(int(hitung(kal)))