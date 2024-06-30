# Import packages
import pandas as pd

# Defining the DataFrame 
df = pd.read_csv('./data.csv')
print(df)

# Defining the totals and converting them to integer values
totals = pd.to_numeric(df['Total'], downcast='integer', errors='coerce')

# Defining the overall value of each character by dividing their totals by how many fields make up that number
overall_value = totals / 6

# Creating a new field in our data frame and adding the overall values to each character
df['Overall Value'] = overall_value

# Rounding the overall values to the nearest whole numbers
df['Overall Value'] = df['Overall Value'].round(0)

# Writing the new overall value data to a csv file.
df.to_csv('./CSV/overall_value.csv')

# Seperating monsters by type 1, as not all creatures have a type 2
# Grass, Fire, Water, Bug, Normal, Poison, Electric, Ground, Fairy, 
# Fighting, Psychic, Rock, Ghost, Ice, Dragon, Dark, Steel, Flying.

# Grass type monsters
grass_type = df.loc[df['Type 1'] == 'Grass']
# Saving grass type monsters to a csv file
grass_type.to_csv('./CSV/grass.type.csv')

# Fire type monsters
fire_type = df.loc[df['Type 1'] == 'Fire']
# Saving fire type to a csv file
fire_type.to_csv('./CSV/fire.type.csv')

# Water type monsters
water_type = df.loc[df['Type 1'] == 'Water']
# saving water type monsters to a csv file
water_type.to_csv('./CSV/water.type.csv')

# Bug type mpnsters
bug_type = df.loc[df['Type 1'] == 'Bug']
# Sacing bug type to a csv file
bug_type.to_csv('./CSV/bug.type.csv')

# Normal type monsters
normal_type = df.loc[df['Type 1'] == 'Normal']
# Saving normal type to a csv
normal_type.to_csv('./CSV/normal.type.csv')










