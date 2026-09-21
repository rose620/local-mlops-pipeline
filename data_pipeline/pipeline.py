import pandas as pd
from prefect import flow, task
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

@task
def fetch_data():
    """Reads the dataset using dynamic relative paths and cleans column formatting dynamically."""
    print("Reading dataset from local data directory...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", "winequality-red.csv")
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Missing dataset! Looked at: {data_path}")
        
    df = pd.read_csv(data_path, sep=";")
    
    # DEFENSIVE ENGINEERING meaning strip spaces and convert spaces to underscores automatically
    df.columns = df.columns.str.strip().str.replace(' ', '_')
    print(f"Sanitized Column Schema: {list(df.columns)}")
    
    return df

@task
def train_model(df):
    """Handles training and saves the model artifact using dynamic relative paths."""
    print("Training Random Forest model on real dataset...")
    X = df.drop(columns=["quality"])
    y = df["quality"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    api_dir = os.path.join(current_dir, "..", "model_api")
    os.makedirs(api_dir, exist_ok=True)
    
    model_path = os.path.join(api_dir, "wine_model.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved successfully to {model_path}")
    
    return model.score(X_test, y_test)

@flow(name="End-to-End Wine Pipeline")
def run_pipeline():
    data = fetch_data()
    r2_score = train_model(data)
    print(f"Pipeline complete! Model validation R² Score: {r2_score:.4f}")

if __name__ == "__main__":
    run_pipeline()
