from os import listdir
from os.path import isfile, join
from FunctionV3 import plotThings, placeToSave
import sys

# Plot the data from a given fileName
# If no filename given, take last fileName
# could be called directly from interface with ./plot
def plotFromFile(fileName=""):
    # Get the latest file name
    try:
        if fileName == "": fileName = [f for f in listdir(placeToSave) if isfile(join(placeToSave, f))][0]
    except:
        print("ERROR : There is no data yet, first run the calculator")
        return

    theta, p_theta = [], []

    # Read the data from the file
    try:
        with open(placeToSave + fileName, "r") as f:
            data = f.readlines()
    except:
        print("ERROR : There is no file named '" + fileName + "', please make sure you have the correct filename")
        return

    # Create theta and p_theta
    for line in data[2:]:
        theta.append(float(line.split(" ")[0]))
        p_theta.append(float(line.split(" ")[1]))

    # Plot the data
    plotThings(theta, p_theta, data[0])

if __name__ == "__main__":
    if len(sys.argv) > 1: plotFromFile(sys.argv[1])
    else: plotFromFile()