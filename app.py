from urllib import request
from flask import Flask, request, render_template
from flasgger import Swagger, swag_from
from mathFunctions.functionList import functions
from mathFunctions.euclideanAlgorithm import euclideanAlgorithm
from mathFunctions.euclideanAlgorithmIterative import euclideanAlgorithmIterative
from mathFunctions.gauss import gauss
from mathFunctions.gauss_np import gaussian_elimination as gauss_np
from mathFunctions.leastCommonMultiple import leastCommonMultiple
from mathFunctions.quadractricFormula import quadractricFormula
from utils.paramCheck import aAndBParams, guassParams, aBandCParams
from swagger_stuff import template, swagger_config
from customErrors import err400

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': "Let's calc!",
    'uiversion': 3
}
swagger = Swagger(app)

@app.route("/")
def hello_world():
    return render_template('landing.html')

@app.route("/tos")
def tos():
    return "<p>Please don't use this to harm anyone.</p>"

@app.route('/list', methods=['GET'])
@swag_from('./specs/list.yml')
def list():
    return {
        'functions': functions
    }

@app.route('/gcf', methods=['POST'])
@swag_from('./specs/gcf.yml')
def gcf():
    data = request.get_json()
    if aAndBParams(data):
        return err400('Must supply params with values for a and b and c (even if zero for any)')
    else:
        if data.get('algorithm') != None and data['algorithm'] == 'Euclid Iterative':
            solution = euclideanAlgorithmIterative(data['params']['a'], data['params']['b'])
        else:
            solution = euclideanAlgorithm(data['params']['a'], data['params']['b'])
        return {
            'status': 'Sucess',
            'solution': solution
        }

@app.route('/lcm', methods=['POST'])
@swag_from('./specs/lcm.yml')
def lcm():
    data = request.get_json()
    if aAndBParams(data):
        return err400('Must supply params with values for a and b')
    else:
        solution = leastCommonMultiple(data['params']['a'], data['params']['b'])
        return {
            'status': 'Sucess',
            'solution': solution
        }

@app.route('/systemOfEquations', methods=['POST'])
@swag_from('./specs/systemOfEquations.yml')
def systemOfEquations():
    data = request.get_json()
    if guassParams(data):
        return err400('Must supply params with A = n x n matrix and x = n x 1 array')
    else:
        A = data['params']['A']
        x = data['params']['x']
        if data.get('algorithm') != None and data['algorithm'] == 'Gauss':
            solution = gauss(A, x)
        else:
            x = [[n] for n in x]
            solution = gauss_np(A, x)
        return {
            'status': 'Success',
            'solution': solution
        }

@app.route('/quadraticEquations', methods=['POST'])
@swag_from('./specs/quadraticEquations.yml')
def quadraticEquations():
    data = request.get_json()
    if aBandCParams(data):
        return err400('Must supply params with values for a and b and c (even if zero for any)')
    else:
        solution = quadractricFormula(data['params']['a'], data['params']['b'], data['params']['c'])
        return {
            'status': 'Success',
            'solution': solution
        }