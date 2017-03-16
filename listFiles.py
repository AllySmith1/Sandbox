
import os

print("The files and foldes in {} are: ".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)

