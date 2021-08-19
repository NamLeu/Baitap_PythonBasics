import turtle as t
t.pensize(5)
t.pencolor("red")
index = 0
while True:
    t.forward(index)
    t.right(10)
    index += 0.1
    if index >= 10:
        break
t.done()
