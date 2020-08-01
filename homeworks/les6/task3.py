class Worker:
    income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self) -> float:
        __w = float(self.income.get('wage'))
        __b = float(self.income.get('bonus'))
        return __w + __b


pos = Position('Yerzhan', 'Kudaibergenov', 'manager', 1500, 2000)
print('Полное имя: ' + pos.get_full_name())
print('Доход: ' + str(pos.get_total_income()))
