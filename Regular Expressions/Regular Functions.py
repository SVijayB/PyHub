import re
print("""
Different Regular Functions are : 
re.compile(pattern,flags)
re.search(pattern, string, flags)
re.match(pattern,string, flags)
re.split(pattern,string, max,flag)
re.findall(pattern, string, flag)
""")

print("Using the re.compile function")
pattern = "Hello world"
x = re.compile(pattern)
y = x.match("Hello world")
if (y):
    print("Strings match")
else:
    print("Strings do not match")
