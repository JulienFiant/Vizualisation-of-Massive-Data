import numpy as np
from math import *

def main():
    nb_bebete = 300


    datataille = np.random.uniform(3, 50, nb_bebete)
    datayeux = np.random.uniform(1, 5, nb_bebete).astype(int)
    datapapates = datataille*2 + np.random.uniform(2, 10, nb_bebete).astype(int)
    dataailes = - datapapates/2 + np.random.uniform(55, 74, nb_bebete).astype(int)
    dataaltitude = np.random.uniform(-8000, 6739, nb_bebete)#https://www.peuple-animal.com/article,lecture,2353_decouverte-du-mammifere-vivant-a-la-plus-haute-altitude-au-monde.html#:~:text=Jusqu'o%C3%B9%20y%20a%2Dt,d'altitude%20%3A%20un%20record%20!
    datatrouvé = dataaltitude/3 + np.random.uniform(5000, 10000, nb_bebete).astype(int)
    datalong = np.random.uniform(-180, 120, nb_bebete)
    datalat = np.random.uniform(-90, 90, nb_bebete)

    tmp = [datataille,datayeux, datapapates,dataailes,dataaltitude,datatrouvé,datalong,datalat]
    data = np.transpose(tmp)

    print("Means :")
    print("Size in cm,Number of Eyes,Number of Body Members,Number of Wings, Sea level,Population, Longitude,Latitude")
    print(round(np.mean(datataille),2), round(np.mean(datayeux),2),round(np.mean(datapapates),2),round(np.mean(dataailes),2),round(np.mean(dataaltitude),2), round(np.mean(datatrouvé),2),round(np.mean(datalong),2),round(np.mean(datalat),2), end='\n\n', sep=' ,')
    print("Standard Deviation :")
    print("Size in cm,Number of Eyes,Number of Body Members,Number of Wings, Sea level,Population, Longitude,Latitude")
    print(round(np.std(datataille),3), round(np.std(datayeux),3),round(np.std(datapapates),3),round(np.mean(dataailes),2),round(np.std(dataaltitude),3), round(np.mean(datatrouvé),2),round(np.std(datalong),3),round(np.std(datalat),3), end='\n\n',sep=' ,')

    print("Positive : Number of Body Members and Size in cm")
    print(np.corrcoef(datapapates, datataille))
    print("Positive :  Sea level and Population")
    print(np.corrcoef(dataaltitude, datatrouvé),end='\n\n')

    print("Negative : Number of Body members and Number of Wings")
    print(np.corrcoef(datapapates, dataailes))
    print("Negative : Size and Number of wings")
    print(np.corrcoef(datataille, dataailes),end='\n\n')

    print("No correlation : Size and Sea Level")
    print(np.corrcoef(datataille, dataaltitude))
    print("No correlation : Longitude and Latitude")
    print(np.corrcoef(datalat, datalong))

    np.savetxt("bebetes.csv", data,fmt="%.2f,%i,%i,%i,%.2f,%i,%.2f,%.2f", header='Size in cm,Number of Eyes,Number of Body Members,Number of Wings, Sea level,Population, Longitude,Latitude')#

if __name__ == "__main__":
    main()