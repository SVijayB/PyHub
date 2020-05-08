from abc import ABC,abstractmethod
# ABC = Abstract Base Class. 
class operation(ABC):               # Abstract Class
    @abstractmethod
    def sum(self,a,b):              # Abstract Method
        pass    
    @abstractmethod
    def multiple(self,a,b):         # Abstract Method
        pass

class implemented(operation):       # Inheriting the Abstract class.
    def sum(self,a,b):
        print("Sum :",a+b)
    def multiple(self, a, b):
        print("Product :",a*b)

a = implemented()
a.sum(5,6)
a.multiple(5,6)
