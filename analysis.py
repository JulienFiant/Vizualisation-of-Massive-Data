import numpy as np
import pandas as pd
from math import *

def GetData(origin):
    print("Car from {}".format(origin))
    data = pd.read_csv("data.csv",delimiter=";")
    if origin != "Everywhere":
        data = data[data['Origin'].str.contains(origin)]
    print("MPG :\nMean {}\nStandard Deviation {}".format( round(np.mean(data['MPG']),2), round(np.std(data['MPG']),2) ))
    print("Cylinders :\nMean {}\nStandard Deviation {}".format( round(np.mean(data['Cylinders']),2), round(np.std(data['Cylinders']),2) ))
    print("Horsepower :\nMean {}\nStandard Deviation {}".format( round(np.mean(data['Horsepower']),2), round(np.std(data['Horsepower']),2) ))
    print("Weight :\nMean {}\nStandard Deviation {}".format( round(np.mean(data['Weight']),2), round(np.std(data['Weight']),2) ))
    print("Acceleration :\nMean {}\nStandard Deviation {}".format( round(np.mean(data['Acceleration']),2), round(np.std(data['Acceleration']),2) ))
    df = pd.DataFrame({'Cylinders':data['Cylinders'],
                        'Horsepower':data['Horsepower'],
                       'MPG': data['MPG'],
                       'Weigth':data['Weight'],
                       'Acceleration': data['Acceleration']})
    print(df.corr())
    print()

def main():
    GetData('Everywhere')
    GetData('US')
    GetData('Europe')
    GetData('Japan')
    

    return

if __name__ == "__main__":
    main()