import pandas as pd
import numpy as np
scores = [78, 65, 90, 45, 55, 88, 92, 40, 72, 66]
df = pd.DataFrame({"Math_Score": scores})
mean_score = df["Math_Score"].mean()
median_score = df["Math_Score"].median()
mode_score = df["Math_Score"].mode()[0]
min_score = df["Math_Score"].min()
max_score = df["Math_Score"].max()
score_range = max_score - min_score
std_dev = df["Math_Score"].std()
variance = df["Math_Score"].var()
pass_mark = 40
pass_percentage = (df["Math_Score"] >= pass_mark).mean() * 100
high_achievers = (df["Math_Score"] >= 75).mean() * 100

