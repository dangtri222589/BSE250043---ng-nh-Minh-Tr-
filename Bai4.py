#Bai4 
tong = int(input("Nhập một số: "))

print(f"Các cặp số có tổng bằng {tong}:")
for i in range(1, tong):
    print(f"{i} + {tong - i} = {tong}")

