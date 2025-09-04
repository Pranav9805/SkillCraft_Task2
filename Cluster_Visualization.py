import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('results/clustered_customers.csv')

plt.figure(figsize=(8,5))
sns.boxplot(x='Cluster', y='Age', data=df, palette='Set2')
plt.title('Age Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Age')
plt.show()
plt.figure(figsize=(8,5))
sns.countplot(x='Cluster', hue='Gender', data=df, palette='Set1')
plt.title('Gender Distribution by Cluster')
plt.xlabel('Cluster')
plt.ylabel('Count')
plt.legend(title='Gender')
plt.show()
