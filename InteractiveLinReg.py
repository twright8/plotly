import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
import statsmodels.api as sm

# Save your data in the same folder as the project naming it "data.csv"
# This script gives you an interactive graph with regression lines categorised by the "color" variable; to have one reg line, change to "color = None".
# It then prints statistics of the two main variables CL1CAT and CL2CAT

# Variables - only change these (the bits in the quotation marks



## change the above to change the interactive graph, Use "None" if you do not want to add variables

def main():
    df = pd.read_csv("data.csv", encoding="iso-8859-1")
    df['Combined Variable Score'] = ""
    col_head = (list(df))
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

    n = int(input("Enter a number for your size variable (This changes the size of the dots): "))

    CLsize = col_head[n - 1]
    #
    for a, b in enumerate(col_head, 1):
        print('{} {}'.format(a, b))

    n = int(input("Enter a number for your to define the color of the dots, 'Combined Variable Score' gives you color "
                  "based on location on the chart, 'Country name' means you can disagregate easier by country: "))

    CLcolor = col_head[n - 1]
    #
    df = df.dropna(axis=0, how='any', thresh=None, subset=[CL1CAT, CL2CAT], inplace=False)
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
        size=CLsize,
        trendline='ols',
        color=CLcolor,
        hover_name="Country Name",
        size_max=30,

    )
    trendline = fig.data[1]
    fig.add_trace(trendline)
    fig.show()
    fig = px.scatter(
        data_frame=df,
        x=CL1CAT,
        y=CL2CAT,
    )
    X = df[CL1CAT]
    y = df[CL2CAT]
    X2 = sm.add_constant(X)
    est = sm.OLS(y, X2)
    est2 = est.fit()
    print(est2.summary())

if __name__ == "__main__":
    main()

