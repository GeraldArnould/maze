import time
import random
from ui import Point
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
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
        random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        # print(f"Solved? {self.solve()}")

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        # print(f"DEBUG: visiting cell [{i}][{j}]")
        # print("DEBUG: walls")
        # print(f"DEBUG: * top: {self._cells[i][j].has_top_wall}")
        # print(f"DEBUG: * bottom: {self._cells[i][j].has_bottom_wall}")
        # print(f"DEBUG: * left: {self._cells[i][j].has_left_wall}")
        # print(f"DEBUG: * right: {self._cells[i][j].has_right_wall}")
        if i == len(self._cells) - 1 and j == len(self._cells[0]) - 1:
            return True
        if i > 0:
            src = self._cells[i][j]
            to = self._cells[i - 1][j]
            if not to.visited \
                and not to.has_right_wall \
                and not src.has_left_wall:
                src.draw_move(to)
                if self._solve_r(i - 1, j):
                    return True
                else:
                    src.draw_move(to, undo=True)
        if j > 0:
            src = self._cells[i][j]
            to = self._cells[i][j - 1]
            if not to.visited \
                and not to.has_bottom_wall \
                and not src.has_top_wall:
                src.draw_move(to)
                if self._solve_r(i, j - 1):
                    return True
                else:
                    src.draw_move(to, undo=True)
        if i < len(self._cells) - 1:
            src = self._cells[i][j]
            to = self._cells[i + 1][j]
            if not to.visited \
                and not to.has_left_wall \
                and not src.has_right_wall:
                src.draw_move(to)
                if self._solve_r(i + 1, j):
                    return True
                else:
                    src.draw_move(to, undo=True)
        if j < len(self._cells[0]) - 1:
            src = self._cells[i][j]
            to = self._cells[i][j + 1]
            if not to.visited \
                and not to.has_top_wall \
                and not src.has_bottom_wall:
                src.draw_move(to)
                if self._solve_r(i, j + 1):
                    return True
                else:
                    src.draw_move(to, undo=True)
        return False

    def _break_entrance_and_exit(self):
        maze_entrance = (0, 0)
        maze_exit = (self._num_rows - 1, self._num_cols - 1)
        self._cells[maze_entrance[1]][maze_entrance[0]].has_top_wall = False
        self._draw_cell(maze_entrance[1], maze_entrance[0])
        self._cells[maze_exit[1]][maze_exit[0]].has_bottom_wall = False
        self._draw_cell(maze_exit[1], maze_exit[0])

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            if i > 0:
                if not self._cells[i - 1][j].visited:
                    to_visit.append((i - 1, j, "left"))
            if j > 0:
                if not self._cells[i][j - 1].visited:
                    to_visit.append((i, j - 1, "top"))
            if i < len(self._cells) - 1:
                if not self._cells[i + 1][j].visited:
                    to_visit.append((i + 1, j, "right"))
            if j < len(self._cells[0]) - 1:
                if not self._cells[i][j + 1].visited:
                    to_visit.append((i, j + 1, "bottom"))
            if len(to_visit) == 0:
                # no possible path
                self._draw_cell(i, j)
                break
            else:
                direction = random.randint(0, len(to_visit) - 1)
                to = to_visit[direction]
                if to[2] == "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[to[0]][to[1]].has_right_wall = False
                elif to[2] == "top":
                    self._cells[i][j].has_top_wall = False
                    self._cells[to[0]][to[1]].has_bottom_wall = False
                elif to[2] == "right":
                    self._cells[i][j].has_right_wall = False
                    self._cells[to[0]][to[1]].has_left_wall = False
                elif to[2] == "bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[to[0]][to[1]].has_top_wall = False
                self._draw_cell(i, j)
                self._break_walls_r(to[0], to[1])

    def _reset_cells_visited(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[0])):
                self._cells[i][j].visited = False

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
                col.append(Cell(p1, p2, win=self._win))
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
        time.sleep(0.001)
