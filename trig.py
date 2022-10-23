# Make a model that n random points are in a circle
# Calculate the possibility of n points being in the same semicircle

# The expected probability is: n/2^(n-1)
# For n = 1, the probability is: 1
# For n = 2, the probability is: 1
# For n = 3, the probability is: .75
# For n = 4, the probability is: .5
# For n = 5, the probability is: .3125
# ...

from random import random
from math import sin, cos, pi

RADIAUS = 1
NUM_OF_POINTS = 4

# Store the points using polar coordinates
class POINT:
    def __init__(self, r, theta):
        self.r = r
        self.theta = theta
        self.x = r * cos(theta)
        self.y = r * sin(theta)


def get_random_point():
    r = random() * RADIAUS  # [0, 1)
    theta = random() * 2 * pi  # [0, 2pi)
    return POINT(r, theta)


def get_random_points(n):
    return [get_random_point() for _ in range(n)]


def is_in_same_semicircle(points):
    for i in range(len(points)):
        theta = points[i].theta
        bound = (theta + pi) % (2 * pi)

        lower_bound = min(theta, bound)
        upper_bound = max(theta, bound)

        anti_clockwise = False
        clockwise = False

        for point in points:
            if point.theta > lower_bound and point.theta < upper_bound:
                anti_clockwise = True
            elif point.theta < lower_bound or point.theta > upper_bound:
                clockwise = True
            if anti_clockwise and clockwise:
                continue
        # At the break condition, given boundaries works for all points
        if not (anti_clockwise and clockwise):
            return True
    # After the loop, no possible boundaries found
    return False


def main():
    points = get_random_points(NUM_OF_POINTS)
    return (is_in_same_semicircle(points))


if __name__ == '__main__':
    total_trials = 0
    total_success = 0
    while True:
        if main():
            total_success += 1
        total_trials += 1
        print(str(total_success) + ' / ' + str(total_trials) +
              ' = ' + str(total_success / total_trials), end='\r')
