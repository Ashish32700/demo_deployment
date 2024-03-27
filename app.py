from flask import Flask, jsonify, request 

app = Flask(__name__) 


@app.route('/', methods=['GET']) 
def helloworld(): 
	return "hello, ashish this is your first deploy!"


