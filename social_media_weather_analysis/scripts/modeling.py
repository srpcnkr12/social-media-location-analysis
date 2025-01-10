import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import os

# Ensure the reports folder exists
REPORTS_DIR = "../outputs/reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

def prepare_model_data(merged_df):
    """
    Prepare data for modeling by labeling high and low activity days based on the median.
    """
    # Aggregate daily interaction counts
    daily_activity = merged_df.groupby('date').size().reset_index(name='interaction_count')
    
    # Median split to classify high vs low activity
    median_activity = daily_activity['interaction_count'].median()
    
    # Label data: 1 for High Activity, 0 for Low Activity
    daily_activity['activity_level'] = (daily_activity['interaction_count'] > median_activity).astype(int)
    
    # Merge with weather data
    weather_features = ['temp', 'humidity', 'precip', 'windspeed', 'cloudcover']
    weather_data = merged_df[['date'] + weather_features].drop_duplicates()
    model_data = pd.merge(daily_activity, weather_data, on='date', how='left')
    
    # Drop missing values
    model_data.dropna(inplace=True)
    
    return model_data, weather_features

def train_activity_prediction_model(model_data, weather_features):
    """
    Train a Random Forest classifier to predict high/low social media activity based on weather.
    Saves model evaluation results to a text file.
    """
    # Features and target
    X = model_data[weather_features]
    y = model_data['activity_level']
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Initialize and train Random Forest model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation Metrics
    confusion = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    
    result = (
        "Confusion Matrix:\n" + str(confusion) + "\n\n"
        "Classification Report:\n" + report + "\n"
        f"Accuracy Score: {accuracy:.4f}\n"
    )
    
    # Save model evaluation to file
    with open(f"{REPORTS_DIR}/model_evaluation.txt", "w") as file:
        file.write(result)
    
    print(result)

def run_model_pipeline(merged_df):
    """
    Full pipeline to prepare data and train the model.
    """
    model_data, weather_features = prepare_model_data(merged_df)
    train_activity_prediction_model(model_data, weather_features)