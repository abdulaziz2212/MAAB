from abc import ABC, abstractmethod

'''
Since we want each subclass should have own eat method
we use abstract method to force each subclass to initialize its eat() method
'''
class Animal(ABC):
    def __init__(self,name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def eat(self):
        pass

    def sleep(self):
        print(f'{self.name} is sleeping')

    def speak(self):
        print(f"{self.name} makes unknown sound. ")

    def __str__(self):
        return f"Name: {self.name}, Species: {self.species}"
    
class Monkey(Animal):
    def eat(self):
        print(f"{self.name} is eating a banana")

    def speak(self):
        print(f"{self.name} is chattering")

class Wolf(Animal):
    def eat(self):
        print(f"{self.name} is eating meat")

    def hunt(self):
        print(f"{self.name} is hunting")
    
    def speak(self):
        print(f"{self.name} is howling. ")

class Cow(Animal):
    def eat(self):
        print(f"{self.name} is eating  grass")

    def moo(self):
        print(f"{self.name} is mooing")

    def speak(self):
        print(f"{self.name} says moo! ")

monkey=Monkey('Jumavoy','Primate')
wolf=Wolf("Romul",'Predator')
cow=Cow("Bessie",'Bovine')
print(monkey)