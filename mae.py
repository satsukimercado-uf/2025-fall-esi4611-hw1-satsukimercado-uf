# packages
import pandas as pd
import numpy as np

# def main
def main(): 
    df = read_csv()
    mean(df)

# def read_csv
def read_csv():
    # store file
    df = pd.read_csv("quartet.csv")
    return df

# def mean
def mean(df):
    # store input
    df_in = df
    # store output
    df_mn = pd.DataFrame () # 1x8 matrix
    df_var = pd.DataFrame() # 1x8 matrix 
    df_out = pd.DataFrame(columns = ['x_mean', 'y_mean', 'x_var', 'y_var', 'corr'])


    # df.shape[0] > row count, m = 0. df.shape[1] > column count, n = 1. 
   
    # find mean and var values
    for i in range(df_in.shape[1]): # for i = 0 to num of columns 
        # mean 
        mn = df_in.column[i].mean()
        # var 
        var = df_in.column[i].var()
        # insert in entry [0,i] in output df
        df_mn.loc[0,i] = mn
        df_var.loc[0,i] = var

    print(df_mn, "\n", df_var)


# start
if __name__ == "__main__":
    main()