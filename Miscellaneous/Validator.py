from cerberus import Validator

schema = {'numbers': {'type': 'integer'}}
v = Validator(schema)
data = {'numbers': 5}

if v.validate(data):
	print("Data is valid")
else:
    print("Data is invalid")


v.schema = {'name': {'required': True, 'type': 'string'},
            'age': {'type': 'integer'}}

if v.validate({'age': 34}):
    print('valid data')
else:
    print('invalid data')
    print(v.errors)

v.schema = {'name': { 'type': 'string', 'minlength': 5},
    'age': {'type': 'integer', 'min': 18, 'max': 65}}

if v.validate({'name': 'VJ', 'age': 16}):
    print('Data is valid')
else:
    print('Data is invalid')
    print(v.errors)

