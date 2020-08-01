class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return self.name + ' поехала'

    def stop(self):
        return self.name + ' останавилась'

    def turn(self, direction):
        return self.name + ' повернул ' + direction

    def show_speed(self):
        return 'Скорость: ' + self.name + ' ' + str(self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return 'Преавышение скорости town_car'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return 'Превышение скорости work_car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police_car(self):
        if self.is_police:
            return 'Полицейская машина'


toyota = TownCar(39, 'Белый', 'Toyota', False)
ferrari = SportCar(150, 'Красный', 'Ferrari', False)
kia = WorkCar(90, 'Черный', 'KIA', False)
vaz = PoliceCar(100, 'Синий', 'Жигули', True)

print(toyota.stop())
print(ferrari.turn('влево'))
print(kia.show_speed())
