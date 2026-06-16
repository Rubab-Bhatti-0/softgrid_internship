import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('student_data.csv')

print("Dataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

# Check for nulls
print("\nNull Values:")
print(df.isnull().sum())

# Visualization
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.savefig('correlation_heatmap.png')

plt.figure(figsize=(10, 6))
sns.histplot(df['Final_Performance_Grade'], kde=True)
plt.title('Distribution of Final Grades')
plt.savefig('grade_distribution.png')

print("\nVisualizations saved.")
