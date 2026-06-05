# Simple inheritance

#Parent class
class Animal:
    #constructor (general attributes)
    def __init__(self,name): 
        self.name = name

    #method
    def speak(self):
        print(f"{self.name} makes a sound")

#lets make a child class called as Dog‚
class Dog(Animal):  #carry the attributes of parent
    #def __init__(self):        Adding constructor for the child class
     #   self.behaviour = "friendly"

    def speak(self):
        #print(f"Buddy barks. He is very {self.behaviour}")
         #print(f"{self.name} barks. He is very {self.behaviour}")       #constructor overloading! this will show error because the constructor in the child class is overridden on parent.

#animal = Animal("Generic Animal")   #Create an object for Animal class
#animal.speak()


dog = Dog()  #Create an object for Dog Class
dog.speak()