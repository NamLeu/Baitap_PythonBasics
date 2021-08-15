i = int(input("Nhập số tháng: "))
if 0 < i < 13:
    if i % 2 == 1 or i == 8 or i == 10 or i == 12:
        print('31 ngày')
    elif i == 2:
        print('28 hoặc 29 ngày')
    else:
        print('30 ngày')
else:
    print('Nhập sai tháng')