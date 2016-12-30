from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
import requests
import json
import os
from datetime import datetime

#REDIS_URL = os.environ['REDIS_URL']

app = Flask(__name__)
#app.config.from_object('settings')
#redis_store = FlaskRedis(app)

app.route('/', methods=['GET'])
def index():
    return 'Hi'

@app.route('/hit', methods=['GET'])
def get_faqs():
    """Return a list of FAQ titles and their links.
    """
    query = request.args.get('query', None)
    results = 'OK'
#    if query:
#        results = redis_store.get(query)
#    else:
#        redis_store.set('timestamp', str(datetime.now()))
#        results = 'Redis key stored'
 
    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
