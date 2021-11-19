import pandas as pd
import numpy as np

def df_stringsplit_DEPRECATED(df: pd.DataFrame, colname: str, splitchar: str) -> pd.DataFrame:
    """Performs stringsplit on a dataframe column and automatically adds new columns to the dataframe containing the splits"""

    # Split on character and rename resulting dataframe columns
    col = df[colname].str.split(pat=splitchar, expand=True)

    for i in range(0, len(col.columns)):
        col[col.columns[i]] = col[col.columns[i]].str.strip()
        col = col.rename(columns={i : colname + str(i)})
    # Join new dataframe back to original
    df = df.join(col, how='left')

    return df


def df_stringsplit(df: pd.DataFrame, colname: str, splitchar: list) -> pd.DataFrame:
    """Performs stringsplit on a dataframe column and automatically adds new columns to the dataframe containing the splits"""

    # Create destructable df using column
    coldf = df[[colname]]

    # Initialize the column checklist
    columns_to_check = coldf.columns

    # Iterate over splitting characters
    for splitter in splitchar:
        # Iterate over each column in checklist, relevant for multiple splits
        for column in columns_to_check:
            # Split the current column
            iterdf = coldf[column].str.split(pat=splitter, expand=True)
            # Rename the values in the split column
            for i in range(0, len(iterdf.columns)):
                iterdf = iterdf.rename(columns={i: column + str(i)})
            # Join the new columns back to the worker df
            coldf = coldf.join(iterdf, how='left')

        # Drop the already used column
        coldf = coldf.drop(columns_to_check, axis=1)
        # Update the list of columns to check
        columns_to_check = coldf[list(set(coldf.columns.to_numpy()).difference(set(columns_to_check.to_numpy())))].columns.sort_values().astype('object')

    # Final rename
    for i in range(0, len(coldf.columns)):
        coldf[coldf.columns[i]] = coldf[coldf.columns[i]].str.strip()
        coldf = coldf.rename(columns={coldf.columns[i] : colname + str(i)})

    # Join new dataframe back to original
    df = df.join(coldf, how='left')

    # Clean up the columns before returning
    columns_to_consider = len(columns_to_check)
    total_columns = len(df.columns)
    missings = df.isna().sum()
    condition = False
    # Check if any columns to the right of each split column have fewer missing values. If so, then cleaning is not done
    for i in range(len(missings)-2, 0, -1):
        for j in range(i, 0, -1):
            if missings[j] > missings[i+1]:
                condition = True
                break

    # Each iteration, check if a split column has a missing value. If so, swap its value with the column on the right. Uses same above check logic to exit loop
    counter = 0
    while condition & (counter < 1000):
        counter = counter+1
        for i in range(total_columns-1, (total_columns - columns_to_consider), -1):
            bool_series = df[df.columns[i-1]].isna()
            df.loc[bool_series, [df.columns[i-1], df.columns[i]]] = df.loc[bool_series, [df.columns[i], df.columns[i-1]]].values
        missings = df.isna().sum()
        condition = False
        for i in range(len(missings) - 2, 0, -1):
            for j in range(i, 0, -1):
                if missings[j] > missings[i + 1]:
                    condition = True
                    break

    # Remove any split columns that are completely missing
    for i in range(len(missings)-1, len(missings)-1-columns_to_consider, -1):
        if missings[i] == len(df.index):
            df = df.drop(columns=[df.columns[i]])

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
            print("Number of unique {0} values: {1}".format(col, df[col].nunique()))
        print()