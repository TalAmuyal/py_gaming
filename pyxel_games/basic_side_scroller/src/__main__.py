import math

import pyxel


WINDOW_WIDTH = 225
WINDOW_HEIGHT = 120

STARTING_POSITION = (120.0, 90.0)


class Color:
    BLACK = 0
    DARK_BLUE = 1
    PURPLE = 2
    DARK_GREEN = 3
    BROWN = 4
    GRAY = 6
    WHITE = 7
    RED = 8
    LIGHT_BLUE = 12


def translate_coordinates(x, y, character_relative=True):
    if character_relative:
        x, y = translate_character_to_center(x, y)
        x, y = translate_character_coordinates(x, y)
    return translate_coordinates_to_pyxel(x, y)


def translate_character_coordinates(x, y):
    min_char_x = WINDOW_WIDTH / 2
    min_char_y = WINDOW_HEIGHT / 2
    bordered_char_x = max(character.x, min_char_x)
    bordered_char_y = max(character.y, min_char_y)
    return x - bordered_char_x, y - bordered_char_y


def translate_character_to_center(x, y):
    return x + WINDOW_WIDTH / 2, y + WINDOW_HEIGHT / 2


def translate_coordinates_to_pyxel(x, y):
    return x, WINDOW_HEIGHT - y - 1


class Life:
    RADIUS = 3
    X = 1.5 * RADIUS
    Y = WINDOW_HEIGHT - 1 - 1.5 * RADIUS

    def __init__(self):
        self.count = 3

    def draw(self):
        for i in range(self.count):
            width = 2 * Life.RADIUS + 1
            offset = i * (width + math.ceil(Life.RADIUS / 2))
            x, y = translate_coordinates(
                Life.X + offset,
                Life.Y,
                character_relative=False,
            )
            pyxel.circ(x, y, Life.RADIUS, Color.RED)


class Character:
    RADIUS = 10
    WIDTH = 2 + RADIUS + 1
    HEIGHT = 2 * RADIUS + 1

    def __init__(self):
        self.x, self.y = STARTING_POSITION
        self.direction = 1
        self.fall_speed = 0
        self.double_jumped = True

    def reset(self, position):
        self.x, self.y = position
        self.direction = 1
        self.fall_speed = 0
        self.double_jumped = True

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
    def top(self):
        return self.y + Character.RADIUS

    @property
    def bottom(self):
        return self.y - Character.RADIUS

    @property
    def left(self):
        return self.x - Character.RADIUS

    @property
    def right(self):
        return self.x + Character.RADIUS


class Door:
    WIDTH = Character.WIDTH * 2
    HEIGHT = math.ceil(Character.HEIGHT * 2.5)

    def __init__(self, left, bottom):
        self.left = left
        self.bottom = bottom

    def draw(self):
        left, top = translate_coordinates(
            self.left,
            self.bottom + Door.HEIGHT - 1,
        )
        right, bottom = translate_coordinates(
            self.left + Door.WIDTH - 1,
            self.bottom,
        )
        pyxel.rect(left, top, right, bottom, Color.GRAY)


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


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        radius = 5
        coordinates = [
            (0, 0),
            (8, 0),
            (-8, 0),
            (4, 3),
            (-4, 3),
        ]
        for x, y in coordinates:
            translated_x, translated_y = translate_coordinates(
                self.x + x,
                self.y + y,
            )
            pyxel.circ(
                translated_x,
                translated_y,
                radius,
                Color.WHITE,
            )


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if is_game_over(character):
        return
    if has_fallen_out(character):
        life.count -= 1
        character.reset(STARTING_POSITION)
    if pyxel.btn(pyxel.KEY_LEFT):
        character.x -= 1
        character.direction = -1
    if pyxel.btn(pyxel.KEY_RIGHT):
        character.x += 1
        character.direction = 1

    collides_with_brick = any([
        is_on_brick(character, brick)
        for brick in bricks
    ])
    if (collides_with_brick or character.double_jumped is False) and pyxel.btnp(pyxel.KEY_SPACE):
        character.fall_speed = -3.7
        character.double_jumped = not collides_with_brick
    elif collides_with_brick and character.fall_speed > 0:
        character.fall_speed = 0
        character.double_jumped = False
    else:
        fall()


def draw_game():
    pyxel.cls(Color.LIGHT_BLUE)
    for brick in bricks:
        brick.draw_brick()
    for cloud in clouds:
        cloud.draw()
    door.draw()
    character.draw_character()
    if is_game_over(character):
        pyxel.text(100, WINDOW_HEIGHT / 2, "GAME OVER", Color.WHITE)
        pyxel.text(101, WINDOW_HEIGHT / 2 + 1, "GAME OVER", Color.RED)
    life.draw()


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


def has_fallen_out(char):
    return char.top <= 0


def is_game_over(char):
    return has_fallen_out(char) and life.count == 0


if __name__ == '__main__':
    pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)

    life = Life()
    door = Door(
        left=170 + Brick.SIZE * 7 - Door.WIDTH,
        bottom=70 + Brick.SIZE,
    )
    character = Character()
    bricks = [
        Brick(Brick.SIZE * i, 0)
        for i in range(10)
    ] + [
        Brick(100 + Brick.SIZE * i, 35)
        for i in range(4)
    ] + [
        Brick(170 + Brick.SIZE * i, 70)
        for i in range(8)
    ]
    clouds = [
        Cloud(70, 160),
        Cloud(120, 140),
        Cloud(240, 170),
    ]

    pyxel.run(update, draw_game)
