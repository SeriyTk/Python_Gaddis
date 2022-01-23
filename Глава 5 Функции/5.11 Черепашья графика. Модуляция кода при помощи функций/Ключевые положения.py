import turtle as t
from  Modules import draw_squares as d_s
def main():
    d_s.squares(100, 0, 50, 'red')
    d_s.squares(-150,-100, 200,'blue')
    d_s.squares(-200, 150, 75, 'green')


main()
t.done()