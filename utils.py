import json
import random
import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt

def read_data(path):
    f = open(path)
    data = json.load(f)
    return data["coordinates"]

def get_random_point(coordinates):
    lat_max  = max(map(lambda x: x[0], coordinates))
    lat_min  = min(map(lambda x: x[0], coordinates))
    long_max = max(map(lambda x: x[1], coordinates))
    long_min = min(map(lambda x: x[1], coordinates))
    return [random.uniform(lat_max, lat_min), random.uniform(long_max, long_min)]

def is_within_bounds(random_point, coordinates):
    poly_path = mplPath.Path(np.array(coordinates))
    return poly_path.contains_point(random_point)


def plot_coordinates(points, coordinates, helsinki=False):
    ys, xs = zip(*coordinates)

    plt.figure()
    plt.plot(xs,ys)
    #scatters = []
    for y, x in points:
        plt.scatter(x, y)
        #scatter = plt.scatter(y, x)
        #scatters.append(scatter)
    #plt.legend((scatters), (scatters))
    plt.show()


#
# poly_path = mplPath.Path(np.array(coordinates))
#
# points = []
# for i in range(10):
#     random_point = get_random_point()
#     points.append(random_point)
#     print(random_point, " is in polygon:", poly_path.contains_point(random_point))
#
#
#
# ys, xs = zip(*coordinates)
#
# plt.figure()
# plt.plot(xs,ys)
# #scatters = []
# for y, x in points:
#     plt.scatter(x, y)
#     #scatter = plt.scatter(y, x)
#     #scatters.append(scatter)
# #plt.legend((scatters), (scatters))
# plt.show()
#
#
#
# bottom_left  = [lat_min, long_min]
# top_left     = [lat_max, long_min]
# top_right    = [lat_max, long_max]
# bottom_right = [lat_min, long_max]
#
# # print("bottom_left", bottom_left)
# # print("top_left", top_left)
# # print("top_right", top_right)
# # print("bottom_right", bottom_right)
#
# #https://github.com/sasamil/PointInPolygon_Py/blob/master/pointInside.py
#
# # points = []
# #
# # for i in range(10):
# #     random_point = get_random_point()
# #     points.append(random_point)
# #     print(random_point)
# #     print(is_within_bounds(random_point, coordinates))
# #     #
# #     # ys, xs = zip(*coordinates) #create lists of x and y values
# #
