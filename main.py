from flask import Flask, jsonify, make_response, send_file
from flask_restful import Resource, Api, reqparse
import ast


app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/<department>/<form>/<group>', methods=['GET'])
def get_calendar(department, form, group):
    return department + form + group


@app.route('/')
def index():
    return "Hello, World!"
    
    
if __name__ == '__main__':
    app.run(debug=True)
