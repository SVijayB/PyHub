import requests

# GET request
data = {"title": "test", "userId": "1675", "id": 546547, "completed": True}
response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
print(response.text)

# POST request
response = requests.get("https://jsonplaceholder.typicode.com/todos/101")
print(response.text)

# PUT request
data = {"title": "updated title", "body": "updated body"}
response = requests.put("https://jsonplaceholder.typicode.com/posts/1", data=data)

# DELETE request
print(response.text)
response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)

# Parsing request responses
print(response.headers)
print(response.text)
print(response.status_code)
