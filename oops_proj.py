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
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

# write logic from here

    def signup(self):
        email = input("enter your email here ")
        password = input("setup your password here ")
        self.username = email
        self.password = password
        print("You have signed up successfully")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email here ")
            password = input("enter your password here ")
            if self.username==uname and self.password == password:
                print("You have signed in successfully")
                self.loggedin = True
            else:
                print("Input the correct credentials")
        print("/n")
        self.menu()        
    
      




#Define an object now
obj = chatbook()     
