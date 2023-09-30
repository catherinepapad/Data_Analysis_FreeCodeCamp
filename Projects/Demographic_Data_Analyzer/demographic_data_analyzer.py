import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

def calculate_demographic_data(print_data=True):
  # Read data from file
  df = pd.read_csv("C:/Users/Katerina/Documents/GitHub/Data_Analysis/Demographic_Data_Analyzer/adult.data.csv")
  print(df.columns)
  #print(df.shape)
  
  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = df["race"].value_counts()
  
  # What is the average age of men?
  average_age_men = df.loc[df["sex"] == "Male", "age"].mean().round(1)

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = round((100*sum(df['education'] == 'Bachelors') / df.shape[0]),1)

  # How many people are with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = len(df.loc[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate']))])
  lower_education = df.shape[0] - higher_education
  
  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  bachelors_rich = len(df[(df["education"] == "Bachelors") & (df["salary"] == '>50K')])
  masters_rich = len(df[(df["education"] == "Masters") & (df["salary"] == '>50K')])
  doctorates_rich = len(df[(df["education"] == "Doctorate") & (df["salary"] == '>50K')])
  higher_education_rich = round((100*(bachelors_rich + masters_rich + doctorates_rich) / higher_education),1)
  
  # What percentage of people without advanced education make more than 50K?
  lower_education_rich = round((100*(len(df[(df["salary"] == ">50K")]) - bachelors_rich - masters_rich - doctorates_rich) / lower_education),1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = df["hours-per-week"].min()
  
  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = len(df[(df["hours-per-week"] == df['hours-per-week'].min())])
  min_workers_rich = len(df[(df["hours-per-week"] == df['hours-per-week'].min()) & (df["salary"] == '>50K')])
  
  rich_percentage = round((100*min_workers_rich / num_min_workers),1)

  # What country has the highest percentage of people that earn >50K?
  df1 = df.copy()
  indexSalary = df1[(df1["salary"] == "<=50K")].index
  df1.drop(indexSalary , inplace=True)

  df2 = df.copy()
  indexSalary = df2[(df2["salary"] == ">50K")].index
  df2.drop(indexSalary , inplace=True)
  
  country_sum_rich = df1["native-country"].value_counts()
  country_sum_not_rich = df2["native-country"].value_counts()

  country_percentage = pd.Series()
  for country in country_sum_rich.index:
    country_percentage[country] = country_sum_rich[country] / (country_sum_rich[country] + country_sum_not_rich[country])

  highest_earning_country_percentage = round(100*country_percentage.max(),1)
  highest_earning_country = country_percentage[country_percentage == country_percentage.max()].index[0]
 
  # Identify the most popular occupation for those who earn >50K in India.
  df1 = df.loc[df["native-country"] == "India"]
  indexSalary = df1[(df1["salary"] == "<=50K")].index
  df1.drop(indexSalary , inplace=True)
  
  top_IN_occupation = df1["occupation"].value_counts().index[0]
  

  # DO NOT MODIFY BELOW THIS LINE
  if print_data:
    print("Number of each race:\n", race_count) 
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
    print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
    print(f"Min work time: {min_work_hours} hours/week")
    print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
    print("Country with highest percentage of rich:", highest_earning_country)
    print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
    print("Top occupations in India:", top_IN_occupation)

  return {
      'race_count': race_count,
      'average_age_men': average_age_men,
      'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
      'lower_education_rich': lower_education_rich,
      'min_work_hours': min_work_hours,
      'rich_percentage': rich_percentage,
      'highest_earning_country': highest_earning_country,
      'highest_earning_country_percentage':
      highest_earning_country_percentage,
      'top_IN_occupation': top_IN_occupation
  }
