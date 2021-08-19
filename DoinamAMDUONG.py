
Can = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
Chi = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', ' Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi']
Nam = int(input("Nhập năm dương = "))
i = Nam % 10
j = Nam % 12
print('Đây là năm {} {}'.format(Can[i], Chi[j]))