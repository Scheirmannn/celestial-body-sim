import math
from turtle import *


class Body(Turtle):
    name = 'Body'
    mass = None
    vx = vy = 0.0
    px = py = 0.0

    def attraction(self, other):

        if self is other:
            raise ValueError("Attraction of object %r to itself requested"
                             % self.name)

        sx, sy = self.px, self.py
        ox, oy = other.px, other.py
        dx = (ox - sx)
        dy = (oy - sy)
        d = math.sqrt(dx ** 2 + dy ** 2)

        if d == 0:
            raise ValueError("Collision between objects %r and %r"
                             % (self.name, other.name))

        f = 6.67428e-11 * self.mass * other.mass / (d ** 2)

        theta = math.atan2(dy, dx)
        fx = math.cos(theta) * f
        fy = math.sin(theta) * f
        return fx, fy


def update_info(step, bodies):
    print('Step #{}'.format(step))
    for body in bodies:
        s = '{:<8}  Pos.={:>6.2f} {:>6.2f} Vel.={:>10.3f} {:>10.3f}'.format(
            body.name, body.px / 149.6e9, body.py / 149.6e9, body.vx, body.vy)
        print(s)
    print()


def loop(bodies):
    timestep = 48 * 3600

    for body in bodies:
        body.penup()
        bgcolor("black")

    step = 1
    while True:
        step += 1
        update_info(step, bodies)
        force = {}
        for body in bodies:
            total_fx = total_fy = 0.0
            for other in bodies:
                if body is other:
                    continue
                fx, fy = body.attraction(other)
                total_fx += fx
                total_fy += fy

            force[body] = (total_fx, total_fy)

        for body in bodies:
            fx, fy = force[body]
            body.vx += fx / body.mass * timestep
            body.vy += fy / body.mass * timestep

            body.px += body.vx * timestep
            body.py += body.vy * timestep
            body.goto(body.px * 1.67112299e-9, body.py * 1.67112299e-9)
            body.dot(3)
            body.pensize(3)


def main():
    sun = Body()
    sun.name = 'Sun'
    sun.mass = 1.98892 * 10 ** 30
    sun.pencolor('yellow')
    sun.ht()

    p1 = Body()
    p1.name = 'P1'
    p1.mass = 5.9742 * 10 ** 24
    p1.px = -1 * 149.6e9
    p1.vy = 29.783 * 1000
    p1.pencolor('green')
    p1.ht()

    p2 = Body()
    p2.showturtle()
    p2.name = 'P2'
    p2.mass = 4.8685 * 10 ** 24
    p2.px = .523 * 149.6e9
    p2.vy = -35.02 * 1000
    p2.pencolor('red')
    p2.ht()

    p3 = Body()
    p3.showturtle()
    p3.name = 'P3'
    p3.mass = 4.3245 * 10 ** 24
    p3.px = -1.234 * -149.6e9
    p3.py = -.2 * -149.6e9
    p3.vy = 17.15 * 1000
    p3.pencolor('blue')
    p3.ht()

    p4 = Body()
    p4.showturtle()
    p4.name = 'P4'
    p4.mass = 4.3245 * 10 ** 26
    p4.px = -1.394 * 149.6e9
    p4.py = -.614 * 149.6e9
    p4.vy = 13.615 * 1000
    p4.pencolor('white')
    p4.ht()

    sun.dot(50)
    title("celestial-body-sim")

    loop([sun, p1, p2, p3, p4])


if __name__ == '__main__':
    main()
