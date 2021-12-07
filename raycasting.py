import json
import random
import numpy as np
from matplotlib import pyplot as plt

def is_within_bounds(P, V):
    '''Check whether point P is inside polygon V'''

    n = len(V)-1
    cn = 0
    i = 0

    for i in range(n):
        if (V[i][1] <= P[1] and V[i+1][1] > P[1]) or (V[i][1] > P[1] and V[i+1][1] <= P[1]):
            vt = (P[1]  - V[i][1]) / (V[i+1][1] - V[i][1])
            if P[0] < (V[i][0] + vt * (V[i+1][0] - V[i][0])):
                cn += 1
                return (cn&1)


#def get_random_point():
#    return [random.uniform(lat_max, lat_min), random.uniform(long_max, long_min)]













# f = open('./data/helsinki_new.json')
# data = json.load(f)
# coordinates = data["coordinates"]
#
# lat_max  = max(map(lambda x: x[0], coordinates))
# lat_min  = min(map(lambda x: x[0], coordinates))
# long_max = max(map(lambda x: x[1], coordinates))
# long_min = min(map(lambda x: x[1], coordinates))
#
# bottom_left  = [lat_min, long_min]
# top_left     = [lat_max, long_min]
# top_right    = [lat_max, long_max]
# bottom_right = [lat_min, long_max]

# print("bottom_left", bottom_left)
# print("top_left", top_left)
# print("top_right", top_right)
# print("bottom_right", bottom_right)

# https://github.com/sasamil/PointInPolygon_Py/blob/master/pointInside.py


# random_point1 = get_random_point()
# print(random_point1)
# print(is_within_bounds(random_point1, coordinates))
# random_point2 = get_random_point()
#
#
#
# ys, xs = zip(*coordinates) #create lists of x and y values
#
# plt.figure()
# plt.plot(xs,ys)
# plt.scatter(random_point1[1], random_point1[0])
# plt.show()
