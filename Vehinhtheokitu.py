char = input('Nhập kí tự cần in?: ')
width = int(input('Nhập chiều rộng?: '))
height = int(input('Nhập chiều cao?: '))
#
# for i in range(1, height + 1):
#     print_str = '     '
#     for j in range(1, width + 1):
#         if i == 1 or i == height:
#             print_str += char
#         else:
#             if j == 1 or j == width:
#                 print_str += char
#             else:
#                 print_str += ' '
#     print(print_str)
dem = len(char)
for i in range(1, height + 1):
    if i == 1 or i == height:
        print(str(char * width))
    else:
        x = " " * dem * (width-2)
        print(char + str(x) + char)

