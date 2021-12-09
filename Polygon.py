import json
import random
import numpy as np
import matplotlib.path as mplPath
import matplotlib.pyplot as plt

class Polygon(object):
    """docstring Polygon."""

    def __init__(self):
        self.coordinates = self.read_data('./data/helsinki_new.json')
        self.lat_max  = max(map(lambda x: x[0], self.coordinates))
        self.lat_min  = min(map(lambda x: x[0], self.coordinates))
        self.long_max = max(map(lambda x: x[1], self.coordinates))
        self.long_min = min(map(lambda x: x[1], self.coordinates))
        self.courier_location = self.get_courier_location()

    def get_courier_location(self):
        lat = (self.lat_max + self.lat_min) / 2
        long = (self.long_max + self.long_min) / 2
        return (lat, long)

    def read_data(self, path):
        f = open(path)
        data = json.load(f)
        return [tuple(coordinate) for coordinate in data['coordinates']]

    def is_within_bounds(self, point):
        poly_path = mplPath.Path(np.array(self.coordinates))
        return poly_path.contains_point(point)

    def get_random_point(self):
        return (random.uniform(self.lat_max, self.lat_min), random.uniform(self.long_max, self.long_min))

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
