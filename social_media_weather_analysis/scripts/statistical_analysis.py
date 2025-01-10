import pandas as pd
from scipy.stats import pearsonr, spearmanr, ttest_ind
import os

# Ensure the reports folder exists
REPORTS_DIR = "../outputs/reports"
os.makedirs(REPORTS_DIR, exist_ok=True)

def correlation_analysis(merged_df, weather_feature):
    """
    Perform Pearson and Spearman correlation analysis between weather feature and interaction frequency.
    Saves the results to a text file.
    """
    # Group by date and count interactions
    daily_activity = merged_df.groupby('date').size().reset_index(name='interaction_count')
    
    # Merge with weather data
    daily_weather = merged_df[['date', weather_feature]].drop_duplicates()
    merged_activity_weather = pd.merge(daily_activity, daily_weather, on='date', how='left')
    
    # Drop missing values
    merged_activity_weather.dropna(subset=[weather_feature], inplace=True)
    
    # Pearson Correlation
    pearson_corr, pearson_p = pearsonr(merged_activity_weather['interaction_count'], merged_activity_weather[weather_feature])
    
    # Spearman Correlation
    spearman_corr, spearman_p = spearmanr(merged_activity_weather['interaction_count'], merged_activity_weather[weather_feature])
    
    result = (
        f"Pearson Correlation between interactions and {weather_feature}: {pearson_corr:.4f} (p-value: {pearson_p:.4f})\n"
        f"Spearman Correlation between interactions and {weather_feature}: {spearman_corr:.4f} (p-value: {spearman_p:.4f})\n"
    )
    
    # Save results to file
    with open(f"{REPORTS_DIR}/correlation_{weather_feature}.txt", "w") as file:
        file.write(result)
    
    print(result)

def compare_activity_by_weather_condition(merged_df, condition):
    """
    Perform a t-test to compare interaction frequency between different weather conditions.
    Saves the results to a text file.
    """
    # Group interactions by weather condition
    condition_present = merged_df[merged_df['conditions'].str.contains(condition, case=False, na=False)]
    condition_absent = merged_df[~merged_df['conditions'].str.contains(condition, case=False, na=False)]
    
    # Count daily interactions
    activity_present = condition_present.groupby('date').size()
    activity_absent = condition_absent.groupby('date').size()
    
    # Perform t-test
    t_stat, p_value = ttest_ind(activity_present, activity_absent, equal_var=False)
    
    result = (
        f"T-Test comparing activity on '{condition}' days vs. other days:\n"
        f"T-Statistic: {t_stat:.4f}, P-Value: {p_value:.4f}\n"
    )
    
    # Save results to file
    with open(f"{REPORTS_DIR}/t_test_{condition}.txt", "w") as file:
        file.write(result)
    
    print(result)