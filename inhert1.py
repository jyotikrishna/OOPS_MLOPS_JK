#Super keyword

class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def __init__(self, breed):
        super().__init__()          # using super keyword so that I can access both the parent and child constructor
        self.breed = breed

    def speak(self):
        super().speak()             #Call the parent menthod by using super().
        print(f"{self.name} barks. It is a {self.breed}.")

dog=Dog("Golden Retriever")
dog.speak()
