from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # get user details from user service
    response = requests.get(f'http://localhost:5000/user/{user_id}')
    user_data = response.json()
    
    # get account details from account service
    response = requests.get(f'http://localhost:5001/account/{user_id}')
    account_data = response.json()
    
    # combine user and account details and return
    return jsonify({'user': user_data, 'account': account_data})

#same as the others, functions separately to achieve a common objective, in this case, extracting user data from service.