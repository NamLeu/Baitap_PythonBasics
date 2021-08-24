chuoi = input("Nhập chuỗi: ")
i = len(chuoi) // 2
if len(chuoi) % 2 == 0:
    new_var = list(reversed(chuoi[i:len(chuoi)]))
    new_var_ok = ''.join(new_var)
else:
    new_var = list(reversed(chuoi[i+1:len(chuoi)]))
    new_var_ok = ''.join(new_var)
if chuoi[:i] == new_var_ok:
    print("Đây là chuỗi đối xứng")
else:
    print("Đây là chuỗi không đối xứng")
