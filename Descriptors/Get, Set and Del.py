# get method -> get(self,instance,owner)
# self method -> set(self,instance,value)
# delete -> delete(self,instance)
# Examples :


class cel:
    def __get__(self, instance, owner):
        return 5 * (instance.x - 32) / 9  # Returns value of the attribute.

    def __set__(
        self, instance, value
    ):  # Returned value from get is used as the second attribute.
        instance.x = 32 + 9 * value / 5


class temp:
    y = cel()

    def __init__(self, x):
        self.x = x


t = temp(112)
print(t.y)
t.y = 0
print(t.x)

input("Press Enter key to exit ")
