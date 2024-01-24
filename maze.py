import time
from ui import Point
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        if num_rows <= 0:
            raise Exception(f"cannot create a maze with {num_rows} row(s)")
        else:
            self._num_rows = num_rows
        if num_cols <= 0:
            raise Exception(f"cannot create a maze with {num_cols} column(s)")
        else:
            self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                # Top left corner
                p1 = Point(
                    self._x1 + i * self._cell_size_x,
                    self._y1 + j * self._cell_size_y
                )
                # Bottom right corner
                p2 = Point(
                    self._x1 + (i + 1) * self._cell_size_x,
                    self._y1 + (j + 1) * self._cell_size_y
                )
                col.append(Cell(p1, p2, self._win))
            self._cells.append(col)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        # do not draw if no window is attached
        if self._win == None:
            return

        # i = column, j = row
        p1 = Point(
            self._x1 + i * self._cell_size_x,
            self._y1 + j * self._cell_size_y
        )
        p2 = Point(
            self._x1 + (i + 1) * self._cell_size_x,
            self._y1 + (j + 1) * self._cell_size_y
        )
        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        # do not draw if no window is attached
        if self._win == None:
            return

        self._win.redraw()
        time.sleep(0.01)
