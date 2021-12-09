#!/usr/bin/python
import sys
import json
import random
import geopy.distance
import pprint as pp
import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt
import pandas as pd
from Polygon import Polygon
from scipy.spatial import distance_matrix
from TSP import tsp
from plot_tsp import plot_tsp
import pprint

def run(n):
    polygon = Polygon()
    courier_location = polygon.courier_location
    pickup_points = polygon.get_n_random_points(n)
    delivery_points = polygon.get_n_random_points(n)






    points = [
        courier_location,
        *pickup_points,
        *delivery_points
    ]
    points = [list(elem) for elem in points]

    print("\nCourier location")
    pprint.pprint(points[0])
    print("\nPickup locations")
    pprint.pprint(points[1:10])
    print("\nDelivery locations")
    pprint.pprint(points[10:])

    length, path = tsp(points)

def run_2(n):
    polygon = Polygon()
    courier_position = polygon.courier_location
    start_position = courier_position
    pickup_points = polygon.get_n_random_points(n)
    delivery_points = polygon.get_n_random_points(n)

    # Run TSP on all pickup points
    points1 = [courier_position, *pickup_points]
    points1 = [list(elem) for elem in points1]
    length1, path_pickup = tsp(points1)
    # Set Courier location as last point in the optimal path for pickups
    courier_position = pickup_points[path_pickup[-1] - 1]

    # Run TSP on all delivery points
    points2 = [courier_position, *delivery_points]
    points2 = [list(elem) for elem in points2]
    length2, path_delivery = tsp(points2)

    # Sort points according to path from TSP
    pickup_sorted = sort_points(pickup_points, path_pickup)
    pickup_sorted.insert(0, start_position)
    del pickup_sorted[-1]
    delivery_sorted = sort_points(delivery_points, path_delivery)
    delivery_sorted.insert(0, pickup_sorted[-1])
    del delivery_sorted[-1]

    print("PICKUP POINTS")
    pprint.pprint(pickup_points)
    print("PICKUP PATH")
    print(path_pickup)
    print("PICKUP SORTED")
    pprint.pprint(pickup_sorted)
    print("------------------------------------------")
    print("DELIVERY POINTS")
    pprint.pprint(delivery_points)
    print("DELIVERY PATH")
    print(path_delivery)
    print("DELIVERY SORTED")
    pprint.pprint(delivery_sorted)

    # Set middle and last position
    mid_position = pickup_sorted[-1]
    end_position = delivery_sorted[-1]

    plot_tsp(polygon.coordinates, pickup_sorted, delivery_sorted, start_position,
            mid_position, end_position, path_pickup, path_delivery)

def sort_points(points, path):
    sorted = []
    for p in path:
        sorted.append(points[p-1])
    return sorted

run_2(15)
