import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load clustered data
df = pd.read_csv('results/clustered_customers.csv')

# Boxplot of Age distribution by Cluster
plt.figure(figsize=(8,5))
sns.boxplot(x='Cluster', y='Age', data=df, palette='Set2')
plt.title('Age Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Age')
plt.show()

# Countplot for Gender distribution by Cluster
plt.figure(figsize=(8,5))
sns.countplot(x='Cluster', hue='Gender', data=df, palette='Set1')
plt.title('Gender Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Count')
plt.legend(title='Gender')
plt.show()
