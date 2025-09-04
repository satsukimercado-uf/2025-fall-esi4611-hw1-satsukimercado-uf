# packages
import pandas as pd
import numpy as np

def main(): 
    arr_in = read_csv()
    arr_out = calc(arr_in)
    df = corr(arr_in)

def read_csv():
    df = pd.read_csv("quartet.csv")
    arr = np.array(df)
    return arr

def calc(arr_in):
    # store output
    n_row = int(1) # 1 row
    n_col = int(arr_in.shape[1]) # 8 columns
    arr_mn = np.empty((n_row, n_col))
    arr_var = np.empty((n_row, n_col))

    # calculate along axis = 0, which are the columns. calculation is done all at once, return array 1x8
    mn = np.mean(arr_in, axis = 0) # 1x8 array
    var = np.var(arr_in, axis = 0) # 1x8 array
    # print(mn, var)

    # reshape arr_mn and arr_var, return array 4x2
    arr_mn = mn.reshape(4,2)
    arr_var = var.reshape(4,2)
    # print(arr_mn, arr_var)

    # split array
    x_mn = arr_mn[:, 0:1]
    y_mn = arr_mn[:, 1:]
    x_var = arr_var[:, 0:1]
    y_var = arr_var[:, 1:]

    # stack array
    arr_out = np.hstack([x_mn, y_mn, x_var, y_var])
    # print(arr_out)
    
def corr(arr_in):
    # output array
    
    # split array
    n_col = arr_in.shape[1]
    for i in range(0, n_col,2): # (start, end, step)
        p = arr_in[:, i:i+2] # one pair
        print(s)


if __name__ == "__main__":
    main()