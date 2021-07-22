
import pandas as pd
import json

# you can use this as a script with a json response stored as a file, or can just use same indexing on raw JSON resonse from YNAB server
# if you wanted to do this as a function just declare function and include parameter 'json' that must be passed into the function

# read in json file
json = pd.read_json('filename.json')

# declare counters and assign starting value
catgr_counter = 0
cat_counter = 0

# create empty lists - optional
my_cat_group_list = []
my_categories_list = []

# referencing category groups list and storing as variable (will loop through this list below)
category_group_list = json['data']['category_groups']

#outer for loop to go through all of the category groups
for catg in category_group_list:
	# referencing category group name and updating the category list which will loop through as 'inner loop'
	category_group_name = json['data']['category_groups'][catgr_counter]['name']
	category_list = json['data']['category_groups'][catgr_counter]['categories']
	# inner for loop to pull category group name and do other actions
	for cat in category_list:
		category_name = json['data']['category_groups'][catgr_counter]['categories'][cat_counter]['name']
		# the action to be taken within inner for loop (here I am printing the variables we stored from outer and inner loop and appending the values to respective lists)
		print(category_group_name, ': ', category_name)
		my_categories_list.append(category_name)
		cat_counter = cat_counter +1
	
	#these below actions are part of outer loop
	my_cat_group_list.append(category_gorup_name)
	catgr_counter = catgr_counter + 1
	cat_counter = 0 # resetting counter for innner loop

# can print out lists to see how they look
print(my_cat_group_list)
print(my_categories_list)


		

