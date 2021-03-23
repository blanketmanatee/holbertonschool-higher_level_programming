#!/usr/bin/python3
to_json_string = __import__('3-to_json_string').to_json_string

data = [1, 2, 3, "Holberton"]
s_data = to_json_string(data)
print(s_data)
print(type(s_data))