import turtle
t = turtle.Pen()    # Pen对象
iCirclesCount = 30
for x in range(iCirclesCount):   # 循环30次
    t.circle(100)
    t.left(360/iCirclesCount)