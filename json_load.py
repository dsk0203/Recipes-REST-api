# load the json data
import json


# loads data from drive
def load_recipes(path=None):
    if path == None:
    
        with open(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\test.json",
                encoding='utf-8',errors='ignore') as json_import:
            recipes = json.load(json_import)
    return recipes


# peek function to show number of lines ** Thought was dictionary but ended up being list
def peek(lines=10):
    r = load_recipes()
    import numpy as np
    ran = np.random.randint(0,len(r))
    print(r[0:lines])

# clean input array
def clean(lst):



if __name__ == '__main__':
    peek(20)
