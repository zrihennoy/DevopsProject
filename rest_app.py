from flask import request,Flask

import db_connector

app = Flask(__name__)
# local users storage

@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            user=db_connector.get_username(user_id)
            return {'status': 'ok', 'user_name': user}, 200 # status code
        except Exception as e:
            return {'user_id': user_id, 'reason': 'no such id'}, 500 # status code
    elif request.method == 'POST':
        try:
            # getting the json data payload from request
            request_data = request.json
            #  treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            db_connector.create_user(user_id,user_name)
            return {'status': 'ok', 'user added': user_name}, 200 # status code
        except Exception as e:
            return {'status': 'error', 'reason': 'id already exists'}, 500
    elif request.method == 'PUT':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            db_connector.update_user(user_id, user_name)
            return {'status': 'ok', 'user_updated': user_id}, 200  # status code
        except Exception as e:
            return {'status': 'error', 'reason': 'no such id'}, 500
    elif request.method == 'DELETE':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            db_connector.delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except Exception as e:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code


app.run(host='127.0.0.1', debug=True, port=5000)