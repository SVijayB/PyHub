"""
Program Description : 
List appender is a simple program that allows you to append data, either a single word or a sequence of words,
to a list. To stop adding elements, type !quit. It helps create lists easily when the number of elements
is a lot.
"""
def List_appender():
    print("Start entering data to be appended to the list")
    ans = ""
    unit = ""
    while(True):
        unit = str(input())
        unit = unit.split()
        for x in unit:
            if(x == "!quit"):
               return ans
            ans = (ans + "\"" + x + "\",")

if __name__ == "__main__":
    list_name = input("Enter the name of the list : ")
    ans = List_appender()
    complete_list = (list_name + " = " + "[" + ans + "\b]")
    print(complete_list)