chuoi = input("Nhập nội dung: ")
x = len(chuoi)
for i in range(1, x):
    if chuoi[0:i] == chuoi[i: i + i]:
        h = x // i
        print("Lặp lại chuỗi {} số lần là {}".format(chuoi[0:i], h))
    else:
        continue
