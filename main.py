#!/usr/bin/python
import sys
import json
import random
import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt
from Polygon import Polygon


# Default to 10 if no number is entered upon running the script
# n_orders = sys.argv[1] if len(sys.argv) > 1 else 100
# print("n_orders", n_orders)
def run(n):
    polygon = Polygon()

    pickup_points = polygon.get_n_random_points(n)
    delivery_points = polygon.get_n_random_points(n)

    points = dict(zip(pickup_points, delivery_points))
    print(points)
    print(len(points))

    polygon.plot_coordinates(pickup_points, delivery_points)

run(10)
run(15)




    # plt.figure()
    # plt.plot(xs,ys)
    #
    # pickups = []
    # deliveries = []
    # for y, x in pickup_points:
    #     #plt.scatter(x, y)
    #     pickup = plt.scatter(x, y, color="blue", label='pickup')
    #     pickups.append(pickup)
    #
    # for y, x in delivery_points:
    #     #plt.scatter(x, y)
    #     delivery = plt.scatter(x, y, color="red", label='delivery')
    #     deliveries.append(delivery)
    # plt.legend()
    # plt.show()



    #print(pickup_points)
    #print(n)
    #polygon.plot_coordinates(pickup_points)


# coordinates = read_data('./data/helsinki_new.json')
#
# def get_n_random_coordinates(n, coordinates):
#     coords = []
#     while len(coords) != n:
#         random_point = get_random_point(coordinates)
#         if is_within_bounds(random_point, coordinates):
#             pickup_coord = random_point
#             coords.append(pickup_coord)
#         else:
#             continue
#     return coords
# #
#
# pickup_coords = get_n_random_coordinates(n_orders, coordinates)
# delivery_coords = get_n_random_coordinates(n_orders, coordinates)
#
# plot_coordinates(pickup_coords, coordinates)
# print(pickup_coords)
