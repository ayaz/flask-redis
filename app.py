from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
import requests
import json
import os
import os.path
from datetime import datetime


app = Flask(__name__)
app.config['REDIS_URL'] = os.path.join(os.environ['REDIS_URL'], '0')
redis_store = FlaskRedis(app)

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
