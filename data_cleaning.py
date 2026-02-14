import pandas as pd

# Load dataset
df = pd.read_csv("Data/bank-additional-full.csv", sep=';')

# Basic info
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Convert target variable to binary
df['subscribed'] = df['y'].apply(lambda x: 1 if x == 'yes' else 0)

# Create age group column
bins = [17, 25, 35, 45, 55, 65, 100]
labels = ['18-25','26-35','36-45','46-55','56-65','65+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels)

# Save cleaned file
df.to_csv("Data/bank_cleaned.csv", index=False)

print("\nCleaned file saved successfully!")