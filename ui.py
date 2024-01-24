from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def draw_line(self, l, fill_color):
        l.draw(self.__canvas, fill_color)

    def draw_cell(self, cell, fill_color):
        cell.draw(self.__canvas, fill_color)

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)

class Cell:
    def __init__(self, p1, p2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._p1 = p1
        self._p2 = p2

    def draw(self, canvas, fill_color):
        # create missing top right and bottom left corners
        p3 = Point(self._p2.x, self._p1.y)
        p4 = Point(self._p1.x, self._p2.y)

        # draw the cell's walls if any
        if self.has_top_wall:
            Line(self._p1, p3).draw(canvas, fill_color)
        if self.has_right_wall:
            Line(p3, self._p2).draw(canvas, fill_color)
        if self.has_bottom_wall:
            Line(self._p2, p4).draw(canvas, fill_color)
        if self.has_left_wall:
            Line(p4, self._p1).draw(canvas, fill_color)
