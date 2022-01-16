#!/usr/bin/env python
from flask import (Flask, jsonify, request, abort, render_template)
import requests
import business_logic

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5001


@app.route("/shutdown", methods=['GET'])
def shutdown():
    shutdown_func = request.environ.get('werkzeug.server.shutdown')
    if shutdown_func is None:
        raise RuntimeError('Not running werkzeug')
    shutdown_func()
    return "Shutting down..."


def stop(port=5001):
    requests.get(f'http://localhost:{port}/shutdown')


@app.route('/add', methods=['GET'])
def add_args():
    return jsonify({"result": business_logic.add(*process_request(request))}), 200


def process_request(request):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return a, b


@app.route('/substract', methods=['GET'])
def substract_args():
    a, b = process_request(request)
    return jsonify({"result": business_logic.substract(*process_request(request))}), 200


@app.route('/multiply', methods=['GET'])
def multiply_args():
    return jsonify({"result": business_logic.multiply(*process_request(request))}), 200


@app.route('/divide', methods=['GET'])
def divide_args():
    return jsonify({"result": business_logic.divide(*process_request(request))}), 200


@app.route('/mod', methods=['GET'])
def mod_args():
    return jsonify({"result": business_logic.mod(*process_request(request))}), 200


@app.route('/exp', methods=['GET'])
def exp_args():
    return jsonify({"result": business_logic.exp(*process_request(request))}), 200


@app.route('/average', methods=['GET'])
def average_args():
    return jsonify({"result": business_logic.average(*process_request(request))}), 200


@app.route('/log', methods=['GET'])
def log_args():
    return jsonify({"result": business_logic.log(*process_request(request))}), 200


def run(host, port):
    app.run(debug=False, host=host, port=port)
    return app


if __name__ == '__main__':
    run(HOST, PORT)
