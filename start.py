from flask import Flask, Response, request
from flask_cors import CORS  
from transformers import pipeline



app = Flask(__name__)
host_addr = "0.0.0.0"
#host_port = 5000
host_port = 9000 # howon_gpu_013 포트 포워딩! => 8261로 연결하면 9000으로 붙게되어있음
pipe = pipeline("text2text-generation", model="inhee/opus-mt-ko-en-finetuned-ko-to-en5")

CORS(app, resources={r"/ping": {"origins": "*"}})
CORS(app, resources={r"/translate": {"origins": "*"}})

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
@app.route('/translate', methods=['POST'])
def translate():
    
    input_data = request.get_json()
    response_data = input_data["data"]
    return_response = pipe(response_data)

    response = Response(return_response[0]['generated_text'], content_type="application/json")
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    return response
if __name__ == "__main__":
    app.run(debug=True, host=host_addr, port=host_port)
    #app.run(debug=True, host=host_addr)


    
    