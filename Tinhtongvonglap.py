a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
if a > b:
    print("Số đầu lớn hơn số cuối")
else:
    sum = 0
    i = a
    while i <= b:
        sum += i
        i += 1
    print(sum)

# sum = (a + b) * (b - a + 1) / 2

#for i in range(a, b+1):
#    tong += i
#    print(str(tong))