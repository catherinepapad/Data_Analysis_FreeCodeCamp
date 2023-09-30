import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(
  'C:/Users/Katerina/Documents/GitHub/Data_Analysis/Page_View_Time_Series_Visualizer/fcc-forum-pageviews.csv',
  sep=',',
  #skiprows = 1,
  #header = None,
  #names = ['date', 'value'],
  index_col='date',
  parse_dates=True)
  #print(df.head())
  #print('---------')
  #print(df.tail())
  #print(df.index)

# Clean data
df = df[(df['value'] >= (df['value'].quantile(0.025)))
      & (df['value'] <= (df['value'].quantile(0.975)))]


def draw_line_plot():
  # Copy data
  df_line = df.copy()

  # Draw line plot
  fig = plt.subplots(figsize=(20, 5))
  chart = sns.lineplot(x='date', y='value', data=df_line, color='red')
  chart.set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019', xlabel='Date', ylabel='Page Views')

  # Save image and return fig (don't change this part)
  fig = chart.get_figure()
  fig.savefig('Page_View_Time_Series_Visualizer/line_plot.png')
  return fig


def draw_bar_plot():
  # Copy and modify data for monthly bar plot
  df_bar = df.copy()
  df_bar = df_bar.groupby(pd.PeriodIndex(
    df_bar.index, freq="M"))['value'].mean().reset_index()
  #print(df_bar.head())
  df_bar['month'] = df_bar['date'].dt.month
  df_bar['month'] = df_bar['month'].astype(str)
  df_bar['year'] = df_bar['date'].dt.year
  #print(df_bar.head())

  # Draw bar plot
  fig, ax = plt.subplots(figsize=(12, 10))
  chart = sns.barplot(x='year', y='value', hue='month', data=df_bar)
  chart.set(xlabel='Years', ylabel='Average Page Views')
  plt.xticks(rotation=90)
  hands, labs = ax.get_legend_handles_labels()
  plt.legend(handles=hands,
             loc=2,
             title='Months',
             labels=[
               'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
             fontsize=12,
             title_fontsize=12)

  # Save image and return fig (don't change this part)
  fig = chart.get_figure()
  fig.savefig('Page_View_Time_Series_Visualizer/bar_plot.png')
  return fig


def draw_box_plot():
  # Prepare data for box plots (this part is done!)
  df_box = df.copy()
  df_box.reset_index(inplace=True)
  df_box['year'] = [d.year for d in df_box.date]
  df_box['month'] = [d.strftime('%b') for d in df_box.date]

  month_order = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

  # Draw box plots (using Seaborn)
  fig, axes = plt.subplots(1, 2, figsize=(15, 5))
  chart1 = sns.boxplot(data=df_box,
                       x='year',
                       y='value',
                       ax=axes[0],
                       linewidth=0.5,
                       flierprops=dict(markerfacecolor='0.50', markersize=2))
  chart2 = sns.boxplot(data=df_box,
                       x='month',
                       y='value',
                       order=month_order,
                       ax=axes[1],
                       linewidth=0.5,
                       flierprops=dict(markerfacecolor='0.50', markersize=2))
  chart1.set(xlabel='Year',
             ylabel='Page Views',
             title='Year-wise Box Plot (Trend)')
  chart2.set(xlabel='Month',
             ylabel='Page Views',
             title='Month-wise Box Plot (Seasonality)')

  # Save image and return fig (don't change this part)
  fig.savefig('Page_View_Time_Series_Visualizer/box_plot.png')
  return fig
