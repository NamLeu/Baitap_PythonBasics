import turtle
import random
r = random.Random()
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(0, -200)

t.speed(10)
t.pensize(10)
t.pencolor("red")
t.pendown()
t.circle(200)

t.penup()
t.speed(10)
t.shape("turtle")
t.pencolor('green')
t.goto(0, 0)

angle = random.randint(0, 360)
t.right(angle)
t.showturtle()
count = 0
while True:
    t.speed(1)

    t.forward(188)
    # Bắt rùa về vị trí ban đầu, chính giữa hộp tròn
    t.hideturtle()
    t.speed(10)
    t.goto(0, 0)
    angle = random.randint(0, 360)
    # Tạo hướng mới cho rùa chạy, thử vận may mới
    t.right(angle)
    t.showturtle()
    # Khi rùa thử đến số lần nào đó thì dừng lại
    # kết thúc chương trình bằng lệnh break
    count += 1
    if count == 10:
        break

turtle.done()