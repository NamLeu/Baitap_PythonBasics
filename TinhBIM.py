chieucao = float(input("Nhập chiều cao: "))
cannang = float(input("Nhập cân nặng: "))
BMI = cannang / (chieucao ** 2)
print("Giá trị BMI: " + str(BMI))
if BMI > 40:
    print("Béo phì cấp độ III")
elif 35<=BMI:
    print("Béo phì cấp độ II")
elif 30<=BMI<35:
    print("Béo phì cấp độ I")
elif 25<=BMI<30:
    print("Thừa cân")
elif 18.5<=BMI<25:
    print("Bình thường")
elif 17<=BMI<18.5:
    print("Bình thường")
elif 16<=BMI<17:
    print("Bình thường")
else:
    print("Gầy cấp độ 3")