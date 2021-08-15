day = ("Monday", "Tuesday", "Wednesday", "Friday", "Thusday", "Saturday", "Sunday")
i = int(input("Nhập số ngày: "))
if i>1 and i<9:
      print(day[i-2])
else:
      print("Nhập sai số ngày")