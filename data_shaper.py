import pandas as pd


def fix_df_header(df):
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    return df


def does_df_contain_column(df, columns):
    for column in columns:
        if column not in df.columns:
            return False
    return True


def columns_to_lower(dataframe, columns):
    df = dataframe[[*columns]]
    for i in range(len(columns)):
        df = df.rename(columns={columns[i]: columns[i].lower()})
    return df


def convert_column_to_numeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df


def convert_column_to_datetime(df, column):
    df[column] = pd.to_datetime(df[column])
    return df


def merge_df(df1, df2, join_column):
    df1 = df1.sort_values(join_column)
    df2 = df2.sort_values(join_column)
    merged_df = pd.merge(df1, df2, left_on=join_column, right_on=join_column, how='left')
    merged_df = merged_df.sort_values(join_column)
    return merged_df
