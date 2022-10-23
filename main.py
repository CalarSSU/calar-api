from flask import Flask, jsonify, make_response, send_file, request
from flask_restful import Api
from waitress import serve
from os.path import exists

from config import *

app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Incorrect request'}), 404)


@app.route('/')
def index():
    return "Hello, World!"


@app.route('/<department>/<form>/<group>', methods=['GET'])
def get_calendar(department, form, group):
    subgroup = request.args.get('subgroup', default='')
    eng = request.args.get('eng', default='false')

    if department not in ALLOWED_DEPARTMENTS:
        return make_response(jsonify({'error': 'Incorrect department'}), 404)
    if form not in ALLOWED_FORMS:
        return make_response(jsonify({'error': 'Incorrect form'}), 404)

    filename = f'{DATA_DIR}/{department}/{form}/{group}x{subgroup}.ics'
    if not exists(filename):
        return make_response(
            jsonify({'error': f'No such group or subgroup {filename}'}), 404)

    return send_file(filename)


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)
