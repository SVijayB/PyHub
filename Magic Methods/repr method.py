class measurement:
    value = {"mm":0.001, "cm":0.01, "m":1 , "km":1000, "in":0.0254,
         "ft":0.3048, "yd":0.9144, "mi":1609.344}   # Converting to meters.
        
    def __init__(self, x, value_unit="m"):
        self.x = x
        self.value_unit = value_unit
    
    def convertor(self):
        return self.x * measurement.value[self.value_unit]

    def __add__(self,other):
        ans = self.convertor() + other.convertor()
        return measurement(ans/measurement.value[self.value_unit],self.value_unit)
    
    def __str__(self):      # Converts into string
        return str(self.convertor)  
    
    def __repr__(self):     # Evaluates -> representation
        return "After Convertion : " + str(self.x) + " , " + self.value_unit

if __name__ == "__main__":
    obj = measurement(5.5, "yd") + measurement(1)
    print(repr(obj))
    print(obj)
