from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__rootWidget = Tk()
        self.__rootWidget.title("mazeSolver")
        self.__canvasWidget = Canvas(self.__rootWidget, bg="White", height=height, width=width)
        self.__canvasWidget.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__rootWidget.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, Line, color):
        Line.draw(self.__canvasWidget, color)
    
    def redraw(self):
        self.__rootWidget.update_idletasks()
        self.__rootWidget.update()
    
    def wait_for_close(self):
        self.__running = True
        while (self.__running):
            self.redraw()
    
    def close(self):
        self.__running = False
        
class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.__point1 = point1
        self.__point2 = point2

    def draw(self, Canvas, color):
        Canvas.create_line(self.__point1.x, self.__point1.y, self.__point2.x, self.__point2.y, fill=color, width=2)
    
class Cell:
    def __init__(self, p1, p2, window, has_left=True, has_right=True, has_top=True, has_bottom=True):
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bottom = has_bottom
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y
        self.__window = window

    def draw(self):
        if self.has_left:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x1, self.__y2)
            ln = Line(p1, p2)
            self.__window.draw_line(ln, "black")
        if self.has_top:
            p1 = Point(self.__x1, self.__y1)
            p2 = Point(self.__x2, self.__y1)
            ln = Line(p1, p2)
            self.__window.draw_line(ln, "black")
        if self.has_right:
            p1 = Point(self.__x2, self.__y1)
            p2 = Point(self.__x2, self.__y2)
            ln = Line(p1, p2)
            self.__window.draw_line(ln, "black")
        if self.has_bottom:
            p1 = Point(self.__x1, self.__y2)
            p2 = Point(self.__x2, self.__y2)
            ln = Line(p1, p2)
            self.__window.draw_line(ln, "black")