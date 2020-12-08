# Flask api
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/recipes', methods=['GET'])
def get_ingred_list():
    # change location of serialized dictionary??
    ingred_list = str(request.args.getlist("ing"))
    return "ingredients are {}.".format(ingred_list)

if __name__ == '__main__':
    app.run(debug=True)
