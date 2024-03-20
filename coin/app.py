from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flip', methods=['POST'])
def flip_coin():
    data = request.json
    probability_heads = data['probability_heads']
    result = "heads" if random.random() < probability_heads else "tails"
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)