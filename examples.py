from PolyWrapper import *
connection = PolyWrapper("node2.lunes.host:27106", "Better_Password", "ExampleDB")
# res = connection.insert("helloz", {"suss": "yes"})
# print(res)
# res = connection.insert("hello2", "no")
# print(res)
# res = connection.get("key")
# print(res)
res = connection.update("hello2", {"users": ["hi", "hi"]})
print(res)
res = connection.get()
print(res)
connection.remove('rows')