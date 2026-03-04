#Chương 3
#Bai1 
mon_hoc = ["Cơ sở lập trình ", "Đại số tuyến tính", "Triết học Mác Lê", "Lịch sử Đảng"]
print("Số lượng môn học:", len(mon_hoc))
print("Danh sách các môn học:")
for mon in mon_hoc:
    print(mon)
#bai3
mau_sac = ["Red", "Blue", "Green", "Yellow", "Pink"]

try:
    mau_sac.remove("Green")
    print("Đã xóa màu Green khỏi danh sách.")
except ValueError:
    print("Màu Green không có trong danh sách.")

print("Danh sách màu sắc hiện tại:")
for mau in mau_sac:
    print(mau)

#neu green khong co trong danh sach
mau_sac = ["Red", "Blue", "Yellow", "Pink"]

try:
    mau_sac.remove("Green")
    print("Đã xóa màu Green khỏi danh sách.")
except ValueError:
    print("Màu Green không có trong danh sách.")

print("Danh sách màu sắc hiện tại:")
for mau in mau_sac:
    print(mau)