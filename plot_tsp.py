import matplotlib.pyplot as plt

def plot_tsp(coordinates,pickup_points, delivery_points, start_pos,
            mid_pos, end_pos, pickup_path, delivery_path):
    ys, xs = zip(*coordinates)
    px, py = zip(*pickup_points)
    dx, dy = zip(*delivery_points)
    sx, sy = start_pos
    mx, my = mid_pos
    ex, ey = end_pos

    fig, ax = plt.subplots()
    fig = plt.plot(xs, ys)

    pickups = ax.scatter(py, px, color='b')
    deliveries = ax.scatter(dy, dx, color='r')
    start = ax.scatter(sy, sx, color='b', s = 150)
    mid = ax.scatter(my, mx, color='g', s = 150)
    end = ax.scatter(ey, ex, color='r', s = 150)

    for p in pickup_path:
        y1, x1 = pickup_points[p-1]
        y2, x2 = pickup_points[p]
        x = [x1, x2]
        y = [y1, y2]
        ax.plot(x, y, color='b')
        #ax.quiver(x1, y1, (x2-x1), (y2-y1), angles='xy', scale_units='xy', scale=1, color='b', width=0.001, headwidth=10, headlength=10)

    for p in delivery_path:
        y1, x1 = delivery_points[p-1]
        y2, x2 = delivery_points[p]
        x = [x1, x2]
        y = [y1, y2]
        ax.plot(x, y, color='r')
        #ax.quiver(x1, y1, (x2-x1), (y2-y1), angles='xy', scale_units='xy', scale=1, color='r', width=0.001, headwidth=10, headlength=10)

    plt.legend((pickups,deliveries, mid, start, end),('pickups', 'deliveries', 'mid', 'start', 'end'),numpoints=1, fontsize=8)
    plt.show()
