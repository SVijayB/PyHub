print("\nDefining method with the same name but changing the number of arguments the function can be called with",
"is called Method Overloading")

class Overloading():
    def run(self,name=None):
        if(name==None):
            print("Sorry, I did not receive any name")
        else:
            print("Your name is :",name)

o = Overloading()
o.run()
o.run("Vijay")
 
print("\nThat is, we can call the method \"run\" in two ways.")
