import csv
from collections import defaultdict
import matplotlib.pyplot as plt
def start1():
    with open("/home/dwipendu/Desktop/project3/Data/country_pop.csv",mode='r') as contry_file:
        country_data=csv.DictReader(contry_file)
        population=defaultdict(int)
        
        for row in country_data:
            if row['year']=='2014':
                #taking Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, Vietnam countries
                if row['country']=='Brunei Darussalam' or row['country']=='Cambodia' or row['country']=='Indonesia' or row['country']=='Lao PDR' or row['country']=='Malaysia' or row['country']=='Myanmar' or row['country']=='Philippines' or row['country']=='Singapore' or row['country']=='Thailand' or row['country']=='Viet Nam':
                    #now taking the country and populatins of those counties in dictionary
                    population[row['country']]+=int(row['population'])
                #short

        population=dict(sorted(population.items(), key=lambda x:x[1]))
        graph1(population)
def graph1(population_data):
    #taking the countries from the key 
    country=population_data.keys()
    #taking tyhe population number from the values 
    population_number=population_data.values()
    print(population_data)
    
    #plotting
    plt.bar(country,population_number)

    #taking tittles and labels names
    plt.title("population of Asean Countries.")
    plt.ylabel("Population")
    plt.xlabel("countries")
    #rotate x-label by 90 deg and set fontsize =6
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
start1()