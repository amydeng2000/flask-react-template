from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS support

@app.route('/users')
def get_users():
    users = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')
