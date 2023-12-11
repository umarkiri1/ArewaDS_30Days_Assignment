# Create an empty tuple
tpl = tuple()

# Create two tuples each containing names of your sisters and your brothers (imaginary siblings are fine)
my_brothers = ('Muhammad','Abubakar')
my_sisters = ('Salma','Khadija','Halima')
# Join brothers and sisters tuples and assign it to siblings
siblings = my_brothers + my_sisters
print(siblings)

# How many siblings do you have?
print(len(siblings)) # 5 

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
parents = ['Aliyu','Suwaida']
family_members = siblings + parents
print("Family_members: ",family_members)

# Unpack siblings and parents from family_members
*sibs,father, mother = family_members
print(sibs)  # sibs = siblings unpacked
a,b,c,d,e,*parents = family_members
print(parents) 


# Create fruits, vegetables and animal products tuples. 
# Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apples','Grapes','Banana')
vegetables = ('Cabbage','lettuce')
animal_products = ('Diary','Eggs','Meat', 'Honey')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
len(food_stuff_tp) # length is 8
food_stuff_tp[int(len(food_stuff_tp)/2)-1:int(len(food_stuff_tp)/2)+1] # ('Spinach','Lettuce')

# Slice out the first three items and the last three items from food_staff_lt list
food_stuff_list[0:3]  # first three
food_stuff_list[-3:]  # last three
# Delete the food_staff_tp tuple completely
del food_stuff_tp
# confirming
print(food_stuff_tp)  # NameError
# Check if an item exists in tuple:
'Grapes' in food_stuff_tp #NameError:  food stuff tupple no longer exists
# However,checking the list
'Grapes' in food_stuff_list # returns True
# Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
'Estonia' in nordic_countries # false
'Iceland' in nordic_countries  # True 