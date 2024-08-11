from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)
    p1 = Point(10, 10)
    p2 = Point(20, 20)
    cell = Cell(p1, p2, win, True, True, True, True)
    cell.draw()
    win.wait_for_close()

main()