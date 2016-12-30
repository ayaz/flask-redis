from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
import requests
import json
import os
from datetime import datetime

REDIS_URL = os.environ['REDIS_URL']

app = Flask(__name__)
#app.config.from_object('settings')
#redis_store = FlaskRedis(app)

app.route('/root', methods=['GET'])
def index():
    return 'Hi %s' % REDIS_URL

@app.route('/hit', methods=['GET'])
def get_faqs():
    """Return a list of FAQ titles and their links.
    """
    query = request.args.get('query', None)
    results = 'OK %s' % REDIS_URL
    return results

@app.route('/get_key', methods=['GET'])
def get_key():
    query = request.args.get('query', 'timestamp')
    results = redis_store.get(query)
    return str(results)

@app.route('/set_key', methods=['GET'])
def set_key():
    query = request.args.get('query', None)
    value = request.args.get('value', None)
    if query and value:
        redis_store.set(query, value)
        results = 'OK'
    else:
        return 'ERROR: query and value params missing'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
