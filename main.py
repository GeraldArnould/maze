from ui import Cell, Line, Point, Window

def main():
    win = Window(800, 600)

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
        cell = Cell(point1, point2)
        cell_c.append(cell)
        win.draw_cell(cell, "black")

    # draw some paths between cells
    for i in range(1, len(cell_c)):
        win.draw_path(cell_c[i - 1], cell_c[i], undo=True if i % 2 == 0 else False)

    win.wait_for_close()

if __name__ == "__main__":
    main()
