from flask import Flask
from redis import Redis
from flask import request,json,jsonify,abort
import hashlib
import os

app = Flask(__name__)
redisClient = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return 'Hello World!'


'''
@author:  Badri
@method:  post_message
@request: `/messages`
@method : POST
'''
@app.route('/messages', methods = ['POST'])
def post_message():
    store_messages = {}
    if request.headers['Content-Type'] == 'application/json':
        d = request.json
        sha = hashlib.sha256(d["message"].encode()).hexdigest()
        redisClient.hset("Messages",sha,d["message"])
        return json.dumps({"digest":sha},indent = 2)
    else:
        return json.dumps({"error" : "Unsupported Media Type"},indent = 2)


'''
@author:  Badri
@method:  get_message
@request: `/messages/<digestId>`
@method : GET
'''
@app.route('/messages/<string:digestId>', methods = ['GET'])
def get_message(digestId):
    mess = redisClient.hget("Messages",digestId)
    if mess is not None:
        mess = (str(mess,'utf-8'))
        return json.dumps({'message':mess},indent = 2)
    else:
        return json.dumps({"err_msg": "Message not found"},indent = 2), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)