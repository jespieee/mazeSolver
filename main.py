from graphics import Window, Line, Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    p1 = Point(10, 10)
    p2 = Point(20, 20)
    cell1 = Cell(win)
    cell1.draw(p1.x, p1.y, p2.x, p2.y)

    p3 = Point(50, 50)
    p4 = Point(60, 60)
    cell2 = Cell(win)
    cell2.draw(p3.x, p3.y, p4.x, p4.y)
    cell1.draw_move(cell2, True)

    maze = Maze(200, 500, 5, 5, 10, 10, win)
    win.wait_for_close()

main()