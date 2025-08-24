import numpy as np
import pickle

# Load your precomputed data
with open('model/movie_tag_matrix.pkl', 'rb') as f:
    movie_tag_matrix = pickle.load(f)

tag_sim = np.load('model/tag_sim.npy')

def similar_movies_by_tags(movie_title):
    if movie_title not in movie_tag_matrix.index:
        return [f"'{movie_title}' not found."]
    idx = movie_tag_matrix.index.get_loc(movie_title)
    sim_scores = tag_sim[idx]
    similar_indices = sim_scores.argsort()[::-1][1:6]
    similar_titles = movie_tag_matrix.index[similar_indices].tolist()
    return similar_titles
