import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Function  for Transposing data
def getdata(filename):
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(filename)
    countrywise_df = df.set_index(['Country Name', 'Indicator Name']).stack().unstack(0).reset_index()
    countrywise_df.columns.name = None
    return df, countrywise_df


file_path = 'indicatordata.csv'
df, countrywise_df = getdata(file_path)
# print(countrywise_df.head())

'''countrywise_df.to_csv('countrywise.csv')'''

# Summary Statistics for few countries
'''countries = ['Bahrain', 'France', 'Pakistan']
indicators = ['Population, total']
selected_data =original_df[original_df['Country Name'].isin(countries) & original_df['Indicator Name'].isin(selected_indicators)]
selected_data_numeric = selected_data.drop(['Country Name','Indicator Name'], axis=1)
summary_stats = selected_data_numeric.describe()
mean_values = selected_data_numeric.mean()
median_values = selected_data_numeric.median()
std_dev_values = selected_data_numeric.std()
print("Summary Statistics for Total Population:")
print(summary_stats)
print("\nMean Values:")
print(mean_values)
print("\nMedian Values:")
print(median_values)
print("\nStandard Deviation:")
print(std_dev_values)'''

# Correlation Heatmap.
'''selected_data = [countrywise_df['Indicator Name'] == 'Mortality rate, under-5 (per 1,000 live births)'][['Australia', 'France','Nepal']]
correlation_matrix = selected_data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap - Mortality Under 5')
plt.show()'''

# Line Chart Code
'''countrywise=pd.read_csv('countrywise.csv')
data = countrywise[(countrywise['Indicator Name'] == 'CO2 emissions from liquid fuel consumption (% of total)') &
                   (countrywise['Year'].notna())]  # Ensure there's a valid year

# Select only the relevant columns
selected_data = countrywise[['Year', 'Japan', 'Canada', 'Australia']]
grouped_data = selected_data.groupby('Year').sum()

# Plot the line chart
plt.figure(figsize=(10, 6))
plt.plot(grouped_data.index, grouped_data['Japan'], label='Japan')
plt.plot(grouped_data.index, grouped_data['Canada'], label='Canada')
plt.plot(grouped_data.index, grouped_data['Australia'], label='Australia')
plt.title('Carbon dioxide emission from liquid')
plt.xlabel('Year')
plt.ylabel('Co2 Emission from liquid')
plt.legend()
plt.grid(True)
plt.show()'''

# Pie Chart for Top5 Countries
'''cereal_yield_data = df[df['Indicator Name'] == 'Cereal yield (kg per hectare)']
years_columns = df.columns[2:]
# Sum the values across years for each country
cereal_yield_data['Total'] = cereal_yield_data[years_columns].sum(axis=1)
# Create a pie chart
plt.figure(figsize=(10, 8))
plt.pie(cereal_yield_data['Total'], labels=cereal_yield_data['Country Name'], autopct='%1.1f%%', startangle=90)
plt.title('Total Cereal Yield Distribution by Country')
plt.show()'''


#Bar Chart
'''barchart = countrywise_df[countrywise_df[
                         'Indicator Name'] == 'Electricity production from nuclear sources (% of total)'][
    ['Belgium', 'France']]
aggregated_data = barchart.sum()
aggregated_data.plot(kind='bar', color=['blue', 'orange', 'green', 'red'], figsize=(10, 6))
plt.title('Electricity Production- France vs Belgium')
plt.xlabel('Country')
plt.ylabel('Poverty Headcount')
plt.show()'''