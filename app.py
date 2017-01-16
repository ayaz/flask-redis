from flask import Flask, request, jsonify
from flask_redis import FlaskRedis
import requests
import json
import os
import os.path
from datetime import datetime


app = Flask(__name__)
try:
    app.config['REDIS_URL'] = os.path.join(os.environ['REDIS_URL'], '0')
except:
    app.config['REDIS_URL'] = 'redis://{}:{}/{}'.format(
            os.environ['REDIS_PORT_6379_TCP_ADDR'],
            int(os.environ.get('REDIS_PORT_6379_TCP_PORT', 6379)),
            0)
redis_store = FlaskRedis(app)

@app.route('/hit', methods=['GET'])
def get_faqs():
    """Return a list of FAQ titles and their links.
    """
    results = 'OK %s' % app.config['REDIS_URL']
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
        results = 'ERROR: query and value params missing'
    return results

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
