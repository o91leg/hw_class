from functools import reduce

class Animals:
    satiety = True

    def __init__(self, weight=0.0, name='noname'):
        self.name = name
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def voice(self, song):
        print(song)

    def state_satiety(self):
        if self.satiety:
            print('Не нужно кормить')
        else:
            print('Нужно покормить')

    def __add__(self, other):
        return Animals(self.weight + other.weight)

class WaterBirds(Animals):
    swiming = True

class Birds(Animals):
    wings = True
    eggs = True

    def get_eggs(self):
        if self.eggs:
            self.eggs = False
            print('Нужно собрать яйца')
            return self.eggs
        else:
            print('Яйца собраны')

class Ducks(WaterBirds, Birds):
    flying = True

    def voice(self, song='Кря'):
        super(Ducks, self).voice(song)

class Geese(WaterBirds, Birds):
    def voice(self, song='Гу гу гу'):
        super(Geese, self).voice(song)

class Hens(Birds):
    def voice(self, song='Кококо'):
        super(Hens, self).voice(song)

class Milk(Animals):
    def get_milk(self):
        if self.milk:
            self.milk = False
            print('Нужно доить')
            return self.milk
        else:
            print('Уже доили')

class Cows(Milk):
    milk = True

    def voice(self, song='Муууу'):
        super(Cows, self).voice(song)

class Goats (Milk):
    milk = True

    def voice(self, song='мееее'):
        super(Goats, self).voice(song)

class Sheep (Animals):
    shear = True

    def voice(self, song='беее'):
        super(Sheep, self).voice(song)

    def get_shear(self):
        if self.shear :
            self.shear  = False
            print('Нужно доить')
            return self.shear
        else:
            print('Уже доили')


cow = Cows(250, 'Манька')
goat1 = Goats(43, 'Рога')
goat2 = Goats(51, 'Копыта')
sheep1 = Sheep(98, 'Барашек')
sheep2 = Sheep(67, 'Кудрявый')
geese1 = Geese(9, 'Серый')
geese2 = Geese(8, 'Белый')
duck = Ducks(2, 'Кряква')
hen1 = Hens(2, 'Ко-ко')
hen2 = Hens(1, 'Кукареку')

if __name__ == '__main__':
    animal_list = [cow, goat1, goat2, sheep1, sheep2, geese1, geese2, duck, hen1, hen2]
    max_weight = reduce(lambda weight1, weight2: weight1 if (weight1 > weight2) else weight2, animal_list)
    sum_weight = reduce(lambda weight1, weight2: weight1 + weight2, animal_list)
    print(f'Самое тяжелое животное {max_weight.name}')
    print(f'Общий вес всех животных {sum_weight.weight} кг')