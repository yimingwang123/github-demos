class Point3D:
    def __init__(self, x: int | float, y: int | float, z: int | float  ):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other: 'Point3D') -> 'Point3D':
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def subtract(self, other: 'Point3D') -> 'Point3D':
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance(self, other: 'Point3D') -> float:
        """计算两个三维点之间的欧几里得距离"""
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5
