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
    RADIUS = 10

    def __init__(self):
        self.x = 120
        self.y = 90
        self.direction = 1
        self.fall_speed = 0

    def draw_character(self):
        body_x, body_y = translate_coordinates(
            self.x,
            self.y,
        )
        pyxel.circ(
            body_x,
            body_y,
            Character.RADIUS,
            Color.WHITE,
        )
        eye_x, eye_y = translate_coordinates(
            self.x + 5 * self.direction,
            self.y + 5,
        )
        pyxel.circ(eye_x, eye_y, 2, Color.DARK_BLUE)

    @property
    def bottom(self):
        return self.y - Character.RADIUS

    @property
    def left(self):
        return self.x - Character.RADIUS

    @property
    def right(self):
        return self.x + Character.RADIUS


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
] + [
    Brick(100 + Brick.SIZE * i, 35)
    for i in range(4)
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
    collides_with_brick = [
        is_on_brick(character, brick)
        for brick in bricks
    ]
    if pyxel.btnp(pyxel.KEY_SPACE):
        character.fall_speed = -3.7
    if any(collides_with_brick) and character.fall_speed > 0:
        character.fall_speed = 0
    else:
        fall()


def draw_game():
    pyxel.cls(Color.LIGHT_BLUE)
    for brick in bricks:
        brick.draw_brick()
    character.draw_character()


def is_on_brick(char, brick):
    if char.bottom - 1 != brick.top:
        return False
    return is_same_x_range(char, brick)


def is_same_x_range(char, brick):
    if char.right < brick.left:
        return False
    if char.left > brick.right:
        return False
    return True


def fall():
    same_x_range_bricks = [
        brick
        for brick in bricks
        if is_same_x_range(character, brick)
    ]
    under_bricks = [
        brick
        for brick in same_x_range_bricks
        if character.bottom >= brick.top
    ]
    distances = [
        character.bottom - brick.top - 1
        for brick in under_bricks
    ]
    character.y -= min(distances + [character.fall_speed])
    character.fall_speed += 0.19


if __name__ == '__main__':
    pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
    pyxel.run(update, draw_game)
