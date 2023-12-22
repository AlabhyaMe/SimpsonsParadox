#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Setting the seed for reproducibility
np.random.seed(259)

# Function to generate data for each area
def generate_data(mean_hours, sd_hours, mean_income, sd_income, n, base_income, area_name):
    hours = np.random.normal(mean_hours, sd_hours, n)
    income = 0.25 * np.abs(hours * np.random.normal(mean_income, sd_income, n)) + base_income
    return pd.DataFrame({'Hours': hours, 'Income': income, 'Area': area_name})

# Generate data for each area
AreaSD_df = generate_data(90, 3, 105, 5, 100, 700, 'AreaSD')
AreaLA_df = generate_data(92, 3, 97, 6, 90, 500, 'AreaLA')
AreaB_df = generate_data(93, 3, 90, 6, 110, 100, 'AreaB')
AreaI_df = generate_data(93, 4, 73, 5, 80, 0, 'AreaI')
AreaR_df = generate_data(96, 3, 68, 4, 75, -300, 'AreaR')

# Combine all areas into a single DataFrame
all_data = pd.concat([AreaSD_df, AreaLA_df, AreaB_df, AreaI_df, AreaR_df])


# In[11]:


# Plotting for each area
def plot_area(data, color, title):
    sns.scatterplot(x='Hours', y='Income', data=data, color=color)
    plt.title(title)
    plt.xlabel("Hours")
    plt.ylabel("Income")
    plt.show()

plot_area(AreaSD_df, "darkgreen", "Area SD")
plot_area(AreaLA_df, "darkblue", "Area LA")
plot_area(AreaB_df, "darkorange", "Area Berkeley")
plot_area(AreaI_df, "darkred", "Area Irvine")
plot_area(AreaR_df, "brown", "Area Riverside")


# In[12]:


# Perform linear regression for each area
def perform_regression(x, y):
    x_with_const = sm.add_constant(x)
    model = sm.OLS(y, x_with_const).fit()
    print(model.summary())

for df in [AreaSD_df, AreaLA_df, AreaB_df, AreaI_df, AreaR_df]:
    perform_regression(df['Hours'], df['Income'])

# Perform linear regression on the combined data
all_data_encoded = pd.get_dummies(all_data, columns=['Area'], drop_first=True)
model_all = sm.OLS(all_data_encoded['Income'], sm.add_constant(all_data_encoded.drop('Income', axis=1))).fit()
print(model_all.summary())

# Plotting combined data with regression line
sns.lmplot(x="Hours", y="Income", hue="Area", data=all_data, ci=None)
plt.show()

