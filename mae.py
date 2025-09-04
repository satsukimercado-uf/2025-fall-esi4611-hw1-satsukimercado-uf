# packages
import pandas as pd
import numpy as np

# def main
def main(): 
    df = read_csv()
    mean()

# def read_csv
def function read_csv():
    df = pd.read_csv("quartet.csv")
    return df

# start
if __name__ == "__main__":
    main()