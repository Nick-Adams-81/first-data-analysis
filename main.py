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

# Poison type monsters
poison_type = df.loc[df['Type 1'] == 'Poison']
# Saving poison type to csv
poison_type.to_csv('./CSV/poison.type.csv')

# Electric type monsters
electric_type = df.loc[df['Type 1'] == 'Poison']
# Saving electric type tp csv
electric_type.to_csv('./CSV/electric.type.csv')

# Ground type monsters
ground_type = df.loc[df['Type 1'] == 'Ground']
# Saving ground type monsters to a csv file
ground_type.to_csv('./CSV/ground.type.csv')

# Fairy type monsters
fairy_type = df.loc[df['Type 1'] == 'Fairy']
# Saving fairy type to a csv file
fairy_type.to_csv('./CSV/fairy.type.csv')

# Fighting type monsters
fighting_type = df.loc[df['Type 1'] == 'Fighting']
# Saving fighting type to a csv file
fighting_type.to_csv('./CSV/fighting.type.csv')

# Psychic type monsters
psychic_type = df.loc[df['Type 1'] == 'Psychic']
# Saving psychic type to a csv file
psychic_type.to_csv('./CSV/psychic.type.csv')

# Rock type monsters
rock_type = df.loc[df['Type 1'] == 'Rock']
# Saving rock type monsters to a csv file
rock_type.to_csv('./CSV/rock.type.csv')

# Ghost type monsters
ghost_type = df.loc[df['Type 1'] == 'Ghost']
# Saving ghost type to a csv file
ghost_type.to_csv('./CSV/ghost.type.csv')

# Ice type monsters
ice_type = df.loc[df['Type 1'] == 'Ice']
# Saving ice type to a csv file
ice_type.to_csv('./CSV/ice.type.csv')

# Dragon type monsters
dragon_type = df.loc[df['Type 1'] == 'Dragon']
# Saving dragon type monsters to a csv file
dragon_type.to_csv('./CSV/dragon.type.csv')

# Dark type monsters
dark_type = df.loc[df['Type 1'] == 'Dark']
# Sacving dark type to a csv file
dark_type.to_csv('./CSV/dark.type.csv')

# Steel type monsters
steel_type = df.loc[df['Type 1'] == 'Steel']
# Saving steel type to a csv file
steel_type.to_csv('./CSV/steel.type.csv')

# Flying type monsters
flying_type = df.loc[df['Type 1'] == 'Flying']
# Saving flying type to a csv file
flying_type.to_csv('./CSV/flying.type.csv')










