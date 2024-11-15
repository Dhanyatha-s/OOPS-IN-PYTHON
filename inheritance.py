class Cat:

    def sleep(self):
        return "*sleeping*"
    
    def speak(self):
        return "Meow!"
    
    def eat(self):
        return "*eating*"
    
    def hunt(self):
        return "*hunting*"
    
class Percian(Cat): # Inherits the class Cat
    def talk(self):
        return super().speak() # inheirits the properties of the funtion speek from inherited class "Cat" to class "percian"
    
kitty = Percian()

print(kitty.talk())
