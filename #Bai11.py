#Bai11
diemtrungbinh = float(input("Nhập điểm trung bình: "))
if diemtrungbinh >= 8 :
    xeploai = "Giỏi"       
elif diemtrungbinh >= 6.5 :
    xeploai = "Khá"
elif diemtrungbinh >= 5 :
    xeploai = "Trung bình"
else:
    xeploai = "Yếu"
print(f"Xếp loại học lực: {xeploai}")