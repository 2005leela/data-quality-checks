
import pandas as pd

# Load the dataset
df = pd.read_csv("dirty_data.csv")

print("📊 Original Data:")
print(df)

# Drop duplicates
df = df.drop_duplicates()

# Fill missing values
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Email'] = df['Email'].fillna('noemail@example.com')
df['Score'] = df['Score'].fillna(df['Score'].mean())

print("\n✅ Cleaned Data:")
print(df)

# Save cleaned file
df.to_csv("cleaned_data.csv", index=False)
