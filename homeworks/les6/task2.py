class Road:
    mass = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_asphalt(self):
        return self._length * self._width * self.mass


road = Road(25, 1000)
road.mass = 125
print(road.mass_asphalt())
