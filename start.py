from flask import Flask, Response, request
from flask_cors import CORS  

app = Flask(__name__)
host_addr = "0.0.0.0"
host_port = 5000


CORS(app, resources={r"/ping": {"origins": "*"}})

@app.route('/')
def hello():
    return "try /ping!"

@app.route('/ping', methods=['POST'])
def ping():
    # response = Response('pong')
    # #response.headers['Access-Control-Allow-Origin'] = 'http://49.50.173.20'
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # return response
    input_data = request.get_json() 
    
    response_data = input_data["data"]
    response = Response(response_data, content_type="application/json")
    
    #response.headers['Access-Control-Allow-Origin'] = 'http://49.50.173.20'
    response.headers['Access-Control-Allow-Origin'] = '*'
    #response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run(debug=True, host=host_addr, port=host_port)