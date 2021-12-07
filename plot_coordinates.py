import matplotlib.pyplot as plt
import json

f = open('./data/helsinki_new.json')
data = json.load(f)
coord = data["coordinates"]

ys, xs = zip(*coord) #create lists of x and y values

plt.figure()
plt.plot(xs,ys)
plt.show()

f.close()
