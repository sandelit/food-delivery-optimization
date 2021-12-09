import json
import random
import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt

class Polygon(object):
    """docstring Polygon."""

    def __init__(self):
        self.coordinates = self.read_data('./data/helsinki_new.json')

    def read_data(self, path):
        f = open(path)
        data = json.load(f)
        return [tuple(coordinate) for coordinate in data['coordinates']]

    def is_within_bounds(self, point):
        poly_path = mplPath.Path(np.array(self.coordinates))
        return poly_path.contains_point(point)

    def get_random_point(self):
        lat_max  = max(map(lambda x: x[0], self.coordinates))
        lat_min  = min(map(lambda x: x[0], self.coordinates))
        long_max = max(map(lambda x: x[1], self.coordinates))
        long_min = min(map(lambda x: x[1], self.coordinates))
        return (random.uniform(lat_max, lat_min), random.uniform(long_max, long_min))

    def get_n_random_points(self, n):
        coords = []
        while len(coords) != n:
            random_point = self.get_random_point()
            if self.is_within_bounds(random_point):
                pickup_coord = random_point
                coords.append(pickup_coord)
            else:
                continue
        return coords

    def plot_coordinates(self, pickup_points=None, delivery_points=None):
        ys, xs = zip(*self.coordinates)
        px, py = zip(*pickup_points)
        dx, dy = zip(*delivery_points)
        fig, ax = plt.subplots()
        fig = plt.plot(xs, ys)
        pickups = ax.scatter(py, px,color='b')
        deliveries = ax.scatter(dy, dx, color='r')
        plt.legend((pickups,deliveries),('pickups', 'deliveries'),numpoints=1, fontsize=8)
        plt.show()

class Point():
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def distance_to(point):
        return distance(self.coordinates, point)
