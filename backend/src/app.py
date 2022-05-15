from flask import Flask, jsonify, request
from flask_restful import Api

from endpoints import Search, Uwu

app = Flask(__name__)
api = Api(app)

# 
# uwu
# @app.route("/")
# def index():
#     return render_template("index.html", thingo=':flushed:')

api.add_resource(Uwu, '/uwu/<string:memeID>')
api.add_resource(Search, '/search/<search_string>')

if __name__ == '__main__':
    app.run(debug=True)