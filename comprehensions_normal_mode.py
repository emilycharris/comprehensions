import csv
import statistics
import datetime
from collections import defaultdict

#Remove all vowels from this sentence List Comprehensions are the Greatest!

def remove_vowels(string):

    vowels = ('a', 'e', 'i', 'o', 'u')
    result = ''.join([letter for letter in string if letter not in vowels])
    return result
result = remove_vowels("List Comprehensions are the Greatest!")
print("Remove Vowels: ", result)


#Create a list of Water Temps for each day from the data set.


def open_file():
    csvfile = open("dataset.txt", 'r')
    data = csv.reader(csvfile, delimiter=',')
    next(data)
    dataset = list(data)
    return dataset
dataset = open_file()

def list_water_temp():

    water_temp = [row[4] for row in dataset]
    return water_temp
water_temp = list_water_temp()
print("Water Temp List: ", water_temp)


def list_date():
    date = [row[5] for row in dataset]
    return date
date_list = list_date()
print("Date List: ", date_list)

#Convert the Water Temps from a string to a float


def float_conversion_func():
    float_conversion = [float(temp) for temp in water_temp[1:]]
    return(float_conversion)
float_conversion = float_conversion_func()
print("Temps as Float: ", float_conversion)

#Convert the Water Temps from Celsius to Fahrenheit rounded to an int


def temp_conversion_C_to_F():
    fahrenheit = [int(temp * 1.8 + 32) for temp in float_conversion]
    return fahrenheit
fahrenheit = temp_conversion_C_to_F()
print("Temps Converted C to F: ", fahrenheit)

#Create a dictionary with Date as the key and Wave Height as the value

def wave_height_func():
    wave_height = [row[1] for row in dataset]
    return wave_height
wave_height = wave_height_func()

def wave_height_dictionary():
    dates = date_list
    dictionary = {dates[i]: wave_height[i] for i in range(len(dates))}
    return dictionary
dictionary = wave_height_dictionary()
print("Wave Height Dictionary: ", dictionary)

#Create a dictionary with the average wave height for each day

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def get_dow(date_string):
    return days[datetime.datetime.strptime(date_string, '%Y-%m-%d').weekday()]

def wave_by_dow():
    wave_by_dow_dict = defaultdict(list)
    [wave_by_dow_dict[get_dow(date)].append(float(height)) for date, height in dictionary.items()]
    return wave_by_dow_dict
wave_by_dow_dict = wave_by_dow()

def avg_wave_by_dow():
    avg_height_dict = {}
    for day, height in wave_by_dow_dict.items():
        avg_height_dict[day] = (statistics.mean(height))
    print("Average Wave Height Dictionary: ", avg_height_dict)
avg_wave_by_dow()

def homework1_avg():
    grade_dictionary = {'Gale': {'Homework 1': 88, 'Homework 2': 76},
                    'Jordan': {'Homework 1': 92, 'Homework 2': 87},
                    'Peyton': {'Homework 1': 84, 'Homework 2': 77},
                    'River': {'Homework 1': 85, 'Homework 2': 91}}
    homework_1 = []
    [homework_1.append(grades["Homework 1"]) for (person, grades) in grade_dictionary.items()]

    return statistics.mean(homework_1)
homework_average = homework1_avg()
print("Homework 1 Average: ", homework_average)