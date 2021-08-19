a = int(input("Nhập cạnh a = "))
b = int(input("Nhập cạnh b = "))
c = int(input("Nhập cạnh c = "))

if a <= 0 or b <= 0 or c <= 0: print("Đây không phải là 3 cạnh của 1 tam giác")
else:
    if a + b > c or b + c > a or a + c > b:
        print("cạnh a = {}, cạnh b = {}, cạnh c = {} tạo thành 1 tam giác".format(a, b, c))
    if a == b and a == c:
        print("Đây là 3 cạnh của tam giác đều")
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print("Đây là 3 cạnh của tam giác cân")
    elif (b**2 + c**2 == a**2) and a != c:
        print("Đây là 3 cạnh của tam giác thường")


