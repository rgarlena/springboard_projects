#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.cm import viridis


# In[2]:


# Load the uploaded datasets
file_1_path = '1-incidence-of-tuberculosis-sdgs.csv'
file_2_path = '2-tuberculosis-deaths-by-age.csv'
file_3_path = '3-tuberculosis-case-detection-rate.csv'
file_4_path = '4-tuberculosis-treatment-success-rate-by-type.csv'
file_5_path = '5-tuberculosis-patients-with-hiv-share.csv'
file_6_path = '6-tuberculosis-deaths-under-five-ihme.csv'

# Read the datasets into pandas DataFrames
df_tb_incidence = pd.read_csv(file_1_path)
df_tb_deaths_age = pd.read_csv(file_2_path)
df_tb_detection_rate = pd.read_csv(file_3_path)
df_tb_treatment_success = pd.read_csv(file_4_path)
df_tb_hiv_share = pd.read_csv(file_5_path)
df_tb_deaths_under_five = pd.read_csv(file_6_path)


# In[3]:


df_tb_incidence.head()


# In[4]:


df_tb_deaths_age.head()


# In[5]:


df_tb_detection_rate.head()


# In[6]:


df_tb_treatment_success.head()


# In[7]:


df_tb_hiv_share.head()


# In[8]:


df_tb_deaths_under_five.head()


# In[9]:


# Group the TB incidence data by year to get the global trend
global_tb_incidence = df_tb_incidence.groupby('Year')['Estimated incidence of all forms of tuberculosis'].mean()

# Use viridis colormap and select a color (e.g., from 0.6 in the range of 0-1)
color = viridis(0.6)

# Plot Global TB Incidence Trend with a color from viridis
plt.figure(figsize=(10, 6))
plt.plot(global_tb_incidence.index, global_tb_incidence.values, marker='o', color=color)
plt.title('Global Tuberculosis Incidence Trend (2000-2020)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Estimated Incidence (Per 100,000 People)', fontsize=12)
plt.grid(True)
plt.show()


# In[10]:


# Merging based on correct column names
df_detection_treatment = pd.merge(
    df_tb_detection_rate[['Entity', 'Year', 'Case detection rate (all forms)']],
    df_tb_treatment_success[['Entity', 'Year', 'Indicator:Treatment success rate: new TB cases']],
    on=['Entity', 'Year']
)

# Drop rows with missing values
df_detection_treatment_clean = df_detection_treatment.dropna()

# Apply 'viridis' colormap for the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df_detection_treatment_clean['Case detection rate (all forms)'],
            df_detection_treatment_clean['Indicator:Treatment success rate: new TB cases'],
            alpha=0.7, c=df_detection_treatment_clean['Case detection rate (all forms)'], cmap='viridis')

plt.title('Case Detection Rate vs Treatment Success Rate', fontsize=14)
plt.xlabel('Case Detection Rate (%)', fontsize=12)
plt.ylabel('Treatment Success Rate (%)', fontsize=12)
plt.colorbar(label='Case Detection Rate (%)')
plt.grid(True)
plt.show()


# In[11]:


# Group the TB-HIV dataset by year to get the average share of TB patients with HIV
tb_hiv_share_by_year = df_tb_hiv_share.groupby('Year')['Estimated HIV in incident tuberculosis'].mean()

# Use viridis colormap and select a color (e.g., from 0.6 in the range of 0-1)
color = viridis(0.2)

# Plot the share of TB patients with HIV over time using a color from the viridis palette
plt.figure(figsize=(10, 6))
plt.plot(tb_hiv_share_by_year.index, tb_hiv_share_by_year.values, marker='o', color=color)
plt.title('Share of TB Patients with HIV Over Time (2000-2020)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Share of TB Patients with HIV (%)', fontsize=12)
plt.grid(True)
plt.show()


# In[12]:


# Create a DataFrame with TB deaths by different age groups over time
df_tb_deaths_by_age_group = df_tb_deaths_age.groupby('Year').sum()

# Plot TB deaths by age group over time
plt.figure(figsize=(10, 6))

# Plot each age group in a separate line
plt.plot(df_tb_deaths_by_age_group.index, df_tb_deaths_by_age_group['Deaths - Tuberculosis - Sex: Both - Age: Under 5 (Number)'], label='Under 5', marker='o', color=viridis(0.2))
plt.plot(df_tb_deaths_by_age_group.index, df_tb_deaths_by_age_group['Deaths - Tuberculosis - Sex: Both - Age: 5-14 years (Number)'], label='5-14 years', marker='o', color=viridis(0.4))
plt.plot(df_tb_deaths_by_age_group.index, df_tb_deaths_by_age_group['Deaths - Tuberculosis - Sex: Both - Age: 15-49 years (Number)'], label='15-49 years', marker='o', color=viridis(0.6))
plt.plot(df_tb_deaths_by_age_group.index, df_tb_deaths_by_age_group['Deaths - Tuberculosis - Sex: Both - Age: 50-69 years (Number)'], label='50-69 years', marker='o', color=viridis(0.8))
plt.plot(df_tb_deaths_by_age_group.index, df_tb_deaths_by_age_group['Deaths - Tuberculosis - Sex: Both - Age: 70+ years (Number)'], label='70+ years', marker='o', color=viridis(1.0))

# Adding titles and labels
plt.title('Tuberculosis Deaths by Age Group Over Time (1990-2020)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Deaths', fontsize=12)
plt.grid(True)
plt.legend(title="Age Groups")
plt.show()


# In[ ]:




