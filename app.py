import streamlit as st
import pandas as pd
from surprise import Dataset, Reader, KNNBasic

df = pd.read_csv("interactions.csv")
movies_df = pd.read_csv("movies.csv")
movies_df.columns = movies_df.columns.str.strip()  

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['userId', 'itemId', 'rating']], reader)
trainset = data.build_full_trainset()
model = KNNBasic(sim_options={'user_based': True})
model.fit(trainset)

def get_recommendations(user_id, top_n=5):
    items = df['itemId'].unique()
    rated_items = df[df['userId'] == user_id]['itemId'].values
    unrated_items = [item for item in items if item not in rated_items]

    predictions = []
    for item_id in unrated_items:
        pred = model.predict(user_id, item_id)
        predictions.append((item_id, pred.est))

    predictions.sort(key=lambda x: x[1], reverse=True)
    top_items = predictions[:top_n]

    results = []
    for movie_id, score in top_items:
        title = movies_df[movies_df['movieId'] == movie_id]['title'].values
        title = title[0] if len(title) > 0 else f"Movie {movie_id}"
        results.append((title, score))
    
    return results

st.title("🎬 Movie Recommender")

user_id = st.number_input("Enter User ID:", min_value=1, step=1)

if st.button("Get Recommendations"):
    recommendations = get_recommendations(user_id)
    st.subheader("Top Recommended Movies:")
    for title, score in recommendations:
        st.write(f"🎬 {title} — Predicted Rating: {score:.2f}")
