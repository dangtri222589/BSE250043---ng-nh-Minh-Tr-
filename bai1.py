Height = int(input("Điền chiều cao: "))
Weight = int(input("Điền cân nặng : "))
if Weight <= 60 or Height <= 165:
    print("Chiều cao và cân nặng phải lớn hơn 60kg và 165cm.")
else:
    BMI = Weight / (Height*Height)
    print("Chỉ số BMI của bạn là: ", BMI)