# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_redis import FlaskRedis

import redis

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
redis_client = FlaskRedis(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

total_spus = redis_client.get('total_spus')
if total_spus is None:
  total_spus = 0
else:
  total_spus = int(total_spus)

@app.route('/spu_count', methods=['GET', 'POST'])
def spu_count():
  global total_spus
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    if int(post_data['seq']) <= total_spus:
      total_spus += 1
    else:
      total_spus = int(post_data['seq'])
    redis_client.set('total_spus', total_spus)
    spu = "{}-{}{:03d}{}".format(post_data['prefix'], post_data['date'], total_spus % 1000, post_data['category'].upper())
    response_object['spu_count'] = total_spus
    response_object['spu'] = spu
  else:
    response_object['spu_count'] = total_spus

  return jsonify(response_object)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')


if __name__ == '__main__':
  app.run()