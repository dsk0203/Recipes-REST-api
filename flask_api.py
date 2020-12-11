# Flask api
from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)


@app.route('/recipes', methods=['GET'])
def get_ingred_list():
    
    # get the ingredient list from the http push (i=egg etc.)   
    ingred_list = (request.args.getlist("i"))
    
    # hold array for recipes
    recipe_hold = []
    
    # hold array for ingredients couldn't find, user passed bad ingredient
    errors = []

    # cycle through different ingredients passed
    for each_ingredient in ingred_list:
    
        # all dictionaries are in lowercase
        each_ingredient = each_ingredient.lower()
       
        # dodge dictionary key errors
        if each_ingredient in my_recipes:
            
            # if the size is > 1000, just grab a random 1000 sample
            if len(my_recipes[each_ingredient]) > 1000:
                recipe_hold.extend(np.random.choice(my_recipes[each_ingredient], 1000))
                
            # else just push all into the recipe hold
            else:
                recipe_hold.extend(my_recipes[each_ingredient])
            
        else:
            # add the error ingredient
            errors.append(each_ingredient)
            
            
    if len(recipe_hold) == 0 and len(errors) == 0:
        return "Ooops, we couldn't find anything, switch it up!"
    elif len(recipe_hold) == 0 and len(errors) != 0:
        return "Couldn't find anything, try switching up these {}".format(errors)

    if len(recipe_hold) >= 2:
    
        # Default dictionary logic
        recipe_count = {}
        
        for each_recipe in recipe_hold:
            
            if each_recipe not in recipe_count:
                recipe_count[each_recipe] = 1
            else:
                recipe_count[each_recipe] += 1
                
        #return logic, depending on errors or not :|
        if len(errors) == 0:
            return "You should try cooking {}".format(max(recipe_count))
        else:
            return "You should try cooking {}, we couldn't find these ingredients {}".format(max(recipe_count), errors)
    else:
        if len(errors) == 0:
            return "You should try cooking {}".format(recipe_count[0])
        else:
            return "You should try cooking {}, we couldn't find these ingredients {}".format(recipe_count[0], errors)
        
# data class load, point to file on desktop for server run --> keep in cache for quick lookups
class data():

    def __init__(self):
    
        # point this to server db
        with open(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\recipes_dict.pickle", 'rb') as handle:
                global my_recipes
                my_recipes = pickle.load(handle)
                print("\n\n\nserver started + data loaded\n\n\n")
        
        # check if recipes is loading 
        if not len(my_recipes) > 0:
            raise ValueError('\n\n\nCould not find the file\n\n\n')
        
    
if __name__ == '__main__':
    data()
    app.run(debug=True)
    
