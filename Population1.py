import csv
import matplotlib.pyplot as plt
from collections import defaultdict


COUNTRY = 'country'
YEAR = 'year'
POPULATION = 'population'


def start1(file_path):
    with open(file_path, mode='r') as contry_file:
        country_data = csv.DictReader(contry_file)
        population = defaultdict(int)

        for row in country_data:
            # taking inda country
            if row[COUNTRY] == 'India':
                # now taking the years and populatins of india in dictionary
                population[row[YEAR]] += int(row[POPULATION])
        return population


def graph1(population_data):
    # taking tyhe years from the key
    year = population_data.keys()
    # taking tyhe population number from the values
    population_number = population_data.values()

    # plotting
    plt.bar(year, population_number)

    # taking tittles and labels names
    plt.title("population of India vs. years.")
    plt.ylabel("Population")
    plt.xlabel("years")
    # rotate x-label by 90 deg and set fontsize =6
    plt.xticks(rotation=90, fontsize=6)
    plt.tight_layout()
    plt.show()


def execute1():
    file_path = "/home/dwipendu/Desktop/project3/Data/country_pop.csv"
    population_dict = start1(file_path)
    graph1(population_dict)


if __name__ == "__main__":
    execute1()
