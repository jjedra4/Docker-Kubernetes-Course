import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. Load Data
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Feature Engineering (must match what happens in inference)
df['petal_area'] = df['petal_length'] * df['petal_width']

X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'petal_area']]
y = df['species']

# 2. Train
model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)

# 3. Save Model
joblib.dump(model, "iris_model.joblib")
print("Model saved to iris_model.joblib")