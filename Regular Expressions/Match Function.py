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

print("""
Specific Characters : 
.           -> Matches every character except new line characters.
\w          -> Matches any single character digit or underscore.
\W          -> Matches any character which is not in lowercase.
\s          -> Matches single white space character, like spaces, tabs etc.
\S          -> Matches all character that are not part of \s.
\\t          -> Used to match all the tab spaces.
\\n          -> Used to match a new line.
\\r          -> Used to match return.
\d          -> Matches decimal digits from 0-9.
^           -> Matches pattern at the start of the string.
$           -> Matches pattern at the end of the string.
[abc]       -> Matches a,b, or c in the pattern.
[a-zA-Z0-9] -> Matches chatacters within given range.
(0-9)       -> Matches numbers from 0-9.
\\b          -> Matches only the start and end of the word.
\           -> If character following a \ is not an escape character, it acts as a backslash alone.
""")

# Backslash  Case : 
x = re.search(r"Hello\\sWorld","Hello\sWorld").group()
print(x)
x = re.search(r"Hello\sWorld","Hello World").group()
print(x)
