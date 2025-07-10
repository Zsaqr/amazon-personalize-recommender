import pandas as pd
from surprise import Dataset, Reader, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy

df = pd.read_csv("interactions.csv") 

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['userId', 'itemId', 'rating']], reader)

trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

model = KNNBasic(sim_options={'user_based': True})  # ممكن تغير لـ item_based=False
model.fit(trainset)

predictions = model.test(testset)
rmse = accuracy.rmse(predictions)
print(f"\n✅ Model trained successfully. RMSE: {rmse:.4f}")

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

    print(f"\n🎯 توصيات للمستخدم {user_id}:")
    for item_id, score in top_items:
        print(f"Movie ID: {item_id}, Predicted Rating: {score:.2f}")

get_recommendations(user_id=1)
