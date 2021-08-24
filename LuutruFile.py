number = int(input("Nhập dung lượng file: "))
Y = number // 4096
if number <= 4096:
    print("Dung lượng file là 4KB")
else:
    ntfs = 4 + (Y-1) * 4
    print("Dung lượng file là {} KB".format(ntfs))
