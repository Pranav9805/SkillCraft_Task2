import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nData Summary:")
    print(df.describe())
    return df

if __name__ == "__main__":
    data_path = "data/Mall_Customers.csv"  # Adjust relative path as needed
    df = load_data(data_path)

import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('data/Mall_Customers.csv')  # Update path if needed

# Select relevant features: Annual Income and Spending Score
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# X_scaled is the normalized data ready for clustering
print("Scaled feature example:\n", X_scaled[:5])
