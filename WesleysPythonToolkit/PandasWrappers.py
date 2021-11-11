import pandas as pd

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