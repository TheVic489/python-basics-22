import json

data = ['foo', {'bar': ('baz', None, 1.0, 2)}]

py_str:   str = str(data)
json_str: str = json.dumps(data)

print(py_str, json_str, sep='\n')

py_data2: list = print(json.loads(json_str))
print(py_data2)

