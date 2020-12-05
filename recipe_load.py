# load the json data
import pandas as pd


# loads data from drive
def load_recipes():
    df = pd.read_csv(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\cleaned_data.csv")
    return df

def transition_dictionary():
    return 0
    # write in jupyter notebook......


if __name__ == '__main__':
    new_data = load_recipes()
    print(new_data.sample(n=15))
