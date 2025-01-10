# 📊 Weather and Social Media Activity Analysis

## 🌐 Project Overview

This project explores how **Istanbul's 2024 weather** affects user engagement on **TikTok** and **Instagram**. By analyzing weather conditions and social media activity data, the project identifies patterns, correlations, and predicts engagement behavior using machine learning.

---

## 🗂️ Folder Structure

📦 weather-social-media-analysis
├── 📂 data
│   ├── istanbul_2024_weather.csv        # Weather data for Istanbul in 2024  
│   ├── liked_comments.json              # Instagram liked comments data  
│   ├── liked_posts.json                 # Instagram liked posts data  
│   └── user_data_tiktok.json            # TikTok activity data  
├── 📂 notebooks
│   ├── 01_data_preprocessing.ipynb      # Data loading and preprocessing  
│   ├── 02_exploratory_data_analysis.ipynb # Exploratory data analysis (EDA)  
│   ├── 03_statistical_analysis.ipynb    # Correlation and statistical analysis  
│   └── 04_modeling.ipynb                # Predictive modeling (Random Forest)  
├── 📂 scripts
│   ├── data_preprocessing.py            # Data cleaning and merging  
│   ├── eda.py                           # EDA and visualizations  
│   ├── statistical_analysis.py          # Correlation and statistical testing  
│   └── modeling.py                      # Predictive modeling logic  
├── 📂 outputs
│   ├── 📂 figures                       # Plots and visualizations  
│   │   ├── interaction_distribution.png  
│   │   ├── activity_over_time.png  
│   │   ├── activity_vs_temp.png  
│   │   └── weather_correlation_heatmap.png  
│   └── 📂 reports                      # Statistical results and model performance  
│       ├── correlation_temp.txt  
│       ├── t_test_Rain.txt  
│       └── model_evaluation.txt  
├── README.md                            # Project documentation  
├── requirements.txt                     # Python dependencies  
└── .gitignore                           # Files to ignore in version control  

---

## 📈 Key Findings

- **Temperature** is **negatively correlated** with social media engagement.

  - 📉 Higher temperatures lead to **lower activity**.
  - 📄 (Pearson correlation: **-0.5920**, p-value: **0.0000**)

- **Rain** does **not significantly** affect engagement.

  - 📄 T-test result: **No significant difference** between rainy and non-rainy days.

- A **Random Forest model** predicts high/low activity with **~73% accuracy**.
  - 📄 Better at predicting **high activity days** than low activity days.

---

## 🛠️ Project Setup

### 1. **Install Dependencies**

bash
pip install -r requirements.txt

### 2. **Run Jupyter Notebook**

bash
jupyter notebook

### 2. **Execution Order**

    1.	01_data_preprocessing.ipynb → Loads and merges data.
    2.	02_exploratory_data_analysis.ipynb → Generates visualizations.
    3.	03_statistical_analysis.ipynb → Performs statistical testing.
    4.	04_modeling.ipynb → Trains the Random Forest model.

## 📊 Results Preview

Social Media Activity vs Temperature
• Instagram activity is higher during cooler weather.
• TikTok activity peaks during warmer weather.

Interaction Distribution
• Instagram has far more engagement, especially through Liked Posts.
• TikTok engagement is mainly through Favorite Videos.

Model Performance
• Accuracy: 73%
• Confusion Matrix: Model is better at predicting high activity days.

## 🔍 Tools & Technologies

    •	Python
    •	Pandas, NumPy – Data processing
    •	Matplotlib, Seaborn – Visualization
    •	Scikit-learn – Machine learning
    •	Jupyter Notebook – Interactive analysis

## 📄 License

This project is for educational purposes only.

## ✨ Acknowledgments

    •	TikTok and Instagram activity data provided by the user.
    •	Weather data for Istanbul 2024.
