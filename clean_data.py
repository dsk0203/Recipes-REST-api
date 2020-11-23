# clean data 
import pandas as pd
import numpy as np

# import data, clean data, ready to be modeled for nn
# use a partial clean to do modeling, will move to server for full clean
# little laptop guy
def load_split(path=r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\partial_data.csv",num_lines=0):
    path = pd.read_csv(path)
    subset = path[0:num_lines].copy()
    subset.to_csv(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\partial_data.csv")

def load_split():
    return pd.read_csv(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\partial_data.csv")


if __name__ == '__main__':
    comment_me = load_split(path=None,120)
    #df = Partial(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\recipes.csv")
    test = load_split() 
    print('columns from the dataset are listed here {}'.format([c for c in test.columns]))
    print(test.head())

    
    


