from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    #this gets user details from another device
    response = request.get(f'http://localhost:5001/user/{user_id}')
    user_data = response.json()
    
    #return the user details 
    return jsonify(user_data)