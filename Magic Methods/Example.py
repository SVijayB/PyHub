def doc():
    """
# Without using Magic Methods : 
dict1 = {"firstname":"vijay"}
dict2 = {"lastname":"balaji"}
print(dict1+dict2)
    """
print(doc.__doc__)
print("Using Magic Methods : ")
class dictionary(dict):
    def __add__(self,other):
        self.update(other)
        return dictionary(self)

dict1 = dictionary({"firstname":"vijay"})
dict2 = dictionary({"lastname":"balaji"})
print(dict1+dict2)