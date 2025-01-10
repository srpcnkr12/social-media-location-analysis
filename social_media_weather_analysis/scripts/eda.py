import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure the output folder exists
FIGURE_DIR = "../outputs/figures"
os.makedirs(FIGURE_DIR, exist_ok=True)

def plot_interaction_distribution(merged_df):
    plt.figure(figsize=(8, 6))
    sns.countplot(data=merged_df, x='platform', hue='interaction')
    plt.title('Distribution of Social Media Interactions by Platform')
    plt.xlabel('Platform')
    plt.ylabel('Number of Interactions')
    plt.legend(title='Interaction Type')
    plt.tight_layout()
    plt.savefig(f"{FIGURE_DIR}/interaction_distribution.png")
    plt.show()

def plot_activity_over_time(merged_df):
    activity_counts = merged_df.groupby('date').size().reset_index(name='interaction_count')
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=activity_counts, x='date', y='interaction_count')
    plt.title('Daily Social Media Activity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Interactions')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{FIGURE_DIR}/activity_over_time.png")
    plt.show()

def plot_activity_vs_weather(merged_df, weather_feature):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=merged_df, x='platform', y=weather_feature)
    plt.title(f'Social Media Activity vs {weather_feature.capitalize()}')
    plt.xlabel('Platform')
    plt.ylabel(weather_feature.capitalize())
    plt.tight_layout()
    plt.savefig(f"{FIGURE_DIR}/activity_vs_{weather_feature}.png")
    plt.show()

def heatmap_correlation(merged_df):
    numeric_features = ['temp', 'humidity', 'precip', 'windspeed', 'cloudcover']
    correlation_matrix = merged_df[numeric_features].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Between Weather Conditions')
    plt.tight_layout()
    plt.savefig(f"{FIGURE_DIR}/weather_correlation_heatmap.png")
    plt.show()