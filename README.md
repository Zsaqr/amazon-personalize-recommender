#  Movie Recommendation System using Surprise (SVD)

This project is a personalized movie recommender system using **collaborative filtering** with the Surprise library (SVD algorithm). It predicts movie ratings for users and presents top movie recommendations using an interactive Streamlit UI.

---

##  Features

- ✅ Collaborative Filtering using `Surprise` SVD algorithm
- ✅ Evaluated using RMSE
- ✅ Streamlit interface for user input and live recommendations
- ✅ Automatically maps `movieId` to real movie `title`
- ✅ Lightweight and runs locally

---

##  Project Structure

| File               | Description |
|--------------------|-------------|
| `app.py`           | Streamlit app that runs the recommender |
| `recommender.py`   | Contains the training, prediction, and evaluation logic |
| `movies.csv`       | Movie metadata (movieId + title) |
| `ratings.csv`      | Historical ratings by users |
| `requirements.txt` | Python packages required to run the app |

---

## ▶ How to Run the App

1. **Clone the repository:**
```bash
git clone https://github.com/Zsaqr/amazon-personalize-recommender.git
cd amazon-personalize-recommender
