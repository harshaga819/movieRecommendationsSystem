from flask import Flask, render_template, request, jsonify
import json
from utils.recommend import recommend_movies
from utils.download_files import download_large_files

app = Flask(__name__)

# Automatically download model files if not present
download_large_files()

# Load list of movie titles for dropdown
with open('model/movie_titles.json') as f:
    movie_titles = json.load(f)

@app.route('/')
def home():
    return render_template('index.html', movie_titles=movie_titles)

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie = data.get('movie')
    recommendations = recommend_movies(movie)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
