import pyxel


BALL_SPEED = 2
BAT_SPEED = 1.4


class Color:
    BLACK = 0
    WHITE = 7


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


def add_with_wall(axis, p, velocity):
    p_to_axis = axis - p
    axis_to_new_p = velocity - p_to_axis
    return p + p_to_axis - axis_to_new_p


def draw_centered_text(position, text, color):
    text_width = len(text) * pyxel.constants.FONT_WIDTH
    pyxel.text(
        position.x - text_width / 2,
        position.y,
        text,
        color,
    )


class Game:
    WIDTH = 225
    HEIGHT = 120

    def __init__(self):
        self.ball = Ball(
            Vector(Game.WIDTH / 2, Game.HEIGHT / 2),
            Vector(-1.5 / 2, 3 / 2),  # TODO: Randomize
        )
        self.player1_bat = Bat(
            Vector(0, Game.HEIGHT / 2 - Bat.HEIGHT / 2),
            pyxel.KEY_D,
            pyxel.KEY_F,
        )
        self.player2_bat = Bat(
            Vector(Game.WIDTH - Bat.WIDTH - 1, Game.HEIGHT / 2 - Bat.HEIGHT / 2),
            pyxel.KEY_K,
            pyxel.KEY_J,
        )
        pyxel.init(Game.WIDTH, Game.HEIGHT)

    def run(self):
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if self.get_winner() is not None:
            return
        self.player1_bat.update()
        self.player2_bat.update()
        self.ball.update(self.player1_bat, self.player2_bat)

    def draw(self):
        pyxel.cls(Color.BLACK)
        self.ball.draw()
        self.player1_bat.draw()
        self.player2_bat.draw()
        winner = self.get_winner()
        if winner is not None:
            draw_centered_text(
                Vector(Game.WIDTH / 2, Game.HEIGHT / 2),
                f'The Winner is: {winner}',
                Color.WHITE,
            )

    def get_winner(self):
        if self.ball.position.x < 0:
            return 'Player 2'
        if self.ball.position.x > Game.WIDTH:
            return 'Player 1'
        return None


class Ball:
    RADIUS = 2

    def __init__(
            self,
            initial_position,
            initial_velocity,
            ):
        self.position = initial_position
        self.velocity = initial_velocity

    def update(self, bat1, bat2):
        new_position = self.position + self.velocity

        if 0 < new_position.y < Game.HEIGHT:
            self.position.y = new_position.y
        else:
            wall = 0 if new_position.y <= 0 else Game.HEIGHT
            self.position.y = add_with_wall(
                wall,
                self.position.y,
                self.velocity.y,
            )
            self.velocity.y *= -1

        if bat1.collides_with(self):
            self.position.x = add_with_wall(
                bat1.top_left_position.x + Bat.WIDTH + Ball.RADIUS,
                self.position.x,
                self.velocity.x,
            )
            self.velocity.x *= -1
        else:
            self.position.x = new_position.x

        if bat2.collides_with(self):
            self.position.x = add_with_wall(
                bat2.top_left_position.x - Ball.RADIUS,
                self.position.x,
                self.velocity.x,
            )
            self.velocity.x *= -1
        else:
            self.position.x = new_position.x

    def draw(self):
        pyxel.circ(
            self.position.x,
            self.position.y,
            Ball.RADIUS,
            Color.WHITE,
        )


class Bat:
    WIDTH = 2
    HEIGHT = 18
    SPEED = 2  # pixels per frame

    def __init__(
            self,
            initial_top_left_position,
            up_key,
            down_key,
            ):
        self.top_left_position = initial_top_left_position
        self.up_key = up_key
        self.down_key = down_key

    def collides_with(self, ball):
        ball_bottom = ball.position.y + Ball.RADIUS
        bat_top = self.top_left_position.y
        if ball_bottom < bat_top:
            return False
        ball_top = ball.position.y - Ball.RADIUS
        bat_bottom = bat_top + Bat.HEIGHT
        if ball_top > bat_bottom:
            return False
        ball_left = ball.position.x - Ball.RADIUS
        bat_right = self.top_left_position.x + Bat.WIDTH
        if self.top_left_position.x <= ball_left <= bat_right:
            return True
        ball_right = ball.position.x + Ball.RADIUS
        if self.top_left_position.x <= ball_right <= bat_right:
            return True
        return False

    def update(self):
        if pyxel.btn(self.up_key):
            self.top_left_position.y -= Bat.SPEED
        elif pyxel.btn(self.down_key):
            self.top_left_position.y += Bat.SPEED

    def draw(self):
        pyxel.rect(
            self.top_left_position.x,
            self.top_left_position.y,
            self.top_left_position.x + Bat.WIDTH,
            self.top_left_position.y + Bat.HEIGHT,
            Color.WHITE,
        )


if __name__ == '__main__':
    game = Game()
    game.run()

