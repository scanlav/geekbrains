# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и
# костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Textile:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'{self.name} - общая площадь ткани \n {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)} м2')


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height, name='Пальто')
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь ткани на пальто {self.square_c} м2'


class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height, name='Костюм')
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь ткани на костюм {self.square_j} м2'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_c())
print(jacket.get_square_j())

