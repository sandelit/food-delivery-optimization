import geopy.distance

coords_1 = (60.27686377728241, 25.025427454194684)
coords_2 = (60.17550582999867, 25.030633052651474)

print(geopy.distance.distance(coords_1, coords_2).m)
#11296.593711754846
