import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    @staticmethod
    def running():
        x = range(3)
        for i in x:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            if i == 1:
                time.sleep(5)
            if i == 2:
                time.sleep(3)


tr = TrafficLight()
tr.running()
