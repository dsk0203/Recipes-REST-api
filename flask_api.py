# Flask api
from flask import Flask, jsonify, request
import pickle

app = Flask(__name__)

@app.route('/recipes', methods=['GET'])
def get_ingred_list():
    # change location of serialized dictionary??
    with open(r"C:\Users\dsk02\Desktop\python_projects\nn_recipes\recipes_dict.pickle", 'rb') as handle:
        b = pickle.load(handle)

    
    ingred_list = str(request.args.getlist("i"))
    
    # hold array for recipes
    recipe_hold = []
    
    # cycle through different ingredients passed
    for each_ingredient in ingred_list:
        
        # append to the hold array
        recipe_hold.append(b[each_ingredient])
    
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
