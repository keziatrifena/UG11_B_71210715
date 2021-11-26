def check_data_type (d1,d2):
    if (type(d1) == str and d2.lower() == "str"):
        print("Jawaban Anda benar")
        return True
    elif(type(d1) == int and d2.lower() == "int"):
        print("Jawaban Anda benar")
        return True
    elif (type(d1) == int and d2.lower() == "str"):
        print("Jawaban Anda salah, seharusnya adalah int")
        return False
    else:
        print("Jawaban Anda salah, seharusnya adalah str")
        return False
        
print(check_data_type("Kevin","STr"))
print(check_data_type("Kevin","str"))
print(check_data_type(12345,"str"))
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))
