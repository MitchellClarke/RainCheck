from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import csv

iFile = open('Output.csv')
reader = csv.reader(iFile)

temps = [[]]
sales = [[]]
department = []

header = True
#deptNo is the number of the departments we have seen up to this point,
#Note that this is different from deptName as some small departments were
#lost in the data filtering.
deptName = 1
#read in the data
for row in reader:
    if not header:
        while int(row[1]) > len(temps):
            temps.append([])
            sales.append([])
            
        deptName = int(row[1])
        temps[deptName-1].append(float(row[4]))
        sales[deptName-1].append(float(row[3]))
        #department.append(int(row[1]))
    else: header = False
    
    

slopes = np.zeros(len(sales))
intercepts = np.zeros(len(sales))
r_values = np.zeros(len(sales))
p_values = np.zeros(len(sales))
slope_std_errors = np.zeros(len(sales))

print("done reading")
tempsArray = np.array(temps)
salesArray = np.array(sales)

for i in range(len(tempsArray)):
    if(len(salesArray[i]) != 0):
        slopes[i], intercepts[i], r_values[i], p_values[i], slope_std_errors[i] = stats.linregress(tempsArray[i], salesArray[i])

        # Calculate some additional outputs
        predict_y = intercepts[i] + np.multiply(slopes[i], tempsArray[i])
        print(len(tempsArray[i]), len(predict_y))
        pred_error = salesArray[i] - predict_y
        degrees_of_freedom = len(tempsArray[i]) - 2
        residual_std_error = np.sqrt(np.sum(pred_error**2) / degrees_of_freedom)

        # Plotting
        plt.plot(tempsArray[i], salesArray[i], ',')
        plt.text(0, max(salesArray[i]), 'Slope: ' + str(slopes[i]))
        plt.xlabel("Degrees F")
        plt.ylabel("Sales")
        plt.title("Temperature vs Department #" + str(i+1) + " sales")
        plt.plot(tempsArray[i], predict_y)
        plt.savefig("deptNo" +str(i+1))
        plt.show()
