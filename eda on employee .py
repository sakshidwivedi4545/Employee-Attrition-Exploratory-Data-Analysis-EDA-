#!/usr/bin/env python
# coding: utf-8

# # EXPLORATORY DATA ANALYSIS

# # # IMPORTING LIBRARIES

# In[3]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# # IMPORT CSV FILE
# data = pd.read_csv("C:/Users/sumit/OneDrive/Desktop/employeee.csv")
# 
# 

# #  Initial Exploration

# In[20]:


data.head()


# In[21]:


data.tail()


# In[22]:


data.info()


# In[23]:


data.describe()


# # # Age and Years at Company vs Attrition

# plt.figure(figsize=(6, 4))
# sns.countplot(data=data, x='Attrition')
# plt.title('Attrition Distribution')
# plt.show()

# In[25]:


plt.figure(figsize=(8, 6))
sns.scatterplot(data=data, x='Age', y='DistanceFromHome', hue='Attrition')
plt.title('Age vs Distance from Home')
plt.show()


# # Hypothesis Testing 

# In[28]:


import pandas as pd
from scipy.stats import ttest_ind

# Load the dataset (replace 'employee_data.csv' with your actual file path)
data = pd.read_csv('employeee.csv')

# Encode 'Attrition' column: 'Yes' -> 1, 'No' -> 0
data['Attrition'] = data['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

# Example of t-test comparing age for attrited and non-attrited employees
attrited_age = data[data['Attrition'] == 1]['Age']
non_attrited_age = data[data['Attrition'] == 0]['Age']
t_statistic, p_value = ttest_ind(attrited_age, non_attrited_age)
print("T-Statistic for Age:", t_statistic)
print("P-Value for Age:", p_value)


# # DATA VISUALISATION:# Grouped bar plot: Attrition rates by EducationField and MaritalStatus
# 

# In[29]:


plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='EducationField', y='Attrition', hue='MaritalStatus')
plt.title('Attrition Rates by EducationField and MaritalStatus')
plt.xticks(rotation=45)
plt.show()


# ## Age and Years at Company vs Attrition
# 

# In[30]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='Attrition', y='Age')
plt.title('Age Distribution by Attrition')
plt.show()


# ## Percent Salary Hike vs Performance Rating
# 

# In[31]:


plt.figure(figsize=(10, 6))
sns.boxplot(data=data, x='PerformanceRating', y='PercentSalaryHike')
plt.title('Percent Salary Hike by Performance Rating')
plt.show()


# ## Relationship Satisfaction and Performance Rating
#  

# In[33]:


plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='RelationshipSatisfaction', y='PerformanceRating', hue='Attrition')
plt.title('Relationship Satisfaction vs Performance Rating')
plt.show()


# In[ ]:




