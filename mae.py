# packages
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression 

def main(): 
    # prep data
    arr_in = read_csv()
    corr_out = corr(arr_in)
    # part a 
    df_out = calc(arr_in, corr_out)
    print("part a: \n", df_out, "\n")
    # part b 
    least_rmse, set_num = lin_reg(arr_in)
    # part c
    lin_reg_perf(least_rmse, set_num)

def read_csv():
    df = pd.read_csv("quartet.csv")
    arr = np.array(df)
    return arr

def calc(arr_in, corr_out):
    xy_corr = corr_out
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
    arr_out = np.hstack([x_mn, y_mn, x_var, y_var, xy_corr])
    # print(arr_out)

    # array to df
    col_names = ('x_mean', 'y_mean', 'x_var', 'y_var', 'xy_correlation')
    df_out = pd.DataFrame(arr_out, columns = col_names)    
    # print(df_out)
    return df_out

def corr(arr_in):
    # output array
    n_row = int(arr_in.shape[1]/2) # columns = num of pairs
    n_col = 1 # 1 column 
    corr_out = np.empty((n_row, n_col))

    # split array
    n_col = arr_in.shape[1]
    for i in range(0, n_col,2): # (start, end, step)
        # x and y in the same pair
        j = int(i/2)       
        x = arr_in[:, i:i+1] 
        y = arr_in[:, i+1: i+2] 
        corr_mtx= np.corrcoef(x,y, rowvar = False) # matrix, rowvar = False transposes x and y 
        corr_r = corr_mtx[0,1] # [0,1] and [1,0] contain the same value, do this to return a single r value
        corr_out[j,0] = corr_r
    return corr_out

def lin_reg(arr_in):
    n = arr_in.shape[1] # returns number of columns, step = 2 for pairs 
    s = 1
    rmse_list = []
    least_rmse = 0 
    print("part b:\n")

    
    for i in range(0,n,2):
        x_train = arr_in[:, i].reshape(-1,1) # set i, x values 
        y_train = arr_in[:, i+1].reshape(-1,1) # set i, y values 
        # print(x_train, "\n", y_train)

        # linear regression 
        model = LinearRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_train)
        # print("set ", i, "\n", y_pred, "\n")

        # line of best fit 
        m = model.coef_[0,0] # [0,0] to return the value, not the entire array
        b = model.intercept_[0] # [0] to return the value, not the entire row
        # mse
        mse = mean_squared_error(y_pred, y_train)
        rmse = np.sqrt(mse)
        rmse_list.append(rmse)

        # output 
        print("set ", s, ": y =", round(m,2), "x + ", round(b,2), "\nrmse =", round(rmse,4), "\n")
        
        # increment set
        s = s + 1
    
    # find the set with the smallest valued rmse:
    for j in range(1,len(rmse_list)):
        if rmse_list[j] <= rmse_list[j-1]:
            least_rmse = rmse_list[j]
    # print(least_rmse, j+1)

    # return smallest valued rmse & set 
    return least_rmse, j+1

def lin_reg_perf(least_rmse, set_num):
    print("part c: \nThe set for which the linear regression performs the best is set", set_num, " with a RMSE of", round(least_rmse,4), ".")


if __name__ == "__main__":
    main()