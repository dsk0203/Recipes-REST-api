# Flask api                                                                                                          
from flask import Flask, request                                                                                     
import pickle5 as pickle                                                                                             
import numpy as np                                                                                                                                                                                                                        
application = Flask(__name__)                                                                                                                                                                                                             

@application.route('/recipes', methods=['GET'])                                                                      
def get_ingred_list():
                                                                                                                                     
    # point this to server db                                                                                            
    with open("/home/ubuntu/flaskapplication/recipes_dict.pickle", 'rb') as handle:                                          
        my_recipes = pickle.load(handle)                                                                                                                                                                                                      
    if not len(my_recipes) > 0:
        raise ValueError('\n\n\nCould not find the file\n\n\n')                                                                                                                                                                               

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

if __name__ == '__main__':                                                                                            
    application.run(host='0.0.0.0', port=8080)            
