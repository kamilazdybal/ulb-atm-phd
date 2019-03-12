# Load numerical data from .csv file to a (nested) list

from numpy import genfromtxt
my_data = genfromtxt('data.csv', delimiter=',')
my_data = my_data.tolist()
print(type(my_data))
print(my_data)
