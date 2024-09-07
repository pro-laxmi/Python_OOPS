class person:
    __name="Lala"  # To make something that we don't want to edit outside the class like passwords
    def hello(self): 
        __name="Lala"
        print("Hello World")
        print(__name)

p1=person()
print(p1.hello())