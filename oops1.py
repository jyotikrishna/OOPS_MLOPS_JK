# initiate a class

class employee:  #Create a class called employee
    # Create a data/attribute here. This is called as special method/magic method/dunder method or simply called as constructor.
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/data have been initiated")

    #Create a method/function (Defining a function in class is generally called as method)
    def travel(self, destination):
        print("This travel method has been called manually")
        print(f"Employee is now travelling to {destination}")

# create an object/instance of the class
sam = employee()  #sam is an object of the class employee
#print(sam.salary)

#Calling a method
sam.travel("Kerala")

#print(type(sam)) #type is employee class
