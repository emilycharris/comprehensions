import csv
import statistics
import datetime
from collections import defaultdict

#Remove all vowels from this sentence List Comprehensions are the Greatest!

def remove_vowels(string):

    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''.join([letter for letter in string if letter not in vowels])
    return result
print("Remove Vowels: ", remove_vowels("List Comprehensions are the Greatest!"))


#Create a list of Water Temps for each day from the data set.


def open_file():
    csvfile = open("dataset.txt", 'r')
    data = csv.reader(csvfile, delimiter=',')
    dataset = list(data)
    return dataset


def list_water_temp():

    water_temp = [row[4] for row in open_file()]
    return water_temp
print("Water Temp List: ", list_water_temp())


def list_date():
    date = [row[5] for row in open_file()]
    return date
print("Date List: ", list_date())

#Convert the Water Temps from a string to a float


def float_conversion_func():
    float_conversion = [float(temp) for temp in list_water_temp()[1:]]
    return(float_conversion)
print("Temps as Float: ", float_conversion_func())

#Convert the Water Temps from Celsius to Fahrenheit rounded to an int


def temp_conversion_C_to_F():
    fahrenheit = [int(temp * 1.8 + 32) for temp in float_conversion_func()]
    return fahrenheit
print("Temps Converted C to F: ", temp_conversion_C_to_F())

#Create a dictionary with Date as the key and Wave Height as the value

def wave_height_func():
    wave_height = [row[1] for row in open_file()]
    return wave_height

def wave_height_dictionary():
    dates = list_date()
    wave_height = wave_height_func()
    dictionary = {dates[i]: wave_height[i] for i in range(len(dates))}
    return dictionary
print("Wave Height Dictionary: ", wave_height_dictionary())

#Create a dictionary with the average wave height for each day

def average_wave_height():

    dates = []
    for date in wave_height_dictionary():
        dates.append(date) #==>string to list
    dates.remove("Date")
    return dates
dates = average_wave_height()
print(dates)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_dow(date_string):
    return days[datetime.datetime.strptime(date_string, '%Y-%m-%d').weekday()]

print([get_dow(date) for date in dates])


def homework1_avg():
    grade_dictionary = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                    'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                    'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                    'River': {'Homework 1': 85, 'Homework 2': 91}}
    homework_1 = []
    [homework_1.append(grades["Homework 1"]) for (person, grades) in grade_dictionary.items()]

    return statistics.mean(homework_1)
print("Homework 1 Average: ", homework1_avg())