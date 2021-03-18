from flask import Flask, jsonify, request
from datetime import datetime
import time
import threading
import json

app = Flask(__name__)

current_datetime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
current_timestamp = time.time()

#Get file size
def buffer_size(loc, file, dtm, method):

    data = {}
    data[loc] = []

    if method == 'POST':
        data[loc].append({
            'id': str(request.form['ack']),
            'datetime': dtm,
            'd1': str(request.form['d1']),
            'd2': str(request.form['d2']),
            'd3': str(request.form['d3']),
            'd4': str(request.form['d4'])
        })

    else:
        data[loc].append({
            'id': str(request.args.get('ack')),
            'datetime': dtm,
            'd1': str(request.args.get('d1')),
            'd2': str(request.args.get('d2')),
            'd3': str(request.args.get('d3')),
            'd4': str(request.args.get('d4'))
        })

    f = open(loc+"/"+file,'w')
    json.dump(data, f)
    size = json.dumps(data)

    return len(size)

#Function to define result from a request
def response_handler(key, loc, file, method):
    if key == 'bd2722b3-955e-4261-b135-183283cd5515':
        return jsonify({
                'identifier': request.args.get('ack'), 
                'received_datetime': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
                'received_timestamp': current_timestamp,
                'load_datetime': datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
                'load_timestamp': time.time(),
                'bytes': buffer_size(loc, file, current_datetime, method),
                'method': method,
                'success': True
                })
    else:
        return jsonify({'status':404, 'method': method, 'reason':'api unidentified', 'success': False})

#Function to establish connection
@app.route('/test')
def established():
    return jsonify({
            'messages': 'Connection Established',
            'success': True
            })

#Function to handle reponse
@app.route('/<loc>/<file>', methods = ['POST', 'GET'])
def handler(loc, file):

    #POST method handler
    if request.method == 'POST':
        key = request.form['key']
        return response_handler(key, loc, file, request.method)

    #GET method handler
    elif request.method == 'GET':
        key = request.args.get('key')
        return response_handler(key, loc, file, request.method)

    #Other method handler
    else:
        return jsonify({
            'messages': 'Connection established, method not yet developed on server side',
            'success': True
            })

#Main function
def main(port):
    if __name__ == '__main__':
        app.run(debug=False, host='127.0.0.1', port=port)

#Thread manager
port = ["5199"]
cpu = len(port)
for c in range (cpu):
    threading.Thread(target=main, args=(port[c], )).start()