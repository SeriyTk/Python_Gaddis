import turtle as t
print(t.isdown())

if t.isdown(): print(t.penup())

if not (t.isdown()): print(t.pendown())

t.done()