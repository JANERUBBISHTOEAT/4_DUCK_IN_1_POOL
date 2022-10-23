# Make a model that n random points in a circle
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

    # def __str__(self):
    #     return f"({self.x}, {self.y})"


# def is_in_circle(point):
#     return point.r <= RADIAUS


def get_random_point():
    r = random() * RADIAUS  # [0, 1)
    theta = random() * 2 * pi  # [0, 2pi)
    return POINT(r, theta)


def get_random_points(n):
    return [get_random_point() for _ in range(n)]


# This function is no longer needed since
# the random points are defined in the circle already
# def get_random_points_in_circle(n):
#     cnt = 0
#     points = []
#     while cnt < n:
#         point = get_random_point()
#         if is_in_circle(point):
#             points.append(point)
#             cnt += 1
#     return points

# Debug
# delta_min = pi
# delta_max = 0
# theta_min = 2 * pi
# theta_max = 0
# radius_max = 0
# radius_min = 1


def is_in_same_semicircle_bad(points):  # Does not work
    # global delta_min, delta_max
    # global theta_min, theta_max
    # global radius_max, radius_min

    theta = points[0].theta
    max_theta = theta
    min_theta = theta

    for point in points:
        if point.theta < min_theta:
            min_theta = point.theta
        elif point.theta > max_theta:
            max_theta = point.theta

    # Debug

    # The extreme delta of theta:
    # if delta_min > max_theta - min_theta:
    #     delta_min = max_theta - min_theta
    # if delta_max < max_theta - min_theta:
    #     delta_max = max_theta - min_theta
    # print (delta_min, delta_max, end='\r')

    # The extreme theta:
    # if theta_min > min_theta:
    #     theta_min = min_theta
    # if theta_max < max_theta:
    #     theta_max = max_theta
    # print (theta_min, theta_max, end='\r')

    # The extreme radius:
    # max_radius = 0
    # min_radius = 1
    # for point in points:
    #     if point.r > max_radius:
    #         max_radius = point.r
    #     if point.r < min_radius:
    #         min_radius = point.r
    # if radius_max < max_radius:
    #     radius_max = max_radius
    # if radius_min > min_radius:
    #     radius_min = min_radius
    # print (radius_min, radius_max, end='\r')

    return max_theta - min_theta <= pi


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
        if not (anti_clockwise and clockwise):  # At the break condition it works
            return True
    return False


def main():
    points = get_random_points(NUM_OF_POINTS)
    # for point in points:
    #     print(point.x, point.y)
    # print(is_in_same_semicircle(points))
    # input()
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
        # print(total_success / total_trials, end='\r')
