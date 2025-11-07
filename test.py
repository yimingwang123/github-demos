class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)


    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
