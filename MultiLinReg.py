import statsmodels.formula.api as sm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# need to check this
#input you variables here
CL1CAT = "CPI2017"
CL2CAT = "SDG32017" # dependent variable
CL3CAT = "GDP2017"
CL4CAT = "HDI2017"
CL5CAT = "COCWB2017"
CL6CAT = None
CL7CAT = None
CL8CAT = None


df = pd.read_csv("data.csv", encoding="iso-8859-1")
fields = []
fields.extend(value for name, value in locals().items() if name.startswith('CL') and value is not None)
df = df.dropna(axis=0, how='any', thresh=None, subset=fields, inplace=False)
fields.remove(CL2CAT)
in_var = '+'.join(fields)
result = sm.ols(formula=f"{CL2CAT} ~ {in_var}", data=df).fit()
print(result.params)
print(result.summary())
corr = df.iloc[:, :-1].corr()
sns.heatmap(corr,
            xticklabels=corr.columns,
            yticklabels=corr.columns)
plt.show()