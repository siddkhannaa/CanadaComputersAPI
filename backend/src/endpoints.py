from flask_restful import Resource

from flask import jsonify, request

from services import product_search

# parser = reqparse.RequestParser()
# parser.add_argument('search_string')

memes ={}

class Uwu(Resource):
    def get(self, memeID):
        # resp = jsonify({'meme': 'cat'})
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        return {memeID: memes[memeID]}
    
    def put(self, memeID):
        memes[memeID] = request.form['data']
        return {memeID: memes[memeID]}

# searches = {}

class Search(Resource):
    def get(self, search_string):
        # args = parser.parse_args() # nargs incoming
        # searches[search_string] = request.form['data']
        args = request.args
        print(args)
        low = args.get('price_min', None)
        high = args.get('price_max', None)
        resp = jsonify(product_search(search_string, low, high))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.status_code = 201
        # print(resp)
        return resp
    
    # def post(self):
    #     args = parser.parse_args() # nargs incoming
    #     # searches[search_string] = request.form['data']
    #     resp = jsonify(product_search(args['search_string']))
    #     resp.headers['Access-Control-Allow-Origin'] = '*'
    #     resp.status_code = 201
    #     # print(resp)
    #     return resp
    #     # return {'noob': 'boon'}, 201