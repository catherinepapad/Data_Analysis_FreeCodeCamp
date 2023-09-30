import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('C:/Users/Katerina/Documents/GitHub/Data_Analysis/Sea_Level_Predictor/epa-sea-level.csv')

  # Create scatter plot
  plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

  # Create first line of best fit
  best_fit_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  #Years = range(1880, 2061, 1)
  Years = range(1880, 2051, 1)
  plt.plot(Years, best_fit_1.intercept + best_fit_1.slope*Years, color = 'red')
  
  # Create second line of best fit
  df_newer = df[df['Year']>= 2000]
  best_fit_2 = linregress(df_newer['Year'], df_newer['CSIRO Adjusted Sea Level'])
  Years = range(2000, 2051, 1)
  plt.plot(Years, best_fit_2.intercept + best_fit_2.slope*Years, color = 'orange')

  # Add labels and title
  plt.xlim([1870, 2060])
  plt.title('Rise in Sea Level')
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  #plt.show()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('Sea_Level_Predictor/sea_level_plot.png')
  return plt.gca()