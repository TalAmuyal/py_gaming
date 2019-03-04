import pyxel


WINDOW_WIDTH = 225
WINDOW_HEIGHT = 120


class Color:
    BLACK = 0
    DARK_BLUE = 1
    PURPLE = 2
    DARK_GREEN = 3
    BROWN = 4
    WHITE = 7
    LIGHT_BLUE = 12


def translate_coordinates(x, y):
    return x, WINDOW_HEIGHT - y - 1


class Character:
    def __init__(self):
        self.x = 0
        self.direction = 1

    def draw_character(self):
        x = 20 + self.x
        y = 20
        body_x, body_y = translate_coordinates(x, y)
        pyxel.circ(body_x, body_y, 10, Color.WHITE)
        eye_x, eye_y = translate_coordinates(x + 5 * self.direction, y + 5)
        pyxel.circ(eye_x, eye_y, 2, Color.DARK_BLUE)


class Brick:
    SIZE = 10

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_brick(self):
        x1, y1 = translate_coordinates(self.left, self.bottom)
        x2, y2 = translate_coordinates(
            self.right,
            self.top,
        )
        pyxel.rect(x1, y1, x2, y2, Color.DARK_GREEN)

    @property
    def top(self):
        return self.y + Brick.SIZE - 1

    @property
    def bottom(self):
        return self.y

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + Brick.SIZE - 1


character = Character()
bricks = [
    Brick(Brick.SIZE * i, 0)
    for i in range(10)
]


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btn(pyxel.KEY_LEFT):
        character.x -= 1
        character.direction = -1
    if pyxel.btn(pyxel.KEY_RIGHT):
        character.x += 1
        character.direction = 1


def draw_game():
    pyxel.cls(Color.LIGHT_BLUE)
    character.draw_character()
    for brick in bricks:
        brick.draw_brick()


if __name__ == '__main__':
    pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
    pyxel.run(update, draw_game)
