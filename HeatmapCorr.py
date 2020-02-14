import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
CSVNAME = "data.csv"
#input corect filename

df = pd.read_csv(f"{CSVNAME}", encoding="iso-8859-1")
corr = df.iloc[:, :-1].corr()
sns.heatmap(corr,
            xticklabels=corr.columns,
            yticklabels=corr.columns)
plt.show()