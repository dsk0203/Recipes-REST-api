# load the json data
import pandas as pd


# loads data from drive
def load_recipes():
    df = pd.read_csv(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\recipes.csv")
    return df

# peek function to show number of lines ** Thought was dictionary but ended up being list
def peek():
    df = load_recipes()
    print(df.head())

# clean input array
def clean():
   return 1 



if __name__ == '__main__':
    peek()

