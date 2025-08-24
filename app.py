from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import json
from utils.recommend import similar_movies_by_tags

app = Flask(__name__)

# Load movie titles for dropdown
with open('model/movie_titles.json', 'r') as f:
    movie_titles = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', movie_titles=movie_titles)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie_title = data.get('movie')

    recommendations = similar_movies_by_tags(movie_title)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)