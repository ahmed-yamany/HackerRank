import math
"""
You are given four points A, B, C and D n a 3-dimensional Cartesian coordinate system. 
You are required to print the angle between the plane made by the points A, B, C and D
in degrees(not radians) Let the angle be PHI
Cos(PHI) = (X.Y)/|X||Y| where Z = AB × BC and Y = BC × CD.
Here X.Y means the dot product of X and Y, and AB × BC means the cross product vectors AB and BC.
Also AB = B - A


"""

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Points(x, y, z)

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Points(x, y, z)

    def dot(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return x + y + z

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)

    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
