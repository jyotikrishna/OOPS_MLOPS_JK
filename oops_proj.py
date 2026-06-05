class chatbook:
    #defining attributes and data in this class
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()  #Definining method in the constructor itself


    # Lets create a method now
    def menu(self):
        user_input = input("""Welcome to Chatbook! How would you like to proceed?1. 
                           1. Press 1 to signup.
                           2. Press 2 to sign in 
                           3. Press 3 to write a post. 
                           4. Press 4 to message a friend. 
                           5. Press other key to exit.""")
        if user_input == '1':
            pass
        elif user_input == '2':
            pass
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

   #Define an object
obj = chatbook()     
