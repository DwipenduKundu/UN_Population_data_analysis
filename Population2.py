import csv
import matplotlib.pyplot as plt
from collections import defaultdict


COUNTRY = 'country'
YEAR = 'year'
POPULATION = 'population'


def start2(file_path):
    with open(file_path, mode='r') as contry_file:
        country_data = csv.DictReader(contry_file)
        population = defaultdict(int)

        for row in country_data:
            if row[YEAR] == '2014':
                # taking Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Vietnam countries
                if row[COUNTRY] == 'Brunei Darussalam' or row['country'] == 'Cambodia' or row['country'] == 'Indonesia' or row['country'] == 'Lao PDR' or row['country'] == 'Malaysia' or row['country'] == 'Myanmar' or row['country'] == 'Philippines' or row['country'] == 'Singapore' or row['country'] == 'Thailand' or row['country'] == 'Viet Nam':
                    # now taking the country and populatins of those counties in dictionary
                    population[row[COUNTRY]] += int(row[POPULATION])
                # short

        population = dict(sorted(population.items(), key=lambda x: x[1]))
        return population


def graph2(population_data):
    # taking the countries from the key
    country = population_data.keys()
    # taking tyhe population number from the values
    population_number = population_data.values()
    print(population_data)

    # plotting
    plt.bar(country, population_number)

    # taking tittles and labels names
    plt.title("population of Asean Countries.")
    plt.ylabel("Population")
    plt.xlabel("countries")
    # rotate x-label by 90 deg and set fontsize =6
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def execute2():
    file_path = "/home/dwipendu/Desktop/project3/Data/country_pop.csv"
    population_dict = start2(file_path)
    graph2(population_dict)


if __name__ == "__main__":
    execute2()
