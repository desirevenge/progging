class Dog():
    '''простая классовая модель'''

    def __init__(self, name, age, color):
        '''инициализируем атрибуты'''
        self.name = name
        self.age = age
        self.color = color

    def sit(self):
        print(self.name.title() + ' сел')

    def jump(self):
        print(self.name.title() + ' прыгнул')

    def run(self):
        print(self.name.title() + ' побежал')

my_dog_1 = Dog('Топик', 4, 'белый')
my_dog_2  = Dog('Ник', 7, 'рыжий')
my_dog_3 = Dog('Макс', 4, 'черный')

print(my_dog_1.age)
print(my_dog_1.name)
print(my_dog_1.color)

my_dog_1.jump()
my_dog_2.sit()
my_dog_3.run()
