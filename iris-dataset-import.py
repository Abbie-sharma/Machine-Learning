import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#loading dataset
df = pd.read_csv(url, names=['sepal length','sepal width','petal length', 'petal width','target'])
df

label = df['target']
label
del df['target']
df
