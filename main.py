# Make a model that n rando points in a circle
# Calculate the possibility of a point being in the same semicircle


from random import random
# from matplotlib.patches import Circle

RADIAUS = 1

# CIRCLE_0 = Circle((0, 0), RADIAUS, fill=False)

POINT_1 = (0, 0)
POINT_2 = (0, 0)
POINT_3 = (0, 0)
POINT_4 = (0, 0)

points = []

def is_in_circle(point):
    return point[0] ** 2 + point[1] ** 2 < RADIAUS ** 2

def get_random_point():
    return (random(), random())

def get_random_points(n):
    return [get_random_point() for _ in range(n)]

def get_random_points_in_circle(n):
    cnt = 0
    points = []
    while cnt < n:
        point = get_random_point()
        if is_in_circle(point):
            points.append(point)
            cnt += 1
    return points

# def get_random_points_in_circle_ratio(n):
#     return len(get_random_points_in_circle(n)) / n

# def get_random_points_in_circle_ratio_list(n):
#     return [get_random_points_in_circle_ratio(i) for i in range(1, n)]

def is_in_same_semicircle(points):
    # Check if n points are in the same semicircle
    for point in points:
        pass
    pass

def main():
    points = get_random_points_in_circle(4)
    # is_in_same_semicircle(points)
    print(points)
    input()

if __name__ == '__main__':
    main()