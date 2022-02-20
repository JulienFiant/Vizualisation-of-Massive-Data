import numpy as np
import pandas as pd
from math import *
import argparse

def isColumnExist(nameColumn, dataHeader):
    return (nameColumn in dataHeader)

def main():
    parser = argparse.ArgumentParser(description='Visualization 1')
    parser.add_argument('--range', '-r', type=int, help='range of points', required=False, default=50)
    parser.add_argument('--column1', '-c1', type=str, help='Name of the first column to visualize', required=False, default="Car")
    parser.add_argument('--column2', '-c2', type=str, help='Name of the second column to visualize', required=False, default="Origin")
    args = parser.parse_args()
    print("args.range=%s" % args.range)
    print("args.column1=%s" % args.column1)
    print("args.column2=%s" % args.column2)

    data = pd.read_csv("data.csv",delimiter=";")
    if (isColumnExist(args.column1, data.columns) == False):
        print("Error column : " + args.column1 + " doesn't exist in the dataset")
        return (1)
    if (isColumnExist(args.column2, data.columns) == False):
        print("Error column : " + args.column2 + " doesn't exist in the dataset")
        return (1)
    if (args.range > len(data.index) or args.range < 1):
        print ("Error in the argument range, change the value")
        return (1)

    return

if __name__ == "__main__":
    main()