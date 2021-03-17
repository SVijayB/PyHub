# Json manipulation

import json

json_data = '{ "name":"Vijay", "age":20, "city":"Bangalore"}'
output = json.loads(json_data)
print(output["age"])


dict_data = {"name": "Vijay", "age": 20, "city": "Bangalore"}

json_data = json.dumps(dict_data)
print(json_data)

json_data = json.dumps(dict_data, sort_keys=True, indent=4)
print(json_data)

dict = {"Name": "Vijay", "Age": 20, "Gender": "Male"}
path = "assets\Json.json"
json = json.dumps(dict)
file = open(path, "w+")
file.write(json)
file.close()
