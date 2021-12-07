import matplotlib.pyplot as plt
import json

f = open('./data/helsinki_new.json')
data = json.load(f)


coord = data["coordinates"]

ys, xs = zip(*coord) #create lists of x and y values
# test comment 123
# test2123 commenta
plt.figure()
plt.plot(xs,ys)
plt.show() # if you need...

f.close()
