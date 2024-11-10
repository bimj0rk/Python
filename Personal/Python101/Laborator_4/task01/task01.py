import random as rd
import math

def random_points(radius, x_center, y_center):
    x = rd.uniform(-radius, radius)
    y = rd.uniform(-radius, radius)
    if math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2) <= radius:
        return x, y

