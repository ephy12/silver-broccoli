#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests
import pandas as pd
import json

###### copy paste your YNAB API personal token into line #10

######################################
### pass in personal token for authorization
session = requests.session()
header = {'Authorization': f'Bearer your_personal_token_goes_here'}
session.headers.update(header)

###Figuring out your budget ID
response = session.get(f'https://api.youneedabudget.com/v1/budgets/')
data = response.json()
budget = data["data"]["budgets"][0]
budget_id = budget.get("id")
#print(budget_id)

### Get all your transactions in your budget
response = session.get(f'https://api.youneedabudget.com/v1/budgets/{budget_id}/transactions/').json()
#print(response)
#print(json.dumps(response, indent=2))

### convert json response into dataframe using pandas.json_normalize()
df = pd.json_normalize(response["data"]["transactions"])

### export dataframe to csv file in current directory
new_df = pd.DataFrame(df)
new_df_csv = new_df.to_csv('all_transactions.csv')

### print list of columns in your dataframe
#print(df.keys())

####  create a new dataframe that only shows category name and amount for all transactions
#amounts_with_category = pd.DataFrame(df,columns=['category_name','amount','date'])
#print(amounts_with_category)

### Get list of all your accounts (including closed accounts) + account details and convert to dataframe
#response = session.get(f'https://api.youneedabudget.com/v1/budgets/{budget_id}/accounts/').json()
#print(response)
#df = pd.json_normalize(response["data"]["accounts"])
#print(df)

### Get list of all your categories with details
#response = session.get(f'https://api.youneedabudget.com/v1/budgets/{budget_id}/categories/').json()
#response.category_groups.name)
#print(response)

###create varaibles for category groups and categories underneath them
# first_category_group = response["data"]["category_groups"][0]["name"]
# first_category = response["data"]["category_groups"][0]["categories"][0]["name"]
# second_category = response["data"]["category_groups"][0]["categories"][1]["name"]
# third_category = response["data"]["category_groups"][0]["categories"][2]["name"]
# second_category_group = response["data"]["category_groups"][1]["name"]

### print out the first category group and the first 3 categories underneath
#print(first_category_group)
#print(first_category)
#print(second_category)
#print(third_category)

#print(second_category_group)

## pretty print so that you can see JSON hiearchy
#print(json.dumps(response, indent=2))


#df = pd.json_normalize(response['data']['category_groups'])
#get just the category group names
#category_groups = df['name']
#print(category_groups)
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




