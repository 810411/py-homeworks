class Animal:
    """ Базовый класс животного, имеет вес, аппетит, можно покормить, узнать вес и издает тишину"""
    _weight = 500  # kg
    _appetite = 100  # gram
    _voice = ''

    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.get_weight() + other.get_weight()

    def to_feed(self, feed):
        """ Метод кормления животного, издает голос если корма не хватает для удовлетворения аппетита"""
        self._appetite -= feed
        return self._to_voice() if self._appetite > 0 else self._go_sleep()

    def _to_voice(self):
        print('{}: {}'.format(self.name, self._voice))

    def get_weight(self):
        return self._weight

    def _go_sleep(self):
        print('{} идет спать'.format(self.name))

    @staticmethod
    def _collect_message(self, out_count, out_type):
        """ метод уведомляющий о результатах подоить/постричь/собрать"""
        message = 'От {} получили {} {}'.format(self.name, out_count, out_type)
        return message


class Giver:
    def _collect_message(self, self1, product, s):
        pass


class Milkgiver(Giver):
    """ родительский класс для животных дающих молоко """
    _milk = 10  # litre

    def get_milk(self):
        return self._milk

    def collect(self):
        print(self._collect_message(self, self.get_milk(), 'л молока'))


class Egggiver(Giver):
    """ родительский класс для животных дающих яйца """
    _egg = 2

    def get_egg(self):
        return self._egg

    def collect(self):
        print(self._collect_message(self, self.get_egg(), 'яйца(о)'))


class Cow(Animal, Milkgiver):
    _appetite = 10000
    _voice = 'Му-муууу'

    def get_milk(self):
        return self._milk - (self._appetite / 1000)


class Goat(Animal, Milkgiver):
    _milk = 5
    _voice = 'Меееее'
    _appetite = 1000


class Goose(Animal, Egggiver):
    _weight = 5
    _voice = 'Га-га-га'
    _egg = 1


class Duck(Animal, Egggiver):
    _weight = 4
    _voice = 'Кря-кря'


class Hen(Animal, Egggiver):
    _weight = 3
    _voice = 'Ко-ко-ко'
    _egg = 3


class Sheep(Animal):
    _weight = 50
    _appetite = 1000
    _voice = 'Бееее'
    _wool = 5  # кг%

    def to_trim(self, wool=5):
        """ метод стрижки, задает количество запрошенной шерсти если таковое имеется либо всю имеющуюся шерсть"""
        self._wool = wool if wool <= self._wool else self._wool
        return self._wool

    def get_wool(self):
        return self._wool

    def collect(self):
        print(self._collect_message(self, self.get_wool(), 'кг шерсти'))


# колхоз Дядюшки Джо
translator = {
    'Cow': 'корова',
    'Goose': 'гусь',
    'Sheep': 'овца',
    'Hen': 'курица',
    'Goat': 'коза',
    'Duck': 'утка'
}
heaviest_animal = None
goose_0 = Goose('Серый')
goose_1 = Goose('Белый')
cow = Cow('Манька')
sheep_0 = Sheep('Барашек')
sheep_1 = Sheep('Кудрявый')
hen_0 = Hen('Ко-Ко')
hen_1 = Hen('Кукареку')
goat_0 = Goat('Рога')
goat_1 = Goat('Копыта')
duck = Duck('Кряква')
animals = [goose_0, goose_1, cow, sheep_0, sheep_1, hen_0, hen_1, goat_0, goat_1, duck]

goose_0.to_feed(100)
goose_1.to_feed(50)
cow.to_feed(7000)
sheep_0.to_feed(500)
sheep_1.to_feed(1000)
hen_0.to_feed(50)
hen_1.to_feed(100)
goat_0.to_feed(100)
goat_1.to_feed(50)
duck.to_feed(100)
sheep_1.to_trim(3)
for animal in animals:
    animal.collect()
    if heaviest_animal is None:
        heaviest_animal = animal
    elif animal.get_weight() > heaviest_animal.get_weight():
        heaviest_animal = animal
total_weight = (goose_0 + goose_1) + (cow + sheep_0) + (sheep_1 + hen_0) + (hen_1 + goat_0) + (goat_1 + duck)

print('Общий вес животных: ', total_weight)
print('Самое тяжелое животное: {} {}'.format(translator[str(heaviest_animal.__class__).split('.')[1][:-2]],
                                             heaviest_animal.name))
