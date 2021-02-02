import pandas as pd
import numpy as np

df = pd.read_excel('Absenteeism_at_work.xls')
myList = df['Body mass index'].tolist()


def calc_outliers(dataframe):
    outliers = []
    q1, q3 = np.percentile(dataframe, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    print(lower_bound)
    print(upper_bound)
    for i in dataframe:
        print(i)
        if i < lower_bound or i > upper_bound:
            outliers.append(i)

    return outliers


print(calc_outliers(myList))


