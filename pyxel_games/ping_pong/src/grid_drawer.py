import pyxel


WINDOW_WIDTH = 255
WINDOW_HEIGHT = 255

AXIS_ROOT_X = WINDOW_WIDTH / 2
AXIS_ROOT_Y = WINDOW_HEIGHT / 2


def clear_screen():
    pyxel.cls(7)


def draw_point(x, y, color=8):
    true_x = AXIS_ROOT_X + x
    true_y = AXIS_ROOT_Y - y
    pyxel.circ(
        true_x,
        true_y,
        r=1,
        col=color,
    )


def draw_x_line(x1, x2, y, color=11):
    min_x = min([x1, x2])
    max_x = max([x1, x2])
    for x in range(min_x, max_x + 1):
        draw_point(x, y, color=color)


def draw_y_line(y1, y2, x, color=11):
    min_y = min([y1, y2])
    max_y = max([y1, y2])
    for y in range(min_y, max_y + 1):
        draw_point(x, y, color=color)


def draw_line(x1, y1, x2, y2, color=11):
    x_diff = x2 - x1
    y_diff = y2 - y1
    d = (x_diff ** 2 + y_diff ** 2) ** 0.5
    for step in range(int(d)):
        draw_point(
            x=x1 + (x_diff / d) * step,
            y=y1 + (y_diff / d) * step,
            color=color,
        )


def draw_line_2(x1, y1, x2, y2, color=11):
    m = (y2 - y1) / (x2 - x1)

    def y(x):
        return m * (x - x1) + y1

    min_x = min([x1, x2])
    max_x = max([x1, x2])

    for x in range(min_x, max_x+1):
        draw_point(
            x=x,
            y=y(x),
            color=color,
        )


def draw_polynom(x_range, f):
    for x in x_range:
        y = f(x)
        draw_point(x, y)


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


def draw():
    clear_screen()

    draw_x_line(
        x1=-WINDOW_WIDTH,
        x2=WINDOW_WIDTH,
        y=0,
    )
    draw_y_line(
        y1=WINDOW_HEIGHT,
        y2=-WINDOW_HEIGHT,
        x=0,
    )

    """
    draw_point(x=0, y=0)
    draw_point(x=100, y=0)
    draw_point(x=100, y=10)

    draw_line(
        x1=-10,
        y1=-10,
        x2=30,
        y2=60,
        color=14,
    )
    draw_line_2(
        x1=-10,
        y1=10,
        x2=30,
        y2=80,
        color=14,
    )
    draw_line(
        x1=0,
        y1=0,
        x2=-AXIS_ROOT_X+pyxel.mouse_x,
        y2=AXIS_ROOT_Y-pyxel.mouse_y,
        color=12,
    )
    """
    draw_polynom(range(-20, 20), parabula1)


def parabula1(x):
    return x ** 2 - 12 * x


pyxel.init(
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    caption="Mafrum & Mafooba",
    scale=4,
)

pyxel.run(update, draw)
