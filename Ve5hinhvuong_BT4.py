import turtle as t
t.pensize(2)
t.left(30)
colors = ["red", "yellow", "blue", "green", "black"]
for i in range(5):
    t.pencolor(colors[i%5])
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(72)
t.done()