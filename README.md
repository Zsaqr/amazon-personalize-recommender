
# 🎬 Movie Recommender System (Collaborative Filtering)

A personalized movie recommender system built using **collaborative filtering (user-based)** with the [Surprise library](http://surpriselib.com/) and a simple **Streamlit web interface**.

---

##  Features

-  Recommends top-rated movies for a given user
-  Trained on MovieLens-style interaction data
-  Uses KNNBasic from Surprise for collaborative filtering
-  Interactive UI built with Streamlit
-  Maps movie IDs to actual movie titles (from `movies.csv`)

---

##  Tech Stack

- Python 3.x
- [Surprise](http://surpriselib.com/) (`scikit-surprise`)
- Pandas
- Streamlit

---

##  Project Structure

```
Movie-Recommender/
│
├── app.py                # Streamlit application
├── recommender.py        # (optional) core training/testing logic
├── interactions.csv      # User-Item-Rating dataset
├── movies.csv            # Movie metadata (movieId, title, genres)
└── README.md             # You're reading it 😉
```

---

##  How It Works

1. Loads user-item ratings from `interactions.csv`
2. Trains a KNNBasic model using Surprise
3. Calculates predicted ratings for unrated movies
4. Displays top-N recommendations in the Streamlit UI

---

##  Sample Screenshot

![Demo](https://via.placeholder.com/800x400.png?text=Movie+Recommender+Demo)

---

##  How to Run

```bash
pip install -r requirements.txt  # (or install pandas, streamlit, scikit-surprise manually)

streamlit run app.py
```

Then open the browser and enter a User ID to get recommendations.

---

##  Example Output

For User 1:

```
🎬 The Shawshank Redemption (1994) — Predicted Rating: 5.00
🎬 Fargo (1996) — Predicted Rating: 4.93
🎬 Twelve Monkeys (1995) — Predicted Rating: 4.87
```

---

##  Notes

- Make sure `interactions.csv` and `movies.csv` are in the same folder as `app.py`
- You can use MovieLens 100k, 1M, or a custom dataset

---

##  Future Ideas

- Add genre-based filters
- Save recommendations as CSV
- Add support for other algorithms (SVD, Matrix Factorization)
- Export app as `.exe` or deploy online

---

##  Author

**Ziad Muhammed Saqr**  
Machine Learning & AI Enthusiast  
[LinkedIn](https://www.linkedin.com/in/ziad-muhammed-saqr-8541b5241/) • [GitHub](https://github.com/)
