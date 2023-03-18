from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/account/<int:user_id>', methods=['GET'])
def get_account(user_id):
    # get account details from another service
    response = requests.get(f'http://localhost:5002/account/{user_id}')
    account_data = response.json()
    
    # return account details
    return jsonify(account_data)


#this file functions separately from the rest, and would not affect the other files once it fails