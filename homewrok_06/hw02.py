# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длинаширинамасса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    __length = None
    __width = None
    weight = None
    thickness = None

    def __init__(self, length, width):
        self.thickness = 0.05
        self.length = length
        self.width = width
        print('Create road_to_village object')

    def intake(self):
        self.weight = 25
        __intake = self.length * self.width * self.weight * self.thickness / 1000
        print(f'Need {__intake} ton for the building')


road_to_village = Road(20000, 6)
road_to_village.intake()

