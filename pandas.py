import pandas as pd
import numpy as np 
df=pd.read_csv('nyc_weather.csv')
print(df)

min_science = df['science_original'].min()
max_science = df['science_original'].max()
grade_boundries=np.linspace(min_science, max_science, 6)
print(grade_boundries)
