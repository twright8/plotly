import pandas as pd
import plotly.express as px
import numpy as np
from math import ceil, floor
from sklearn.preprocessing import MinMaxScaler

pd.set_option('mode.chained_assignment', None)

df = pd.read_csv("data_wyear.csv", encoding="iso-8859-1")
df['Combined Variable Score'] = ""
col_head = (list(df))
input("Please make sure that you input the right variables, the script will fail if for example you put a number "
      "column (e.g. CPI) into a string based column (e.g Country Names). On some inputs you can type 'None' if you "
      "dont want to add "
      "a variable Press enter to continue: ")

for a, b in enumerate(col_head, 1):
    print('{} {}'.format(a, b))

n = int(input("Enter a number for your independent variable: "))

CL1CAT = col_head[n - 1]
#
for a, b in enumerate(col_head, 1):
    print('{} {}'.format(a, b))

n = int(input("Enter a number for your dependent variable: "))

CL2CAT = col_head[n - 1]
#
for a, b in enumerate(col_head, 1):
    print('{} {}'.format(a, b))
try:
    n = int(input("Enter a number for your size variable (This changes the size of the dots). Can be 'None': "))
    CLsize = col_head[n - 1]
except:
    CLsize = None
    pass

#
for a, b in enumerate(col_head, 1):
    print('{} {}'.format(a, b))
try:
    n = int(input("Enter a number for your animation variable (YOU SHOULD ALMOST ALWAYS USE 'Year'). Can be 'None': "))
    CLanimation_frame = col_head[n - 1]
    for a, b in enumerate(col_head, 1):
        print('{} {}'.format(a, b))

    n = int(input("Enter a number for your animation group (YOU SHOULD ALMOST ALWAYS USE 'Country name'): "))

    CLanimation_group = col_head[n - 1]
except:
    CLanimation_frame = None
    CLanimation_group = None
    pass

#

for a, b in enumerate(col_head, 1):
    print('{} {}'.format(a, b))
try:
    n = int(input("Enter a number for your to define the color of the dots, 'Combined Variable Score' gives you color "
                  "based on location on the chart, 'Country name' means you can disagregate easier by country. Can be "
                  "'None': "))
except:
    CLcolor = None
    pass
CLcolor = col_head[n - 1]
#

for a, b in enumerate(col_head, 1):
    print('{} {}'.format(a, b))

try:
    n = int(input("Enter a number for what divides your graphs,'Continent' divides this into 5 corresponding graphs "
                  "for each. Can be 'None': "))
    CLfacet_col = col_head[n - 1]
except:
    CLfacet_col = None
    pass

#

df = df.dropna(axis=0, how='any', thresh=None, subset=[CL1CAT, CL2CAT, CLsize], inplace=False)
CL_Name = "Country name"
import statsmodels.formula.api as sm

scaler = MinMaxScaler()
df["A"] = ""
df["B"] = ""
df[['A', 'B']] = scaler.fit_transform(df[[CL2CAT, CL1CAT]])
df['Combined Variable Score'] = df['A'] + df['B']
maxValuesObj = df['Combined Variable Score'].max()
minValuesObj = df['Combined Variable Score'].min()

fig = px.scatter(
    data_frame=df,
    x=CL1CAT,
    y=CL2CAT,
    animation_frame=CLanimation_frame,
    animation_group=CLanimation_group,
    size=CLsize,
    color=CLcolor, range_color=[floor(minValuesObj), ceil(maxValuesObj)],
    hover_name=CL_Name,
    facet_col=CLfacet_col,
    size_max=25,
    trendline='ols',
    category_orders={'Year': list(range(2007, 2019))}  # this might need to be reviewed
)
fig.show()
