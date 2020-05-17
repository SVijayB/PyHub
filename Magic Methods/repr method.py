class measurement:
    value = {"mm":0.001, "cm":0.01, "m":1 , "km":1000, "in":0.0254,
         "ft":0.3048, "yd":0.9144, "mi":1609.344}   # Converting to meters.
        
    def __init__(self, x, unit="m"):
        self.x = x
        self.unit = unit
    
    def convertor(self):
        return self.x * measurement.value[self.unit]

    def __add__(self,other):
        ans = self.convertor() + other.convertor()
        return measurement(ans)
    
    def __str__(self):      # Converts into string
        return str(self.convertor)  
    
    def __repr__(self):     # Evaluates -> representation
        return "After Convertion : " + str(self.x) + "m"

if __name__ == "__main__":
    a = measurement(5.5, "yd") 
    b = measurement(5.5, "in") 
    obj = a+b
    print(repr(obj))        # For printing the representation of the answer
    # print(obj)            # For printing the object reference
