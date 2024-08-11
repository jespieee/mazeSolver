from graphics import Point, Line

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