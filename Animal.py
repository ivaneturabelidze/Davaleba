class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def _info(self):
        print('Name of the animal is ' + self.__name)
        print('The animal is ' + str(self.__age) + ' years old')


class Dog(Animal):
    def __init__(self, species, color):
        self._species = species
        self._color = color
    def _info(self):
        print('info')
