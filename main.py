#import all libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

#Load the Data
df = pd.read_csv(r'C:\Users\saiga\OneDrive\Desktop\Army\surveillance_data.csv', parse_dates=['timestamp'])

#Exploring Data
print(df.head())
print(df.describe())

#Visualize Movement Over Time for Each Location
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='timestamp', y='movement_count', hue='location_id')
plt.title('Movement Over Time by Location')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Detect Anomalies (movement > 15 is considered anomalous)
df['anomaly'] = df['movement_count'] > 15
print("Anomalies Detected:")
print(df[df['anomaly']])

#Visualize Total Movement per Location
heatmap_data = df.groupby('location_id')['movement_count'].sum().reset_index()

sns.barplot(data=heatmap_data, x='location_id', y='movement_count')
plt.title('Total Movement by Location')
plt.show()

#Calculate Threat Score (optional)
df['threat_score'] = (
    df['movement_count'] * 0.5 +
    df['noise_level'] * 0.3 +
    df['temperature'] * 0.2
)

#Sort by Threat Score
print("Top Threats:")
print(df.sort_values('threat_score', ascending=False).head(10))
