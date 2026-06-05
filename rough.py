lst = [1,2,3]
my_str ="mlops playlist"
my_int = 155

#print(type(lst))
#print(type(my_str))
#print(type(my_int)) 

#List, String and Integer all are class in Python. Hence you know why Python is OOP.

lst.clear() # When you do lst. then you will see many methods.
#print(lst)

#a = 'x'
#b = 'y'
#print(a+b)

#Use of class and object in Python as module
#from oops_proj import chatbook 
#user1 = chatbook()



# function
#lst=[1,2,3]
#a1 = len(lst) # using a function called len 
#print(a1)

# method
#from oops_proj import chatbook 
#user1 = chatbook()
#user1.sendmessage().  #calling a method manually. method is just written under a class and we are calling it using an object.
#just by calling a user, all the attributes are being called and after putting a dot we can decide which attribute to call.
#print(obj.menu())


#Dunder method or magic method
#google dunder methods in python. you will find many __abs__, __add__, __dir__ etc
#algebra is not available in Python but we can do it using dunder method __add__.

#Encapsulation

#from oops_proj import chatbook 


#print(obj.__name) # You cant access this because it is encapsulated
#print(obj._chatbook__name) #To access you need to use this

#Getter and Setter
#Get the hidden attribute and set hidden attribute

#print(obj.get_name())
#obj.set_name("Agent X")
#print(obj.get_name())

#Static Method

#from oops_proj import chatbook 


#obj1 = chatbook()
#print(obj1.id)

#obj2 = chatbook()
#obj2.set_id(10)  # check error here
#print(obj2.id)