class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound
    
    def make_sound(self):
        print(f"The {self.species} makes a {self.sound} sound.")

class Dog(Animal):
    def wag_tail(self):
        print("The dog wags its tail.")

class Cat(Animal):
    def purr(self):
        print("The cat purrs.")

dog = Dog("dog", "bark")
cat = Cat("cat", "meow")

dog.make_sound()  
dog.wag_tail()    

cat.make_sound()  
cat.purr()        
