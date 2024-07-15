from flask import Flask, render_template, request, jsonify
import pandas as pd
from models.trend_model import generate_trend, predict_trend_success
from utils.feedback import save_feedback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_trend', methods=['POST'])
def generate_trend_route():
    user_preferences = request.json['preferences']
    new_trend = generate_trend(user_preferences)
    return jsonify(trend=new_trend)

@app.route('/predict_success', methods=['POST'])
def predict_success_route():
    trend_data = request.json['trend']
    prediction = predict_trend_success(trend_data)
    return jsonify(prediction=prediction)

@app.route('/feedback', methods=['POST'])
def feedback_route():
    feedback_data = request.json['feedback']
    save_feedback(feedback_data)
    return jsonify(status='success')

if __name__ == '__main__':
    app.run(debug=True)
