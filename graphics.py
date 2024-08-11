from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__rootWidget = Tk()
        self.__rootWidget.title("mazeSolver")
        self.__canvasWidget = Canvas(self.__rootWidget, bg="White", height=height, width=width)
        self.__canvasWidget.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__rootWidget.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, Line, color="black"):
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