# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:21:34 2023

@author: melvi
"""
"""Importing required python packages"""
import pandas as pd
import matplotlib.pyplot as plt

"""Read the data from the CSV file"""
df=pd.read_csv("ElectricCarData_Clean.csv")
print(df)
df1=df.head(12)
print(df1)

"""Function to plot Bar Chart"""
def barplot():
    f=plt.figure()
    f.set_figwidth(9)
    f.set_figheight(4)
    f=plt.bar(df1.Brand,df1.TopSpeed_KmH)
    plt.xlabel('Brand names')
    plt.ylabel('km/hr')
    plt.show()
    
"""calling the function"""
barplot() 



"""Function to create a histogram for the number of brands"""
def create_brands_histogram():
    brand_counts = df['Brand'].value_counts()  # Counting the number of occurrences for each brand

    plt.figure(figsize=(10, 6))
    plt.hist(df.Brand, bins=len(brand_counts), edgecolor='black')
    plt.xlabel('Brand names')
    plt.ylabel('Numbers')
    plt.title('Number of Models of electric cars')
    plt.xticks(df.Brand,rotation=90)
    plt.tight_layout()
    plt.show()

# Call the function to create the histogram
create_brands_histogram()





















