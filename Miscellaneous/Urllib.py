import urllib.request

data = urllib.request.urlopen("https://official-joke-api.appspot.com/random_ten")
data = data.read().decode()
print(data)
file = open("content.txt", "w+")
file.write(data)
file.close()
