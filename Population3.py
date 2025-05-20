import csv
from collections import defaultdict
import matplotlib.pyplot as plt
def start1():
    with open("/home/dwipendu/Desktop/project3/Data/country_pop.csv",mode='r') as contry_file:
        country_data=csv.DictReader(contry_file)
        population=defaultdict(int)
        
        for row in country_data:
            #taking Afghanistan, Bangladesh, Bhutan, India, Maldives, Nepal, Pakistan, and Sri Lanka countries
            if row['country']=='Afghanistan' or row['country']=='Bangladesh' or row['country']=='Bhutan' or row['country']=='India' or row['country']=='Maldives' or row['country']=='Nepal' or row['country']=='Pakistan' or row['country']=='Sri Lanka':
                #now taking the years and populatins of those counties in dictionary
                population[row['year']]+=int(row['population'])
        graph1(population)
def graph1(population_data):
    #taking tyhe years from the key 
    year=population_data.keys()
    #taking tyhe population number from the values 
    population_number=population_data.values()
    print(population_data)

    #plotting
    plt.bar(year,population_number)

    #taking tittles and labels names
    plt.title("population of Total SAARC population vs. year.")
    plt.ylabel("Population")
    plt.xlabel("years")
    #rotate x-label by 90 deg and set fontsize =6
    plt.xticks(rotation=90,fontsize=6)
    plt.tight_layout()
    plt.show()
start1()