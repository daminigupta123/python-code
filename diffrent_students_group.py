import pandas as pd
import numpy as np

# Sample attendance dataset
data = {
    "Student": ["A1","A2","A3","B1","B2","B3","C1","C2","C3"],
    "Group":   ["A","A","A","B","B","B","C","C","C"],
    "Total_Classes": [40, 40, 40, 40, 40, 40, 40, 40, 40],
    "Attended":      [36, 38, 35, 25, 29, 30, 32, 31, 33]
}

df = pd.DataFrame(data)

# Calculate attendance percentage for each student
df["Attendance %"] = np.round((df["Attended"] / df["Total_Classes"]) * 100, 2)

# Group-wise comparison
group_summary = df.groupby("Group").agg(
    Total_Students=("Student", "count"),
    Avg_Attendance_Percentage=("Attendance %", "mean"),
    Min_Attendance=("Attendance %", "min"),
    Max_Attendance=("Attendance %", "max")
).reset_index()

print("Student-wise Attendance:")
print(df)

print("\nGroup-wise Attendance Comparison:")
print(group_summary)
