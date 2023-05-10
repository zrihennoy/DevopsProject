from flask import request,Flask

import db_connector

app = Flask(__name__)


@app.route("/users/get_user_data/<user_id>")
def get_user_name(user_id):
    user_name = db_connector.get_username(user_id)
  #  if user_name == None:
   #     return "<H1 id='error'> no such user: " + user_id + "</H1>"
    return "<H1 id='user'>" + user_name + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)