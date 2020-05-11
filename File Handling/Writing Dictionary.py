# Writing into a JSON file
import json
dict = {"Name":"1StranGe","Age":"19","Gender":"Male"}
path = "assets\File Handling\Json.json"
json = json.dumps(dict)
file = open(path,"w+")
file.write(json)
file.close()

# Writing into a pickle file.
import pickle
dict = {"Name":"1StranGe","Age":"19","Gender":"Male"}
path = "assets\File Handling\Pickle.pkl"
file = open(path,"wb")          # For pickle files use WB - Write and read from a binary file.
pickle.dump(dict,file)
file.close()