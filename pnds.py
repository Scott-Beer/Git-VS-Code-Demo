import time
import pandas as pd 

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

df["pop>=3M"] = df["population"]>=3000000
df["life<50"] = df["life expectancy"]<50

df2 = df[(df["pop>=3M"] == True) & (df["life<50"] == True)]

print(df2) 