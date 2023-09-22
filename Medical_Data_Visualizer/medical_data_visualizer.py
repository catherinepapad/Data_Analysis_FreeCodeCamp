import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('C:/Users/Katerina/Documents/GitHub/Data_Analysis/Medical_Data_Visualizer/medical_examination.csv')


# Add 'overweight' column
BMI = df['weight'] / ((df['height'] / 100) ** 2)

BMI_cases = [
  (BMI <= 25),
  (BMI > 25)
]
categories = [0, 1]
df['overweight'] = np.select(BMI_cases, categories)
 

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
chol_cases = [
  (df['cholesterol'] == 1),
  (df['cholesterol'] > 1)
]
gluc_cases = [
  (df['gluc'] == 1),
  (df['gluc'] > 1)
]

df['cholesterol'] = np.select(chol_cases, categories)
df['gluc'] = np.select(gluc_cases, categories)



# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df, value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'], id_vars='cardio')

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = df_cat.value_counts().reset_index(name='count')
  df_cat = df_cat.sort_values('variable')

  # Draw the catplot with 'sns.catplot()'
  chart = sns.catplot(data = df_cat, kind = 'bar', x = 'variable', y = 'count', hue = 'value', col = 'cardio')
  chart.set_ylabels('total')
  #plt.show()

  # Get the figure for the output
  fig = chart.fig

  # Do not modify the next two lines
  fig.savefig('Medical_Data_Visualizer/catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[(df['ap_lo'] <= df['ap_hi']) & 
    (df['height'] >= (df['height'].quantile(0.025))) &
    (df['height'] <= (df['height'].quantile(0.975))) &
    (df['weight'] >= (df['weight'].quantile(0.025))) &
    (df['weight'] <= (df['weight'].quantile(0.975)))
  ]

  # Calculate the correlation matrix
  corr = df_heat.corr()
  #corr = round(corr,1)

  # Generate a mask for the upper triangle
  mask = np.zeros_like(corr)
  mask[np.triu_indices_from(mask)] = True

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(5, 5))

  # Draw the heatmap with 'sns.heatmap()'
  sns.set(font_scale=0.4)
  sns.heatmap(corr, center=0.09, square = True, annot = True, fmt = '.1f', mask=mask); #, fmt='.1f'
  
  # Do not modify the next two lines
  fig.savefig('Medical_Data_Visualizer/heatmap.png')
  return fig
