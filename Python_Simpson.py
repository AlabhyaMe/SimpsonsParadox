#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Set the random seed for reproducibility
np.random.seed(259)

# Create data for each area
def create_area_data(mean_hours, sd_hours, mean_income, sd_income, n, area_name):
    hours = np.random.normal(mean_hours, sd_hours, n)
    income = np.abs(hours * np.random.normal(mean_income, sd_income, n))
    return pd.DataFrame({'Area': area_name, 'Hours': hours, 'Income': income})

# Creating data frames for each area
AreaSD = create_area_data(90, 15, 120, 10, 100, 'AreaSD')
AreaLA = create_area_data(100, 16, 100, 8, 90, 'AreaLA')
AreaB = create_area_data(120, 20, 75, 6, 110, 'AreaB')
AreaI = create_area_data(170, 16, 50, 5, 80, 'AreaI')
AreaR = create_area_data(190, 14, 45, 4, 75, 'AreaR')

# Combine all areas into one DataFrame
All = pd.concat([AreaSD, AreaLA, AreaB, AreaI, AreaR])

# Plotting
def plot_area(area_df, color, title):
    sns.scatterplot(data=area_df, x='Hours', y='Income', color=color).set_title(title)

plt.figure(figsize=(12, 10))
plt.subplot(321); plot_area(AreaSD, 'darkgreen', 'Area SD')
plt.subplot(322); plot_area(AreaLA, 'darkblue', 'Area LA')
plt.subplot(323); plot_area(AreaB, 'darkorange', 'Area SF')
plt.subplot(324); plot_area(AreaI, 'darkred', 'Area Irvine')
plt.subplot(325); plot_area(AreaR, 'brown', 'Area Riverside')
plt.tight_layout()
plt.show()



# In[2]:


# Regression analysis for each area
def run_regression(area_df):
    model = ols('Income ~ Hours', data=area_df).fit()
    return model.summary()

print(run_regression(AreaSD))
print(run_regression(AreaLA))
print(run_regression(AreaB))
print(run_regression(AreaI))
print(run_regression(AreaR))

# Combined regression
combined_reg = ols('Income ~ Hours', data=All).fit()
print(combined_reg.summary())

# Regression with area dummy
All_dummy = pd.get_dummies(All, columns=['Area'], drop_first=True)
model_with_dummy = ols('Income ~ Hours + Area_AreaLA + Area_AreaB + Area_AreaI + Area_AreaR', data=All_dummy).fit()
print(model_with_dummy.summary())






# In[3]:


# Plotting with regression line
plt.figure(figsize=(10, 6))
sns.scatterplot(data=All, x='Hours', y='Income', hue='Area')
sns.lineplot(data=All, x='Hours', y=combined_reg.predict(All), color='red')
plt.title('Scatter Plot with Combined Regression Line')
plt.show()


# In[4]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=All, x='Hours', y='Income', hue='Area')
sns.lineplot(data=All_dummy, x='Hours', y=model_with_dummy.predict(All_dummy), hue=All_dummy.filter(regex='Area_').idxmax(axis=1))
plt.title('Scatter Plot with Regression Lines by Area')
plt.show()

