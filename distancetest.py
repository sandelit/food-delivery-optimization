import geopy.distance

coords_1 = (60.16952, 24.93545)
coords_2 = (59.32932, 18.06858)

print(geopy.distance.distance(coords_1, coords_2).m)


dict2 = {"test2": "test2"}
dict3 = {"test3": "test3"}
dict = {dict2:"dict2", dict3:"dict3"}
