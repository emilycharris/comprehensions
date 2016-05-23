import csv

#Remove all vowels from this sentence List Comprehensions are the Greatest!

def remove_vowels(string):

    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''.join([letter for letter in string if letter not in vowels])
    print(result)

remove_vowels("List Comprehensions are the Greatest!")

#Create a list of Water Temps for each day from the data set.


def open_file():
    csvfile = open("dataset.txt", 'r')
    data = csv.reader(csvfile, delimiter=',')
    dataset = list(data)
    return dataset


def list_water_temp():

    water_temp = [row[4] for row in open_file()]
    print(water_temp)
    return water_temp

list_water_temp()


def list_date():
    date = [row[5] for row in open_file()]
    return date

list_date()


#Convert the Water Temps from a string to a float

float_conversion = [float(temp) for temp in list_water_temp()[1:]]
print(float_conversion)

#Convert the Water Temps from Celsius to Fahrenheit rounded to an int

fahrenheit = [int(temp * 1.8 + 32) for temp in float_conversion]
print(fahrenheit)

#Create a dictionary with Date as the key and Wave Height as the value



#Create a dictionary with the average wave height for each day