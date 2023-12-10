#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


all_objs = storage.all()
print(type(all_objs))
print(len(all_objs))
print("I am here can you do that pleeeeeeeeeeeeeease only for me")
GGpro = all_objs.values()
print(f"MY type is ... {type(GGpro)}")
print(GGpro)
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
