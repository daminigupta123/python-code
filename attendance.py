import pandas as pd

# Example DataFrame
df = pd.DataFrame({
    'student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'attendance_percent': [80, 72, 90, 65, 77]
})

# Vectorized eligibility check
df['eligible'] = df['attendance_percent'] >= 75

# Optional: convert True/False to Yes/No
df['eligible'] = df['eligible'].map({True: 'Yes', False: 'No'})