from maze import Maze
from ui import Line, Point, Window
from cell import Cell

def main():
    win = Window(800, 600)

    # test_draw_lines(win)
    # test_draw_cells(win)
    # test_draw_paths(win)
    m1 = test_draw_maze(win, cols=35, rows=50)
    if m1.solve():
        print("Maze solved!")
    else:
        print("Could not find a solution")


    win.wait_for_close()

def test_draw_lines(win):
    # DEBUG: Draw some lines
    lines = [
        [(0, 0), (8, 7)],
        [(1, 5), (8, 2)],
        [(1, 5), (8, 5)],
        [(1, 7), (8, 4)],
        [(8, 2), (8, 4)],
    ]
    # scale points values to show something in the window
    scaling = 75

    for line in lines:
        p1 = Point(line[0][0] * scaling, line[0][1] * scaling)
        p2 = Point(line[1][0] * scaling, line[1][1] * scaling)
        l = Line(p1, p2)
        win.draw_line(l, "black")

def test_draw_cells(win):
    # DEBUG: Draw some cells
    cells = [
        [(1, 0), (2, 1)],
        [(2, 1), (3, 2)],
        [(0, 2), (1, 3)],
        [(1, 2), (2, 3)],
        [(2, 2), (3, 3)],
    ]
    # scale points values to show something in the window
    scaling = 75
    # avoid starting drawing at (0, 0)
    margin = 10
    # holds the created cells for further drawing later
    cell_c = []

    for (p1, p2) in cells:
        point1 = Point(margin + p1[0] * scaling, margin + p1[1] * scaling)
        point2 = Point(margin + p2[0] * scaling, margin + p2[1] * scaling)
        cell = Cell(point1, point2, win)
        cell_c.append(cell)
        cell.draw(fill_color="black")

    return cell_c

def test_draw_paths(win):
    cells = test_draw_cells(win)
    # draw some paths between cells
    for i in range(1, len(cells)):
        cells[i - 1].draw_move(cells[i], undo=True if i % 2 == 0 else False)

def test_draw_maze(win, cols=10, rows=20):
    return Maze(10, 10, rows, cols, 20, 20, win)

if __name__ == "__main__":
    main()
