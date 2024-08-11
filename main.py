from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    p1 = Point(0, 500)
    p2 = Point(50, 50)
    ln1 = Line(p1, p2)
    win.draw_line(ln1,"blue")
    win.wait_for_close()

main()