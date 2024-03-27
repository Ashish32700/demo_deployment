from flask import Flask, jsonify, request 

app = Flask(__name__) 


@app.route('/', methods=['GET']) 
def helloworld(): 
	if(request.method == 'GET'): 
		return "hello, ashish this is your first deploy!"


