# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:14:53 2023

@author: saisindhu
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def lineplot(Crime) :
    plt.plot(Crime.index, Crime['Vehicle_Theft'], label='Vehicle Theft')
    plt.plot(Crime.index, Crime['Burglary'], label='Burglary')
    plt.plot(Crime.index, Crime['Robbery'], label='Robbery')
    plt.xlabel('Year')
    plt.ylabel('Crimes Occurred in millions')
    plt.legend()
    plt.title('Year VS Various crimes')
    plt.savefig('line_plot.png')
    plt.show()
    
def piechart(Crime) :
    crime_1960 = Crime.loc[1960].sort_values()
    crime_1960_series = crime_1960.iloc[2:-4]
    print(crime_1960_series)

    plt.figure(figsize=(15,20))
    plt.subplot(1, 2, 1)
    plt.pie(crime_1960_series, labels=crime_1960_series.index, autopct='%1.1f%%')
    plt.legend(fontsize=7)
    plt.title('Crimes Distribution in 1960 as %',)
    

    crime_2014 = Crime.loc[2014].sort_values()
    crime_2014_series = crime_2014.iloc[2:-4]
    print(crime_2014_series)
    
    plt.subplot(1, 2, 2)
    plt.pie(crime_2014_series, labels=crime_2014_series.index, autopct='%1.1f%%')
    plt.title('Crimes Distribution in 2014 as %')
    plt.legend(fontsize=7, loc=3)
    plt.savefig('crime_dist_pie.png')
    plt.show()
    
def scatterplot(scores) :
    coeffs = np.polyfit(scores['Hours'], scores['Scores'], 1)
    poly = np.poly1d(coeffs)
    print('\nScore in terms of hours of study :', poly)
    scores_est = poly(scores['Hours'])
    plt.scatter(scores['Hours'], scores['Scores'], alpha=0.7)
    plt.plot(scores['Hours'], scores_est, label='Poly-fitted Line')
    plt.legend()
    plt.xlabel('Hours of study')
    plt.ylabel('Scores(0-100)')
    plt.title('Relation between Hours of study and Score ')
    plt.savefig('scatter_plot.png')
    plt.show()

Crime = pd.read_csv('US_Crime_Rates.csv', index_col='Year')
print(Crime)
lineplot(Crime)
piechart(Crime)

scores = pd.read_csv('student_scores.csv')
print(scores)
scatterplot(scores)
