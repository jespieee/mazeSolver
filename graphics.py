from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__rootWidget = Tk()
        self.__rootWidget.title("mazeSolver")
        self.__canvasWidget = Canvas(self.__rootWidget, bg="White", height=height, width=width)
        self.__canvasWidget.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__rootWidget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__rootWidget.update_idletasks()
        self.__rootWidget.update()
    
    def wait_for_close(self):
        self.__running = True
        while (self.__running):
            self.redraw()
    
    def close(self):
        self.__running = False
        
