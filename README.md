# Movie Recommendation System

This is a **content-based movie recommendation system** built using **Flask**, **Python**, and **Machine Learning**.  
It suggests similar movies based on user-selected titles using precomputed similarity matrices.

---

## Features

-  Content-Based Recommendations  
-  Simple and responsive web interface (HTML, CSS, JS)  
-  Automatic model file download from Google Drive (for deployment)  
-  Ready to deploy on platforms like **Render** or **Railway**

---

## Project Structure
```
MovieRecommendationWebApp/
│
├── app.py                        # Main Flask app
├── requirements.txt              # Project dependencies
│
├── model/
│   ├── movie_titles.json         # List of movie names for dropdown
│   ├── tag_sim.npy               # Large similarity matrix (auto-downloaded)
│   └── movie_tag_matrix.pkl      # Movie-tag matrix (auto-downloaded)
│
├── utils/
│   ├── recommend.py              # Recommendation logic
│   └── download_files.py         # Downloads large model files from Google Drive
│
├── static/
│   ├── css/
│   │   └── style.css             # Styling for frontend
│   └── js/
│       └── script.js             # Client-side interactivity
│
├── templates/
│   └── index.html                # Frontend HTML page
│
└── README.md                     # Project documentation
````


---

## How It Works

1. **User selects a movie** from the dropdown list.  
2. The app retrieves similar movies using a **cosine similarity matrix** (`tag_sim.npy`).  
3. The top recommended movies are displayed dynamically on the page.

---

## Model Files (Auto Download Setup)

Large model files are hosted on **Google Drive** and automatically downloaded during app startup.

| File Name | Description | Source |
|------------|-------------|---------|
| `tag_sim.npy` | Precomputed similarity matrix | [Download Link](https://drive.google.com/uc?export=download&id=1MjJDvJjOytQGmDfiKjPHOU0Ve4X0L) |
| `movie_tag_matrix.pkl` | Movie feature matrix | [Download Link](https://drive.google.com/uc?export=download&id=1l99nPAKwbEhiCZLSncsK7i9d8x_3tfyT) |

---

## Installation & Setup

### Clone the Repository
```bash
git clone https://github.com/harshaga819/MovieRecommendationWebApp.git
cd MovieRecommendationWebApp
````
### Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
````

### Install Dependencies
```bash
pip install -r requirements.txt
````
### Run the App
```bash
python app.py
````
---

## Author

Harsh Agarwal

B.Tech in Computer Science and Engineering

