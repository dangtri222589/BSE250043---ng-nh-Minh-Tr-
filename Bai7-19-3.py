def check_password():
    correct_password = "python123"
    while True:
        user_input = input("Nhập mật khẩu: ")
        if user_input == correct_password:
            print("Đúng mật khẩu!")
            break
        else:
            print("Sai mật khẩu! Vui lòng thử lại.")

check_password() 