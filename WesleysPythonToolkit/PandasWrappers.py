import pandas as pd
import numpy as np

def df_stringsplit(df: pd.DataFrame, colname: str, splitchar: str) -> pd.DataFrame:
    """Performs stringsplit on a dataframe column and automatically adds new columns to the dataframe containing the splits"""

    # Split on character and rename resulting dataframe columns
    col = df[colname].str.split(pat=splitchar, expand=True)
    for i in range(0, len(col.columns)):
        col[col.columns[i]] = col[col.columns[i]].str.strip()
        col = col.rename(columns={i : colname + str(i)})
    # Join new dataframe back to original
    df = df.join(col, how='left')

    return df


def df_initialoverview(df: pd.DataFrame, columnlist=[]) -> None:
    """Checks missing counts for all variables, number of unique values for strings, and summary statistics for numbers"""

    if columnlist == []:
        columnlist = df.columns.to_numpy()

    for col in columnlist:
        print("Number of {0} missing: {1}".format(col, df[col].isnull().sum()))
        if (df[col].dtype == np.int64) | (df[col].dtype == np.float64):
            print(df[col].describe())
        else:
            print("Number of unique {0} values: {1}".format(col, df[col].unique()))
        print()