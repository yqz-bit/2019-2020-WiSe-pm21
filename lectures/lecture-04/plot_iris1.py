import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fname = 'iris.csv'
df = pd.read_csv(fname)
sns.stripplot(x="species", y="sepal_width", data=df);
plt.savefig('sepal_width.png')
