k = int(input("Nhập độ dài xâu chuỗi: "))
noidung = input("Nhập nội dung: ")
for i in range(0, len(noidung), k):
    new_var = list(reversed(noidung[i:(i + k)]))
    new_var_ok = ''.join(new_var)
    print(new_var_ok, end='')
