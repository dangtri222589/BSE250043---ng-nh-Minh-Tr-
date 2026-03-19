
def factorial(n): 
    if n == 0 or n == 1: 
        return 1
    else: 
        return n * factorial(n - 1)
    
number = int(input("Nhập một số: "))
result = factorial(number)
print(f"Giai thừa của {number} là: {result}")
