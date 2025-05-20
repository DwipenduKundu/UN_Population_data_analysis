import csv
import matplotlib.pyplot as plt
from collections import defaultdict


COUNTRY = 'country'
YEAR = 'year'
POPULATION = 'population'
asean_countries = ["Brunei Darussalam", "Cambodia", "Indonesia",
                   "Lao PDR", "Malaysia", "Myanmar", "Philippines",
                   "Singapore", "Thailand", "Viet Nam"]


def start4(file_path):
    asean_popul = {}

    with open(file_path, mode="r") as file:
        data = csv.DictReader(file)
        for row in data:
            year = int(row[YEAR])
            country = row[COUNTRY]
            if 2004 <= year <= 2014 and country in asean_countries:
                if year not in asean_popul:
                    asean_popul[year] = defaultdict(int)
                asean_popul[year][country] = row[POPULATION]
    return asean_popul


def graph4(dict_data):
    years = dict_data.keys()

    countries = asean_countries

    bar_width = 0.08
    gap_between_groups = 0.3

    group_count = len(years)
    country_count = len(countries)

    group_width = bar_width * country_count + gap_between_groups

    x_start = [i * group_width for i in range(group_count)]

    plt.figure(figsize=(16, 8))

    for i, country in enumerate(countries):
        x_positions = [x + i * bar_width for x in x_start]
        populations = [dict_data[year].get(country, 0) for year in years]
        plt.bar(x_positions, populations, width=bar_width, label=country)

    middle_positions = [x + (bar_width * country_count) / 2 for x in x_start]
    plt.xticks(middle_positions, years, rotation=45)
    plt.yticks(fontsize=6)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("ASEAN Population (2004–2014)")
    plt.legend(title="Country", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.tight_layout()
    plt.show()


def execute4():
    file_path = "/home/dwipendu/Desktop/project3/Data/country_pop.csv"
    asean_population = start4(file_path)
    graph4(asean_population)


if __name__ == "__main__":
    execute4()
