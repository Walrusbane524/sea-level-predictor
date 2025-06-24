import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    data.plot(x='Year', y='CSIRO Adjusted Sea Level', kind='scatter', color="#006B8C")

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])

    years = pd.Series(range(1880, 2051))
    line = years * slope + intercept

    plt.plot(years, line, color="#00FF0D")

    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    slope, intercept, r_value, p_value, std_err = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(2000, 2051))
    line = years * slope + intercept

    plt.plot(years, line, color="#B40000")


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()