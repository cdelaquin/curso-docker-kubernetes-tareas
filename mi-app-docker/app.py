from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

start_time = time.time()

@app.route('/')
def home():
    return jsonify({
        'message': 'Bienvenido a mi aplicación dockerizada',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'OK',
        'uptime': time.time() - start_time
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
