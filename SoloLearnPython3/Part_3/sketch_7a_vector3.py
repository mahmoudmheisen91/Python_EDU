class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return 3

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            return self.z

    def __add__(self, other):
        _x = self.x + other.x
        _y = self.y + other.y
        _z = self.z + other.z
        return Vector3(_x, _y, _z)

    def __sub__(self, other):
        _x = self.x - other.x
        _y = self.y - other.y
        _z = self.z - other.z
        return Vector3(_x, _y, _z)

    def __mul__(self, other):
        _x = self.x * other.x
        _y = self.y * other.y
        _z = self.z * other.z
        return Vector3(_x, _y, _z)

    def _toStr(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"


class Vector3Test:
    def __init__(self, vec3):
        self.vec3 = vec3
        self.quot = ""
        self.pre = "Current vector: "

    def testAddMethod(self, other):
        self.quot = f"Adding: {other._toStr()} to {self.vec3._toStr()} ...\n"
        self.vec3 += other
        self.pre = "After Addition: "
        self.execute()

    def testLenMethod(self):
        print(f"length: {len(self.vec3)}")

    def testSubMethod(self, other):
        self.quot = f"Subtracting: {other._toStr()} from {self.vec3._toStr()} ...\n"
        self.vec3 -= other
        self.pre = "After Subtracting: "
        self.execute()

    def testGetItemMethod(self):
        x = self.vec3[0]
        y = self.vec3[1]
        z = self.vec3[2]
        print(f"x = {x}, y = {y}, z = {z}")

    def execute(self):
        print(self.quot + self.pre + self.vec3._toStr())
        self.pre = "Current vector: "


if __name__ == "__main__":
    test1 = Vector3Test(Vector3(1, 2, 3))
    test1.execute()
    test1.testAddMethod(Vector3(-1, -2, -3))
    test1.testSubMethod(Vector3(1, -1, 0))
    test1.execute()
    test1.testLenMethod()
    test1.testGetItemMethod()
    #v1 = Vector3(1, 2, 3)
    # print(v1.len())
