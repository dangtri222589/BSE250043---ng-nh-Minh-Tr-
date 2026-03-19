def string_length():
    user_input = input("Nhập một chuỗi: ")
    
    if user_input == "":
        print("Lỗi: Chuỗi rỗng không được phép.")
    else:
        length = len(user_input)
        print(f"Độ dài của chuỗi là: {length}")
string_length()
