start, end = input("Nhập vào số đầu và số cuối : ").split()
start = int(start)
end = int(end)
if end < start or end < 5:
    print('Kiểm tra lại giá trị số đầu và số cuối')
    print('Không thể thực hiện kiểm tra đầy đủ Fizz-Buzz')
else:
    for number in range(start, end + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            continue
        elif number % 3 == 0:
            print("Fizz")
            continue
        elif number % 5 == 0:
            print("Buzz")
            continue
        else:
            print(number)
