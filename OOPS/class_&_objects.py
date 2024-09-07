class person:
    
    collage_name="IIT Gandhinagar" # Class attribute
    name="anonymous"
    # default constructor
    def __init__(self) :
        pass

    # parameterised constuctor
    def __init__(self, fullname, marks):  #Initialisation of the class 
        self.marks=marks
        self.name=fullname  # Assigning a parameter to a variable in self (object)
        print("Adding new students to database..")
    
    def hello(self):
        print("Welcome Student")

    def get_marks(self):
        return self.marks

s1=person("Lala", 97) # Calling of the class by s1 object
print(s1.name) #printing name variable in s1 object
print(person.collage_name) # Class.attributes format
s1.hello() # Method calling
print(s1.get_marks())
# Object attribute > Class attribute
