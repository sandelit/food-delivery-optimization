import json

f = open('./data/helsinki.json')
data = json.load(f)

coordinates = data['geometries'][0]['coordinates']

helsinki_coordinates = []

for c in coordinates[::15]:
    c[0], c[1] = c[1], c[0]
    print(c)

    #60.143680 - 25.1
    if c[0] > 60.143680 and c[1] < 25.09:
         print(c)
         helsinki_coordinates.append(c)

helsinki_coordinates.append([60.1437,25.09])          # bottom right corner
helsinki_coordinates.append(helsinki_coordinates[0])  # repeat the first point to create a 'closed loop'

print("Length of coordinates:", len(helsinki_coordinates))

output = {"coordinates": helsinki_coordinates}

with open('./data/helsinki_new.json', 'w') as outfile:
    json.dump(output, outfile)
f.close()
