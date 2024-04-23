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


class Shape:
    def __init__(self, color='black'):
        self.color = color

    def get_color(self):
        return self.color

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius, color='red'):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, length, width, color='blue'):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)

shapes = [circle, rectangle]
for shape in shapes:
    print(f"Area of the shape is {shape.area()} units square.")
    print(f"Color of the shape is {shape.get_color()}.")
    print()
