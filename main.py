from Intances.FileHandler import FileHandler
import Model.PLModel as PLModel
import os

file = os.path.join(os.getcwd(), "instances.txt")
fh = FileHandler(filepath=file)

instances = fh.read_instances()

for instance in instances:
    PLModel.create_model(instance)