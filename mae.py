# packages
import pandas as pd
import numpy as np

# def main
def main(): 
    df = read_csv()
    df_mn, df_var = calc(df)
    df_out = corr(df_mn, df_var)

# def read_csv
def read_csv():
    # store file
    df = pd.read_csv("quartet.csv")
    # print(df.dtypes)

    # convert values from str to numeric
    # for col in df.columns: # for each column in the dataframe
    #     if df[col].dtype == np.float64:
    #         df[col] = df[col].astype(float)
    return df

# def calc: mean and var
def calc(df):
    df_in = df
    # column names of input = output
    col_names = df_in.columns
    # store output
    df_mn = pd.DataFrame (columns = col_names) # 1x8 matrix, same col name
    df_var = pd.DataFrame(columns = col_names) # 1x8 matrix, same col name

    # iterate over every column 
    for col in df.columns: # for i = 0 to num of columns 
        # mean of the column values
        mn = df_in[col].mean()
        # var of the column values
        var = df_in[col].var()
        # insert in entry [0,col] in output df. col matches the column name
        df_mn.loc[0,col] = mn
        df_var.loc[0,col] = var
    
    # sanity check
    # print(df_mn, "\n", df_var)

    # return 
    return df_mn, df_var

# def corr, one table w correlation calc
def corr(df_mn, df_var):
    # column names of input = output
    col_names = df_mn.columns   
    df_out = pd.DataFrame(columns = col_names)

    # df to arrays
    arr_mn = df_mn.values
    arr_var = df_var.values

    # reshape arrays
    arr_mn = arr_mn.reshape(4,2)
    arr_var = arr_var.reshape(4,2)

    # arr to df
    arr_out = 


    print(arr_mn, "\n", arr_var)

# start
if __name__ == "__main__":
    main()