#!/usr/bin/env python
# coding: utf-8

# In[1]:


# magic command to display matplotlib plots inline within the ipython notebook webpage
get_ipython().run_line_magic('matplotlib', 'inline')

# import necessary modules
import pandas as pd, numpy as np, matplotlib.pyplot as plt


# In[25]:


# create a pandas dataframe from the location data set
df = pd.read_csv("C:\PTUA\Lab05\summer-travel-gps-full.csv")
df.head()


# In[3]:


# Q1: how to get 2 columns from the dataframe (city and country)?
selected_columns = df[['city', 'country']]


# In[5]:


selected_columns.head()


# In[6]:


# Q2: how to get the first 5 rows of the "city" column?
first_5_cities = df['city'].head(5)
first_5_cities


# In[9]:


# Q3: how to use .loc to select the third row of the dataframe?
third_row = df.loc[2]
third_row 


# In[10]:


# Q4: how to use .loc to select the first row in "country" column?
first_row_country = df.loc[0, 'country']
first_row_country


# In[11]:


# Q5: how to select the first 4 rows of ['city', 'date'] columns?
selected_rows = df.loc[0:3, ['city', 'date']]
selected_rows


# In[12]:


# use .iloc for integer position based indexing
# Q6: how to get the value from the row in position 3 and the column in position 2
value_at_position = df.iloc[2, 1]
value_at_position


# In[26]:


# Q7: how to use iloc to select every 300th row from a data set?
every_300th_row = df.iloc[::300]
every_300th_row


# In[24]:


# load a reduced set of gps data
df1 = pd.read_csv("C:\PTUA\Lab05\summer-travel-gps-simplified.csv")
df1.tail()


# In[28]:


# Q9: create a Series of true/false, indicating if each "city" row in the column is equal to "Munich"
df1['is_munich'] = (df1['city'] == 'Munich')
df1


# In[29]:


# pandas logical operators are: | for or, & for and, ~ for not
# these must be grouped by using parentheses
# Q10: what cities were visited in spain that were not barcelona? Create a dataframe for it. 
spain_not_barcelona_df = df1[(df1['country'] == 'Spain') & (df1['city'] != 'Barcelona')]
spain_not_barcelona_df 


# In[30]:


# Q11: select rows where either the city is munich, or the country is serbia？
munich_or_serbia_df = df1[(df1['city'] == 'Munich') | (df1['country'] == 'Serbia')]
munich_or_serbia_df 


# In[32]:


# Q12: how many observations are west of the prime meridian?
west_of_prime_meridian_count = len(df1[df1['lon'] < 0])

print("Number of observations west of the prime meridian:", west_of_prime_meridian_count)


# In[33]:


# Q13: get all rows that contain a city that starts with the letter G？
cities_starting_with_G_df = df1[df1['city'].str.startswith('G')]
print(cities_starting_with_G_df)


# In[35]:


# Q14: how many unique cities and countries in the dataset? 
# Also can you check missing values for the dataframe

unique_cities = df1['city'].nunique()
unique_countries = df1['country'].nunique()

missing_values = df1.isnull().sum()

print("Number of unique cities:", unique_cities)
print("Number of unique countries:", unique_countries)
print("\nMissing values in the DataFrame:",missing_values)


# In[36]:


# Q15: group by country name and show the city names in each of the country

grouped_by_country = df1.groupby('country')['city'].unique()

print(grouped_by_country)


# In[37]:


# load the location data set, indexed by the date field
# and, parse the dates so they're no longer strings but now rather Python datetime objects
# this lets us do date and time based operations on the data set
dt = pd.read_csv("C:\PTUA\Lab05\summer-travel-gps-full.csv", index_col='date', parse_dates=True)
dt.head()


# In[38]:


# Q16: is the timestamp index unique? How can you use code to find it? 
is_index_unique = dt.index.is_unique

print("Is the timestamp index unique?", is_index_unique)


# In[48]:


import pandas as pd

# Load the location dataset, index by the 'date' field, and parse the dates
dt = pd.read_csv("C:\\PTUA\\Lab05\\summer-travel-gps-full.csv", index_col='date', parse_dates=True)

# Drop duplicate indices
dt = dt[~dt.index.duplicated(keep='first')]

# Display the first few rows of the DataFrame
dt


# In[50]:


weekday_df = dt[dt.index.weekday < 5]
weekend_df = dt[dt.index.weekday >= 5]
print("Weekday DataFrame:")
print(weekday_df)

print("\nWeekend DataFrame:")
print(weekend_df)


# In[51]:


#Q19: calculate and plot the number of observations each day of the week has

dt['weekday'] = dt.index.day_name()
observations_by_day = dt['weekday'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
observations_by_day.plot(kind='bar', color='skyblue')
plt.title('Number of Observations Each Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Observations')
plt.show()


# In[ ]:




