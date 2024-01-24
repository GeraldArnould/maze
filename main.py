from ui import Line, Point, Window

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

    win.wait_for_close()

if __name__ == "__main__":
    main()
