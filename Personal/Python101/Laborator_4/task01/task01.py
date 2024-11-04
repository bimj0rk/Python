import random as rd
import math

def random_points(radius, x_center, y_center):
    x = rd.randint(-radius, radius)
    y = rd.randint(-radius, radius)
    if math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2) <= radius:
        return x, y

