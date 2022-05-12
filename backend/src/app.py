from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# 
# uwu
# @app.route("/")
# def index():
#     return render_template("index.html", thingo=':flushed:')

class Uwu(Resource):
    def get(self):
        resp = jsonify({'meme': 'cat'})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

api.add_resource(Uwu, '/')

if __name__ == '__main__':
    app.run(debug=True)