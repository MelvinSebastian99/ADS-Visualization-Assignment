# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:31:23 2023

@author: melvi
"""
"""Importing required python packages"""
import pandas as pd
import matplotlib.pyplot as plt

"""Read the data from the CSV file"""
df1 = pd.read_csv("wages_by_education.csv")
print(df1)

"""Extracting columns for the plot"""
years = df1['year']
men_bachelors_degree = df1['men_bachelors_degree']
men_advanced_degree = df1['men_advanced_degree']
women_bachelors_degree = df1['women_bachelors_degree']
women_advanced_degree = df1['women_advanced_degree']

"""Plotting the data"""
plt.figure(figsize=(10, 6))  # Adjust the figure size if needed

""" function to plot line graph"""
def create_line_plot(men_bachelors_degree,men_advanced_degree,women_bachelors_degree,women_advanced_degree ):
    
    
    
    """Plot lines for men's education levels"""
    plt.plot(years, men_bachelors_degree, label="Men - Bachelor's Degree")
    plt.plot(years, men_advanced_degree, label='Men - Advanced Degree')

    """Plot lines for women's education levels"""
    plt.plot(years, women_bachelors_degree, label="Women - Bachelor's Degree")
    plt.plot(years, women_advanced_degree, label='Women - Advanced Degree')

    plt.title('Wages by educational level in the USA between educated men and women')
    plt.xlabel('Year')
    plt.ylabel('Hourly Wage ($)')
    plt.grid(True)
    plt.legend()
    plt.xticks(years, rotation=90)  # Rotating x-axis labels for better readability

    plt.tight_layout()
    plt.show()
    
""" Calling Function"""
create_line_plot(men_bachelors_degree,men_advanced_degree,women_bachelors_degree,women_advanced_degree) 





                     
                    


