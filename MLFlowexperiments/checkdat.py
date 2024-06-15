import pandas as pd
url = 'winequality-red.csv'
df = pd.read_csv(url)
df = pd.DataFrame(df)
print(df.columns)
print(df.shape)
print(df)