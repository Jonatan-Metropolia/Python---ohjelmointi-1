import math

import matplotlib.pyplot as plt
import numpy as np

def points (list):
    local_radius = radius

    for i in list:
        angle = math.radians(i)

        x = math.cos(angle)*local_radius
        y = math.sin(angle)*local_radius

        plt.annotate(i, (x,y),
                     xytext=(+20, +5), textcoords='offset points', fontsize=8,
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))
        point = plt.Circle((x, y), radius=0.1, fill=True, color='red')
        ax.add_patch(point)



fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.grid()

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

radius = 7

circle = plt.Circle((0, 0), radius, color='black', fill=False)
ax.add_patch(circle)

point_list = [30, 45, 60, 90, 120, 150, 180, 270]

points(point_list)

plt.show()


