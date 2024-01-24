from ui import Point, Line

class Cell:
    def __init__(self, p1, p2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._p1 = p1
        self._p2 = p2
        self._win = win

    def draw(self, fill_color="black"):
        # do not draw if no window is attached
        if self._win == None:
            return

        # create missing top right and bottom left corners
        p3 = Point(self._p2.x, self._p1.y)
        p4 = Point(self._p1.x, self._p2.y)

        # draw the cell's walls if any
        if self.has_top_wall:
            self._win.draw_line(
				Line(self._p1, p3), fill_color
			)
        if self.has_right_wall:
            self._win.draw_line(
				Line(p3, self._p2), fill_color
			)
        if self.has_bottom_wall:
            self._win.draw_line(
				Line(self._p2, p4), fill_color
			)
        if self.has_left_wall:
            self._win.draw_line(
				Line(p4, self._p1), fill_color
        )

    def middle(self):
        return Point(
            int((self._p1.x + self._p2.x) / 2),
            int((self._p1.y + self._p2.y) / 2)
        )

    def draw_move(self, to_cell, undo=False):
        # do not draw if no window is attached
        if self._win == None:
            return

        mid_self = self.middle()
        mid_to = to_cell.middle()
        fill_color = "gray" if undo else "red"
        self._win.draw_line(
            Line(mid_self, mid_to), fill_color
        )
