# packages
import pandas as pd
import numpy as np

# def main
def main(): 
    read_csv()

# def read_csv
def read_csv():
    df = pd.read_csv("quartet.csv")
    print(df)


# start
if __name__ == "__main__":
    main()