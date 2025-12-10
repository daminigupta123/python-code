import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'final_score': [95, 82, 76, 61, 54]
})

# Define conditions and corresponding grades
conditions = [
    df['final_score'] >= 90,
    df['final_score'] >= 80,
    df['final_score'] >= 70,
    df['final_score'] >= 60,
    df['final_score'] < 60
]

grades = ['A', 'B', 'C', 'D', 'F']

# Use np.select for vectorized assignment
df['grade'] = pd.np.select(conditions, grades)

print(df)

df['calculated_grade']=df['final_score'].apply(assignment)
print("first 5 calculated grades:")
print(df[['final_score', 'calculated_grade']].head())