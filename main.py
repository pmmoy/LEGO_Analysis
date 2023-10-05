
#What is the most enormous LEGO set ever created and how many parts did it have?

# --> The Ultimate Battle for Chima with 9987 LEGO parts

#In which year were the first LEGO sets released and how many sets did the company sell when it first launched?

# --> The company's first sets were released in 1949 and the total number of sets was 5 at launch

#Which LEGO theme has the most sets? Is it Harry Potter, Ninjago, Friends or something else?

# --> Star Wars holds the most sets at 753

#When did the LEGO company really take-off based on its product offering? How many themes and sets did it release every year?

# --> LEGO took off in 2010 based on how many products were offered. The amount of themes and sets released per year changed drastically 

# --> in the early years of the company 1949 to 1955, it produced an average of 11 sets and 2 themes

# --> Later years of the company from 2017 to 2020, it produced an average of 779 sets and 85 themes

#Did LEGO sets grow in size and complexity over time? Do older LEGO sets tend to have more or fewer parts than newer sets?

# --> LEGO definitely grew in size and complexity over time, Majority of the older LEGO sets tend to have fewer parts than newer sets

# LEGOS Analysis

<img src ="https://i.imgur.com/49FNOHj.jpg">

import pandas as pd

df = pd.read_csv("colors.csv")

#finds the number of unique lego brick colors
df['name'].nunique()

df.head()

#finds the number of transparent lego brick colors

df.groupby('is_trans').count()

df.is_trans.value_counts()

sets = pd.read_csv('sets.csv')

sets

#In which year were the first LEGO sets released and what were these sets called?
sets.sort_values('year').head()

#Finds all the LEGO sets that were created in their first year in business
sets[sets['year'] == 1949]

#how many different products did the LEGO company sell in their first year of operation?
sets['name'].nunique()

#Finds the LEGO set with the largest number of parts

sets.sort_values('num_parts', ascending=False).head()

import matplotlib.pyplot as plt

#Grouping the sets by year to find how many sets were made per year
sets_by_year = sets.groupby('year').count()
sets_by_year['set_num'].head()

sets_by_year['set_num'].tail()

#plotting all the data of number of sets
plt.plot(sets_by_year.index, sets_by_year.set_num)

#Cleaning up chart to reflect data more accurately because data only contains the "beginning" of 2021
#we see jumps from 1960, 1980, 2000, 2010 followed by a heavy decline after the year of jumps
#1990 was a big year and produced a dramatic amount of LEGO sets
#There is a decline in early 2000's, but picked back up in 2005

#We slice off the year of 2021
plt.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2])

#Creating a Dataframe to analyze themes by year
themes_by_year = sets.groupby ('year').agg({'theme_id' : pd.Series.nunique})

#Renaming the column
themes_by_year.rename(columns = {'theme_id' : 'nr_themes'}, inplace = True)

#LEGO had less than 5 themes per year in their first 5 years in business
themes_by_year.head()

#LEGO has jumped significantly up to 9 times compared to years before
themes_by_year.tail()

#The number of sets grew dramatically from 1960 to 2000
#After 2002 the number of sets was stagnant and didnt pick up again until 2010

plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

#We want to compare the themes vs sets per year, but we need to give them the same x axis and give each a different Y-axis
ax1 = plt.gca() #gets the axis
ax2 = ax1.twinx() # creates another axis and shares the same x-axis

ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')
ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color ='b')

#Styling to tell the difference between the Y-axis Ranges
ax1.set_xlabel('Year')
ax1.set_ylabel('Number of Sets', color ='green')
ax2.set_ylabel('Number of Themes', color = 'blue')

parts_per_set = sets.groupby('year').agg({'num_parts' : pd.Series.mean})

#parts_per_set.rename(columns = {'num_parts' : 'num_parts'}, inplace = True)
parts_per_set.head()

parts_per_set.tail()

#Scatter plot chart show to show trends of number of parts per year
#2010 had double the number of parts on average than in 1960

plt.scatter(parts_per_set.index[:-2], parts_per_set.num_parts[:-2])

#find the most popular sets
#"ID" LEFT --- "NUMBER OF SETS" RIGHT

set_theme_count = sets["theme_id"].value_counts()
set_theme_count[:5]

themes = pd.read_csv('themes.csv')
themes.head()

#Looking at number of themes under "Star Wars"
themes[themes.name == 'Star Wars']

#Looking through how many sets 18 has
sets[sets.theme_id == 18]

#Looking through how many sets 18 has
#All the Star Wars Advent Calendars share the same "theme_id" 
sets[sets.theme_id == 209]

#combining the data we found in theme count to find the names corresponding to each
#both the "set_theme_count" and "themes" DataFrames have a common column named "id", we can merge using the same column
merged_df = pd.merge(set_theme_count, themes, on='id')
merged_df[:3]

plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Nr of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])

