import geopandas as geopd
import matplotlib.pyplot as plt
from shapely.geometry import *

pointA = (-5, -1)
pointB = (0, -2)
pointC = (1, 0)
pointD = (5, 12)
pointE = (7, 8)

lineString = LineString([pointA, pointB, pointC])
#
# geopd.GeoSeries([lineString]).plot()
# plt.show()



def bc(a, b, c, t):
    return (1 - t) * ((1 - t) * a + t * b) + t * ((1 - t) * b + t * c)

def get_curve(pointA, pointB, pointC):
    point_list=[]
    for i in range(100):
        t = i / 100
        x = bc(pointA[0], pointB[0], pointC[0], t)
        y = bc(pointA[1], pointB[1], pointC[1], t)
        point_list.append((x, y))
    return LineString(point_list)
geopd.GeoSeries([get_curve(pointA, pointB, pointC),
                 LineString([pointA, pointB, pointC, pointD, pointE]),
                 get_curve(pointC, pointD, pointE)]).plot()
plt.show()
