import random as rd
import math

def random_points(radius, center_x, center_y):
    theta = rd.uniform(0, 2 * math.pi)
    r = math.sqrt(rd.uniform(0, 1)) * radius
    x = center_x + r * math.cos(theta)
    y = center_y + r * math.sin(theta)
    return x, y