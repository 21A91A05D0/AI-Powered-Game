from flask import Flask, request, jsonify
from helper import get_together_api_key
from L4 import start_game  # Import your main loop function

app = Flask(__name__)

@app.route('/start', methods=['GET'])
def start():
    response = start_game()  # Call your main game function
    return jsonify({"message": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
