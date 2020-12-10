# Flask api
from flask import Flask, jsonify, request
import pickle


app = Flask(__name__)


@app.route('/recipes', methods=['GET'])
def get_ingred_list():
    
    # opening, change file location on load
    with open(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\recipes_dict.pickle", 'rb') as handle:
            my_recipes = pickle.load(handle)        

    if not len(my_recipes) > 0:
        raise ValueError('could not find the file')
 
    print(my_recipes['egg'])
    #call the ingredient list
    #my_dict = get_dict()

    #check the deserializing became a dictionary
    #if not type(my_recipes) == type(dict):
    #    raise ValueError
    
    # change location of serialized dictionary??       
    ingred_list = str(request.args.getlist("i"))
    
    # hold array for recipes
    recipe_hold = []

    print(ingred_list)

    # cycle through different ingredients passed
    for each_ingredient in ingred_list:

        print(my_recipes[each_ingredient])
        
        # append to the hold array
        recipe_hold.append(my_recipes[each_ingredient])
    
    # i'll write the code for default dictionary
    recipe_count = {}
    for recipe in recipe_hold:
        if recipe not in recipe_count:
            recipe_count[recipe] = 1
        else:
            recipe_count[recipe] += 1
        
    return "you should try cooking {}.".format(max(recipe_count))

if __name__ == '__main__':
    app.run(debug=True)
