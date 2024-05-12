from turtle import *

my_turtle = Turtle()
my_turtle.speed(0)
my_turtle.screen.setup(1200, 800)

# Нарисовать спираль
def draw_spiral(t):
    length = 1
    for _ in range(360):
        t.forward(length)
        t.right(91)  # Изменяем угол для получения спирали
        length += 1

# Рисует спираль
draw_spiral(my_turtle)

# Необходимо, чтобы окно не закрывалось само, а только по клику
my_turtle.screen.exitonclick()
my_turtle.screen.mainloop()