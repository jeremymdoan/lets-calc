from urllib import request
from flask import Flask
from flask import request
from flasgger import Swagger
from mathFunctions.functionList import functions
from mathFunctions.euclideanAlgorithm import euclideanAlgorithm
from mathFunctions.euclideanAlgorithmIterative import euclideanAlgorithmIterative
from mathFunctions.gauss import gauss
from mathFunctions.gauss_np import gaussian_elimination as gauss_np
from mathFunctions.leastCommonMultiple import leastCommonMultiple
from mathFunctions.quadractricFormula import quadractricFormula
from utils.paramCheck import aAndBParams, guassParams, aBandCParams
from swagger_stuff import template, swagger_config

app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': "Let's calc!",
    'uiversion': 3
}
swagger = Swagger(app)

@app.route("/")
def hello_world():
    return '<p>Math Functions.</p><p><a href="/apidocs">API Docs</a></p>'

@app.route("/tos")
def tos():
    return "<p>Please don't use this to harm anyone.</p>"

@app.route('/list', methods=['GET'])
def list():
    """ Returns a list of available functions
    ---
    tags:
    - Functions
    produces:
      - application/json
    definitions:
        Functions:
            type: array
            items:
                $ref: '#/definitions/Function'
        Function:
            type: object
            properties:
            name:
                type: string
                description: name of function
                example: Quadratic Equations
            path:
                type: string
                description: path to function endpoint
                example: /quadraticEquations
            algorithms:
                type: array
                desciption: list of possible algorithms implemented for each function
                items:
                type: string
            default:
                type: string
                description: name of the default algorithm if none specified
            limitiations:
                type: array
                description: list of limitations of the implemented algorithms
                items:
                type: string
    responses:
        200:
            description: A list of calculations and the path to the endpoint
            schema:
                id: Functions
                type: array
                items:
                    schema:
                        id: Function
                        type: object
                        properties:
                            name:
                                type: string
                                description: name of function
                                example: Quadratic Equations
                            path:
                                type: string
                                description: path to function endpoint
                                example: /quadraticEquations
                            algorithms:
                                type: array
                                desciption: list of possible algorithms implemented for each function
                                items:
                                type: string
                            default:
                                type: string
                                description: name of the default algorithm if none specified
                            limitiations:
                                type: array
                                description: list of limitations of the implemented algorithms
                                items:
                                type: string
    """
    return {
        'functions': functions
    }

@app.route('/gcf', methods=['POST'])
def gcf():
    """ Greatest Common Factor
    ---
    tags:
    - Functions
    produces:
      - application/json
    parameters:
        - name: input params
          in: body
          type: object
          schema:
            type: object
            properties:
                params:
                    type: object
                    properties:
                        a:
                            type: integer
                            format: int32
                            example: 12
                        b:
                            type: integer
                            format: int32
                            example: 13
                    required: true
                algorith:
                    type: string
                    example: Euclid
          default: all
    responses:
        200:
            description: GCF of two integers
            schema:
                id: Solution
                type: object
                properties:
                    solutions:
                        type: array
                        description: one (or more if applicable) solutions from function
                        items:
                            type: integer
                            format: int32
                            example: 3
                    success:
                        type: string
                        description: says whether or not function was successful
                        example: Success
        400:
            description: Bad request, missing some inputs
            schema:
                id: Error
                type: object
                properties:
                    success:
                        type: string
                        description: says whether or not function was successful
                        example: Error
                    msg:
                        type: string
                        description: error message if status is Error
                        example: you didn't provide the right params or whatever
    """
    data = request.get_json()
    if aAndBParams(data):
        return {
            'status': 'Error',
            'msg': 'Must supply params with values for a and b and c (even if zero for any)'
        }, 400
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
def lcm():
    """ Least Common Multiple
    ---
    tags:
    - Functions
    produces:
      - application/json
    parameters:
        - name: input params
          in: body
          type: object
          schema:
            type: object
            properties:
                params:
                    type: object
                    properties:
                        a:
                            type: integer
                            format: int32
                            example: 12
                        b:
                            type: integer
                            format: int32
                            example: 13
                    required: true
          default: all
    responses:
        200:
            description: LCM of two integers
            schema:
                id: Solution
                type: object
                properties:
                    solutions:
                        type: array
                        description: one (or more if applicable) solutions from function
                        items:
                            type: integer
                            format: int32
                            example: 3
                    success:
                        type: string
                        description: says whether or not function was successful
                        example: Success
        400:
            description: Bad request, missing some inputs
            schema:
                id: Error
                type: object
                properties:
                    success:
                        type: string
                        description: says whether or not function was successful
                        example: Error
                    msg:
                        type: string
                        description: error message if status is Error
                        example: you didn't provide the right params or whatever
    """
    data = request.get_json()
    if aAndBParams(data):
        return {
            'status': 'Error',
            'msg': 'Must supply params with values for a and b'
        }, 400
    else:
        solution = leastCommonMultiple(data['params']['a'], data['params']['b'])
        return {
            'status': 'Sucess',
            'solution': solution
        }

@app.route('/systemOfEquations', methods=['POST'])
def systemOfEquations():
    data = request.get_json()
    if guassParams(data):
        return {
            'status': 'Error',
            'msg': 'Must supply params with a n x n+1 matrix'
        }, 400
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
def quadraticEquations():
    """ Quadratic Equations
    ---
    tags:
    - Functions
    produces:
      - application/json
    parameters:
        - name: input params
          in: body
          type: object
          schema:
            type: object
            properties:
                params:
                    type: object
                    properties:
                        a:
                            type: integer
                            format: int32
                            example: 2
                        b:
                            type: integer
                            format: int32
                            example: 1
                        c:
                            type: integer
                            format: int32
                            example: -1
                    required: true
          default: all
    responses:
        200:
            description: GCF of two integers
            schema:
                id: Solution
                type: object
                properties:
                    solutions:
                        type: array
                        description: one (or more if applicable) solutions from function
                        items:
                            type: integer
                            format: int32
                            example: 3
                    success:
                        type: string
                        description: says whether or not function was successful
                        example: Success
        400:
            description: Bad request, missing some inputs
            schema:
                id: Error
                type: object
                properties:
                    success:
                        type: string
                        description: says whether or not function was successful
                        example: Error
                    msg:
                        type: string
                        description: error message if status is Error
                        example: you didn't provide the right params or whatever
    """
    data = request.get_json()
    if aBandCParams(data):
        return {
            'status': 'Error',
            'msg': 'Must supply params with values for a and b and c (even if zero for any)'
        }, 400
    else:
        solution = quadractricFormula(data['params']['a'], data['params']['b'], data['params']['c'])
        return {
            'status': 'Success',
            'solution': solution
        }