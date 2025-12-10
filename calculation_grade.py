# import pandas as pd

# # Example DataFrame
# df = pd.DataFrame({
#     'student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
#     'final_score': [95, 82, 76, 61, 54]
# })

# # Define conditions and corresponding grades
# conditions = [
#     df['final_score'] >= 90,
#     df['final_score'] >= 80,
#     df['final_score'] >= 70,
#     df['final_score'] >= 60,
#     df['final_score'] < 60
# ]

# grades = ['A', 'B', 'C', 'D', 'F']

# # Use np.select for vectorized assignment
# df['grade'] = pd.np.select(conditions, grades)

# print(df)

# df['calculated_grade']=df['final_score'].apply(assignment)
# print("first 5 calculated grades:")
# print(df[['final_score', 'calculated_grade']].head())
import pandas as pd
import numpy as np # Import numpy
df = pd.DataFrame({
    'student': ['mini', 'ram', 'Charlie', 'sohan', 'riya'],
    'final_score': [95, 82, 76, 61, 54]
})

conditions = [
    df['final_score'] >= 90,
    df['final_score'] >= 80,
    df['final_score'] >= 70,
    df['final_score'] >= 60,
    df['final_score'] < 60
]

grades = ['pass', 'pass', 'pass', 'pass', 'Fail']


df['grade'] = np.select(conditions, grades, default='NaN') # Added a string default value

print(df)

# Note: The 'assignment' function is not defined in the provided code, which will lead to another error.
df['calculated_grade']=df['final_score'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D' if x >= 60 else 'F')
print("first 5 calculated grades:")
print(df[['final_score', 'calculated_grade']].head())