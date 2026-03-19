def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

user_input = input("Nhập một chuỗi: ")
reversed_input = reverse_string(user_input)
print(f"Chuỗi sau khi đảo ngược là: {reversed_input}")