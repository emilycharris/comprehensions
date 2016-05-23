#Remove all vowels from this sentence List Comprehensions are the Greatest!

vowels = ('a', 'e', 'i', 'o', 'u')
sentence = "List Comprehensions are the Greatest!"

result = ''.join([letter for letter in sentence if letter not in vowels])
print(result)

#============================================
#Create a list of Water Temps for each day from the data set.

import csv

csvfile = open("dataset.txt", 'r')
data = csv.reader(csvfile, delimiter=',')
dataset = list(data)
#print(dataset)

water_temp = [row[4] for row in dataset]

print(water_temp)


#Convert the Water Temps from a string to a float

float_conversion = [float(temp) for temp in water_temp[1:]]
print(float_conversion)

#Convert the Water Temps from Celsius to Fahrenheit rounded to an int

fahrenheit = [int(temp * 1.8 + 32) for temp in float_conversion]
print(fahrenheit)

#Create a dictionary with Date as the key and Wave Height as the value



#Create a dictionary with the average wave height for each day