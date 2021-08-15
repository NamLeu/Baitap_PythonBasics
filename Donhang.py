money = float(input("Nhập số tiền hàng (VNĐ): "))
if money<75:
    print("Không được giảm giá" )
elif 100>money>75:
    print("Được giảm giá 15%")
elif 150>money>100:
    print("Được giảm giá 25%")
else:
    print("Được giảm giá 50%")
print("Số tiền thanh toán là: " + str(money) + " VNĐ")