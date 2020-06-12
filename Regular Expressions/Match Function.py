import re

# Basic Match Function
pattern = r"Hey"
sequence = "Hey"

if re.match(pattern, sequence):
    print("Match Found")
else:
    print("Match Not Found")

# Group Function
sequence = "Hello World What Is Going On"
x = re.match(r"(Hello) (World) (What)", sequence)
if (x):
    print(x.group())    # Without argument it returns the entire match word (It has a fixed arg = 0)
    print(x.group(0))
    print(x.group(1))
    print(x.group(2))
    print(x.group(1,3))