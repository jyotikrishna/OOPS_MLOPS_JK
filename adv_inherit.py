#(A) Single or basic inheritance

# Parent class 

#class Parent:
 #   def __init__(self, name):
  #      self.name = name

   # def greet(self):
    #    print(f"Hello my name is {self.name}.")

#child class

#class Child(Parent):

 #   def play(self):
  #      print(f"{self.name} is playing.")


#Define child Object

#child = Child("Alice")
#child.greet()
#child.play()


#(B) Multi-level Inheritance

#Base class
#class Grandparent:
#    def __init__(self,name):
#        self.name = name
#    
#    def tell_story(self):
#        print(f"{self.name} tells a story.")


#Intermediate Class
#class Parent(Grandparent):
 #   
  #  def work(self):
   #     print(f"{self.name} is working.")

#Derived Class

#class Child(Parent):

 #   def play(self):
  #      print(f"{self.name} is playing")


#child = Child("Charlie")
#child.tell_story()
#child.work()
#child.play()


# (C) Hierarchical inheritance : 1 parent, multiple childs

#Base Class
#class Parent:
#    def __init__(self, name):
#        self.name = name

 #   def greet(self):
  #      print(f"Hello my name is {self.name}.")


#class Child1(Parent):
#    def play(self):
#        print(f"{self.name} is playing.")

#class Child2(Parent):
#    def study(self):
#        print(f"{self.name} is studying")

#child1 = Child1("Dave")
#child2 = Child2("Eve")

#child1.greet()
#child1.play()

#child2.greet()
#child2.study()

#(D) Multiple  Inheritance (Diamond Problem)

#Base class

#class A:
 #   def __init__(self,name):
  #      self.name = name


   # def greet(self):
    #    print(f"Hello from A, {self.name}.")

#Intermediate Class 1
#class B(A):

 #   def greet(self):
  #      print(f"Hello from B, {self.name}.")
   #     super().greet()             #Constructor taken by Parent class

#Intermediate Class 2
#class C(A):

 #   def greet(self):
  #      print(f"Hello from C, {self.name}.")
   #     super().greet()         #Constructor taken by Parent class

#Derived class
#class D(B,C):
    
 #   def greet(self):
  #      print(f"Hello from D, {self.name}.")
   #     super().greet()         #Constructor taken by Parent class


#Object

#d = D("Frank")
#d.greet()


#(E) Do Hybrid Inheritance