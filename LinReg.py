import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pandas as pd


#save your data in the same folder as the project naming it "data.csv"

#Variables



def main():


    df = pd.read_csv("data.csv", encoding="iso-8859-1")
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
    df = df.dropna(axis=0, how='any', thresh=None, subset=[CL1CAT, CL2CAT],inplace=False)

    print(df)
    # Read CSV Data
    X = df[CL1CAT].values.reshape(-1,1)
    print(X)
    y = df[CL2CAT].values.reshape(-1,1)
    print(y)
    # this put data into dataframe, change labels to column categories. Y is the dependent variable

    reg = LinearRegression()
    reg.fit(X, y)
    predictions = reg.predict(X)
    plt.figure(figsize=(16, 8))
    plt.scatter(
        df[CL1CAT],
        df[CL2CAT],
        c='#d73671'
    )
    plt.plot(
        df[CL1CAT],
        predictions,
        c='#3695d8',
        linewidth=2
    )
    plt.xlabel(CL1CAT)
    plt.ylabel(CL2CAT)
    plt.show()
    #shows grapgh

    X = df[CL1CAT]
    y = df[CL2CAT]
    X2 = sm.add_constant(X)
    est = sm.OLS(y, X2)
    est2 = est.fit()
    print(est2.summary())
    print("The linear model is: Y = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))

if __name__ == "__main__":
    main()