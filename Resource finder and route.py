#!/usr/bin/env python

## Created by gramadin
## Started in Oct 2019
## Revised 17 Dec 2019
## Current version only supports Wood, Thatch, Stone, and Fiber Blueprints
## (C) 2019 Edward Smythe
## Permission required for use of any code in whole or part
## edward.c.smythe+atlas_tool@gmail.com for support



import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import csv

myFile2 = pd.read_csv('Resource_repo.csv', sep=',')
myFile2 = myFile2.fillna('')
"""
##################################################################################################
#__All Functions__
# quality_check()               ~ indicate blueprint quality
# BP_qty()                      ~ get quantity of resources required from blueprint
# user_inv()                    ~ get user inventory
# valid_dest(X,Y)               ~ check if the location in dataframe to see if resource is available there
# dist_chk(ind)                 ~ get manhatten distnace from the player location to the destination grid
# resource_update(resource)     ~ update the map dataframe with resource locations
# temp_resource                 ~ *future implementation* cycle through all resources in the 'need_list'
# closest_loc                   ~ gets closest grid to player for a resource type
#####
#__Key Variables__
# quality                       ~ Bluprint quality, determines resource variety needed
# player_loc                    ~ map loaction of player
#player_loc_lat/long            ~ parsed location for use in atlas_map
# BP_fiber                      ~ Blueprint required fiber
# BP_stone                      ~ Blueprint required stone
# BP_thatch                     ~ Blueprint required thatch
# BP_wood                       ~ Blueprint required wood
# need_list                     ~ list of resources keys needed
##################################################################################################
"""


# Define quality and ask for user input on BP quality



quality = 1 # initilize quality
def quality_check():
    global quality
    print('1 = Common \n2 = Fine \n3 = Journeyman \n4 = Masterwork \n5 = Legendary \n6 = Mythical')

    
    while True:
        try:
            quality = int(input("What type of Build Quality? "))
            f'You chose {quality}'
            1 < quality < 7
            return (quality) ## i am not able to recall the quality after teh function is completed
            break
        except:
            f'{quality} is not a valid input. must be an integer between 1-6'
    if quality == 1:
        print('You chose Common.')
    elif quality == 2:
        print('You chose Fine.')
    elif quality == 3:
        print('You chose Journeyman.')
    elif quality == 4:
        print('You chose Masterwork.')
    elif quality == 5:
        print('You chose Legendary.')
    elif quality == 6:
        print('You chose Mythical.')
    else:
        print('Try again with a value from 1-6')


# Get Player World Location



player_loc = input("Where does the grind begin? ")
player_loc = player_loc.upper()
player_loc_lat = player_loc[0]
player_loc_long = int(player_loc[1:3])




player_x = ord(player_loc.lower()[0])-96
player_y = player_loc_long
print(f'player is at {player_x} x {player_y}')




## prompt user to enter BP requirments
BP_fiber = 0
BP_stone = 0
BP_thatch = 0
BP_wood = 0

def BP_qty():
    global BP_fiber, BP_stone, BP_thatch, BP_wood
    print('Enter the quantities from BP')

    
    while True:
        try:
            BP_wood = int(input("How much wood? "))
            f'You chose {BP_wood}'
            BP_thatch = int(input("How much thatch? "))
            f'You chose {BP_thatch}'
            BP_stone = int(input("How much stone? "))
            f'You chose {BP_stone}'
            BP_fiber = int(input("How much fiber? "))
            f'You chose {BP_fiber}'
            BP_fiber is int
            BP_stone is int
            BP_thatch is int
            BP_wood is int
            return f'You chose {BP_wood} wood, {BP_thatch} thatch, {BP_stone} stone and {BP_fiber} fiber.'
            break
        except:
            f'Please try again, values must be an integer.'
    




quality_check()


# ## Example Blueprint



BP_qty()




##Initilize Resource dictionaries        
# Type and sub-type
Dict_Wood = dict (Agedwood = 0,
                  DarkWood = 0,
                  Ironwood = 0,
                  Lightwood = 0,
                  Softwood = 0,
                  Strongwood = 0,
                  Wetwood = 0)
Dict_Thatch = dict (Bark = 0,
                    Fronds = 0,
                    Reeds = 0,
                    Roots = 0,
                    Rushes = 0,
                    Twigs = 0)
Dict_Stone = dict (Coquina = 0,
                   Granite = 0,
                   Limestone = 0,
                   Marble = 0,
                   Sandstone = 0,
                   Slate = 0)
Dict_Fiber = dict (Bamboo = 0,
                   Cotton = 0,
                   Hemp = 0,
                   Jute = 0,
                   Seaweed = 0,
                   Silk = 0,
                   Straw = 0)
                   
# List of Resource types
# List of Dictonaries
Dict_Resources = [Dict_Wood, Dict_Thatch, Dict_Stone, Dict_Fiber]


# Get Player Inventory



#establish variety counter of each resources
wood_var=7
thatch_var=6
stone_var=6
fiber_var=7

def user_inv():
# get user inventory
## Hard Way - need to get the loop working
###Wood
    print("Wood")
    Dict_Wood ['Agedwood'] = int(input("How many Agedwood? ") or 0)
    Dict_Wood ['DarkWood'] = int(input("How many DarkWood? ") or 0)
    Dict_Wood ['Ironwood'] = int(input("How many Ironwood? ") or 0)
    Dict_Wood ['Lightwood'] = int(input("How many Lightwood? ") or 0)
    Dict_Wood ['Softwood'] = int(input("How many Softwood? ") or 0)
    Dict_Wood ['Strongwood'] = int(input("How many Strongwood? ") or 0)
    Dict_Wood ['Wetwood'] = int(input("How many Wetwood? ") or 0)
###Thatch
    print("Thatch")
    Dict_Thatch ['Bark'] = int(input("How many Bark? ") or 0)
    Dict_Thatch ['Fronds'] = int(input("How many Fronds? ") or 0)
    Dict_Thatch ['Reeds'] = int(input("How many Reeds? ") or 0)
    Dict_Thatch ['Roots'] = int(input("How many Roots? ") or 0)
    Dict_Thatch ['Rushes'] = int(input("How many Rushes? ") or 0)
    Dict_Thatch ['Twigs'] = int(input("How many Twigs? ") or 0)
###Stone
    print("Stone")
    Dict_Stone ['Coquina'] = int(input("How many Coquina? ") or 0)
    Dict_Stone ['Granite'] = int(input("How many Granite? ") or 0)
    Dict_Stone ['Limestone'] = int(input("How many Limestone? ") or 0)
    Dict_Stone ['Marble'] = int(input("How many Marble? ") or 0)
    Dict_Stone ['Sandstone'] = int(input("How many Sandstone? ") or 0)
    Dict_Stone ['Slate'] = int(input("How many Slate? ") or 0)
###Fiber
    print("Fiber")
    Dict_Fiber ['Bamboo'] = int(input("How many Bamboo? ") or 0)
    Dict_Fiber ['Cotton'] = int(input("How many Cotton? ") or 0)
    Dict_Fiber ['Hemp'] = int(input("How many Hemp? ") or 0)
    Dict_Fiber ['Jute'] = int(input("How many Jute? ") or 0)
    Dict_Fiber ['Seaweed'] = int(input("How many Seaweed? ") or 0)
    Dict_Fiber ['Silk'] = int(input("How many Silk? ") or 0)
    Dict_Fiber ['Straw'] = int(input("How many Straw? ") or 0)
    print(f'You have the following inventory: ', Dict_Resources)
    return




user_inv()




Dict_Resources


# Get Missing Resources



## make temp dictonaries to prevent loss of original values
## help from https://stackoverflow.com/questions/5010536/python-perform-an-operation-on-each-dictionary-value

Dict_Wood_temp = Dict_Wood.copy()    
Dict_Thatch_temp = Dict_Thatch.copy()
Dict_Stone_temp = Dict_Stone.copy()
Dict_Fiber_temp = Dict_Fiber.copy()
Dict_Wood_temp.update((k, v-BP_wood) for k, v in Dict_Wood_temp.items())
Dict_Thatch_temp.update((k, v-BP_thatch) for k, v in Dict_Thatch_temp.items())
Dict_Stone_temp.update((k, v-BP_stone) for k, v in Dict_Stone_temp.items())
Dict_Fiber_temp.update((k, v-BP_fiber) for k, v in Dict_Fiber_temp.items())
#Dict_Temp_inv = Dict_Resources.copy() if needed




#helped by https://stackoverflow.com/questions/44664247/python-dictionary-how-to-get-all-keys-with-specific-values
need_list_wood = [k for k,v in Dict_Wood_temp.items() if float(v) < 0]
need_list_thatch = [k for k,v in Dict_Thatch_temp.items() if float(v) < 0]
need_list_stone = [k for k,v in Dict_Stone_temp.items() if float(v) < 0]
need_list_fiber = [k for k,v in Dict_Fiber_temp.items() if float(v) < 0]




need_list = need_list_wood + need_list_thatch + need_list_stone + need_list_fiber
need_list




## Wood
if wood_var-len(need_list_wood) < quality:
    Dict_Wood_temp.update((k, v-BP_wood) for k, v in Dict_Wood_temp.items())
    print(f'You have {wood_var-len(need_list_wood)} wood but require {quality}.')
else:
    print(f'You have {wood_var-len(need_list_wood)} wood and require only {quality}. You have enough wood! NICE!')
    need_list_wood = " None"




# Thatch
if thatch_var-len(need_list_thatch) < quality:
    Dict_Thatch_temp.update((k, v-BP_thatch) for k, v in Dict_Thatch_temp.items())
    print(f'You have {thatch_var-len(need_list_thatch)} thatch but require {quality}.')
else:
    print(f'You have {thatch_var-len(need_list_thatch)} thatch and require only {quality}. You have enough thatch! NICE!')
    need_list_thatch = " None"





# Stone
if stone_var-len(need_list_stone) < quality:
    Dict_Stone_temp.update((k, v-BP_stone) for k, v in Dict_Stone_temp.items())
    print(f'You have {stone_var-len(need_list_stone)} stone but require {quality}.')
else:
    print(f'You have {stone_var-len(need_list_stone)} stone and require only {quality}. You have enough stone! NICE!')
    need_list_stone = " None"




# Fiber
if fiber_var-len(need_list_fiber) < quality:
    Dict_Fiber_temp.update((k, v-BP_fiber) for k, v in Dict_Fiber_temp.items())
    print(f'You have {fiber_var-len(need_list_fiber)} fiber but require {quality}.')
else:
    print(f'You have {fiber_var-len(need_list_fiber)} fiber and require only {quality}. You have enough fiber! NICE!')
    need_list_fiber = " None"





### Retired this for the below text. If brough back you need to remove the assignment of none in the above 4 lines of code
## Create resource counters for closest grid assigments
#wood_ctr = quality - (wood_var-len(need_list_wood))
#thatch_ctr = quality - (thatch_var-len(need_list_thatch))
#stone_ctr = quality - (stone_var-len(need_list_stone))
#fiber_ctr = quality - (fiber_var-len(need_list_fiber))
#print(f'You need {wood_ctr} types of wood, {thatch_ctr} types of thatch, {stone_ctr} types of stone, and {fiber_ctr} types of fiber')





print(f'Options are:\n Wood:{need_list_wood}\n Thatch:{need_list_thatch}\n Stone:{need_list_stone}\n Fiber:{need_list_fiber}')


# Create resource refereance dataframe




myFile_tp=myFile2.transpose() # not current option being used
# or use myFile2 for vertical arangment, Right now using myFile2


# Create map grid




## Pandas array with labels
##15x15 map representing the server grid in the Atlas Game

atlas_map_bool_mask_init = np.zeros([15,15],dtype=int)
top = [x for x in 'ABCDEFGHIJKLMNO']
side = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
atlas_map_df = pd.DataFrame(atlas_map_bool_mask_init, index=side, columns=top)
atlas_map_df


# Update the grid with resource locations




#function should also get closest before exiting
#Need to input resource from need_list_xxxx
#Help from https://stackoverflow.com/questions/35758620/iterating-over-each-element-in-pandas-dataframe
resource = input('Which resource? ')
def resource_update(resource):
    global atlas_map_df
    global temp_row
    temp_row =[]
    for index, row in myFile2.iterrows():
        global value
        value = row[resource]
        if len(value)> 1:
            temp_row.append(row[resource])
            temp_grid = value
            temp_grid_lat = temp_grid[0]
            temp_grid_long = int(temp_grid[1:3])
            atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)
        else:
            break
    return
resource_update(resource)





atlas_map_df





counter_temp=1
length_temp = len(temp_row)
temp_row_length_list = [1]
while counter_temp < length_temp:
#    print(test_df.loc[counter_loc,'X']) # for verification of output
    counter_temp+=1
    temp_row_length_list.append(counter_temp)
#temp_row_length_list # for conformation of list
#length_temp





top = ['Grid']
side = temp_row_length_list
test_df = pd.DataFrame(temp_row, index=side, columns=top)
test_df


# Find Closest locations for the needed resources




counter_loc=1
length = len(test_df)
length_list = [1]
while counter_loc < length:
#    print(test_df.loc[counter_loc,'X']) # for verification of output
    counter_loc+=1
    length_list.append(counter_loc)
# lenght_list # for conformation of list







side = length_list
#side could be the 'length' variable below
test_df = pd.DataFrame(temp_row, index=side, columns=top)
letter = test_df['Grid'].astype(str).str[0]
test_df['X'] = letter.str.upper()
test_df['Y'] = test_df['Grid'].astype(str).str[1:3]
test_df











# Set start point
atlas_map_df.loc[player_loc_long,player_loc_lat] = int(2)
atlas_map_df
#see that N11 was turned to 2 for home location "starting point", using 2 for easyily finding home in DF





#update closest resource tiles for each resource type needed





#not required for implementation, here for error checking
#is it a valid destination?
def valid_dest (X,Y):
    if atlas_map_df.loc[player_loc_long,player_loc_lat]-atlas_map_df.loc[Y,X] == 1:
        return True #print(f'{X}{Y} is a valid destination!')
    else:
        return False #print(f'{X}{Y} is NOT a valid destination!')





#valid_dest('B',5) # for testing
valid_dest(test_df.loc[1,'X'],int(test_df.loc[1,'Y']))





valid_dest('G',1)





##get the distance for a grid from the player location
#need the input to iterate through each resource type in Dict_xxxxx and store the X & Y for the shortest distance.
#set up short_1, short_2, etc for short_x where x = the (quality-(stone_var-len(need_list_stone)))
#or maybe short_list
# max x is 6
#short
#short_list=[]

def dist_chk(ind):
#    global short_list
    global distance, x_dist, y_dist
    x_dist = abs((ord(test_df.iloc[ind]['X'])-64)-player_x)
    if x_dist > 7:             # this accounts for east west wrap around ability with map
        x_dist = 15-x_dist
    y_dist = abs(int(test_df.iloc[ind]['Y']) - player_y)
    if y_dist > 7:             # this accounts for north south wrap around ability with map
        y_dist = 15-y_dist
    distance = x_dist+y_dist
    return distance


# Find shortest distance to resource




#for res in wood_list:
    





## Pandas array with labels
##15x15 map representing the server grid in the Atlas Game

atlas_map_bool_mask_init = np.zeros([15,15],dtype=int)
top = [x for x in 'ABCDEFGHIJKLMNO']
side = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
atlas_map_df_best = pd.DataFrame(atlas_map_bool_mask_init, index=side, columns=top)
atlas_map_df_best.loc[player_loc_long,player_loc_lat] = int(2)





def closest_loc():
    max_dist = 16
    trip = max_dist
    ind=0
    count = len(test_df)
    global best
    best=[]
    for x in range(count):
        dist_chk(ind)
        ind+=1
        if distance<trip:
            trip=distance
            best = ind
        else:
            pass
    return test_df.iloc[(best-1)]['Grid'] # closest grid for the resource type queried
atlas_map_df_best.loc[int(test_df.iloc[(best-1)]['Y']),test_df.iloc[(best-1)]['X']] = int(1)





print(f'{closest_loc()} is the closest location for {resource}')





atlas_map_df_best




"""
print('fin')


# ## Future Actions
# 
# For follow on projects:<br>
#     Add wind variable to account for fastest way based on current wind condidtions<br>
#     Add GUI support with tkinter, Django, or wooey/gooey<br>
#     Trip feature, allow user to specify the start and end point<br>
#     Add other resource options
#     Put all needed resources on best map and give a recommended path

# ## __ Working area __
# The below code is testing and version control before putting into the main project section above.









for mat_type in need_list_wood:
#for mat_type in range(len(need_list_wood)):
    resource_update(mat_type)
    closest_loc()
    atlas_map_df_best.loc[int(test_df.iloc[(best-1)]['Y']),test_df.iloc[(best-1)]['X']] = int(1)




def temp_resource:
for index, row in myFile2.iterrows():
    value = row['Agedwood']
    if len(value)> 1:
        temp_row.append()(row['Agedwood'])
    else:
        break




counter_loc=1
length = len(test_df)
while counter_loc < length:
#    print(test_df.loc[counter_loc,'X']) # for verification of output
    counter_loc+=1





counter_loc=1
length = len(test_df)
length_list = [1]
while counter_loc < length:
#    print(test_df.loc[counter_loc,'X']) # for verification of output
    counter_loc+=1
    length_list.append(counter_loc)
# lenght_list # for conformation of list






max_dist = 16
trip = max_dist
ind=0
count = len(test_df)
best=[]
for x in range(count):
    dist_chk(ind)
    ind+=1
    if distance<trip:
        trip=distance
        best = ind
    else:
        pass    





trip





best





current = 16
count = len(test_df)
for row,index in test_df.iterrows():
#    print(index, row)
    ind=0
    dist_chk(ind)
    ind+=1
    if count >= 0:
        pass
    short_list=test_df.iloc[ind]['Grid'] #only works if you need 1 resource needed
    current = distance
    ind+=1





current = 16
count = len(test_df)
ind=0
for row,index in test_df.iterrows():
#    print(index, row)
    dist_chk(ind)
    current=distance





current





short_list
#short_list





for X, Y in atlas_map_df.iteritems():
    valid_dest(X,Y)
    dist_chk(***)





test_df = pd.DataFrame(temp_row, index=side, columns=top)
counter_loc=1
length = len(test_df)
length_list = [1]
while counter_loc < length:
#    print(test_df.loc[counter_loc,'X']) # for verification of output
    counter_loc+=1
    length_list.append(counter_loc)





side = length_list
#side could be the 'length' variable below
letter = test_df['Grid'].astype(str).str[0]
test_df['X'] = letter.str.upper()
test_df['Y'] = test_df['Grid'].astype(str).str[1:3]
test_df





##help from https://stackoverflow.com/questions/20303323/distance-calculation-between-rows-in-pandas-dataframe-using-a-distance-matrix
# a helper function to compute distance of two items
dist = lambda xs, ys: sum( DistMatrix[ x ][ y ] for ( x, y ) in zip( xs, ys ) )

# a second helper function to compute distances from a given item
xdist = lambda x: { idx: dist( x, y ) for (idx, y) in sample.iterrows( ) }

# the pairwise distance matrix
pd.DataFrame( { idx: xdist( x ) for ( idx, x ) in sample.iterrows( ) } )





#Only aged wood right now, Make into a function and call function in a loop with each resource called
#function should also get closest before exiting
#Help from https://stackoverflow.com/questions/35758620/iterating-over-each-element-in-pandas-dataframe
resource = 'Agedwood'
#quality = int(input("What type of Build Quality? "))
temp_row =[]
for index, row in myFile2.iterrows():
    global value
    value = row[resource]
    if len(value)> 1:
        temp_row.append(row[resource])
        temp_grid = value
        temp_grid_lat = temp_grid[0]
        temp_grid_long = int(temp_grid[1:3])
        atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)
    else:
        break
top = ['Grid']
#side needs to be adaptive with the number of values in the dataframe column
side = [1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53]
test_df = pd.DataFrame(temp_row, index=side, columns=top)
letter = test_df['Grid'].astype(str).str[0]
test_df['X'] = letter.str.lower()
test_df['Y'] = test_df['Grid'].astype(str).str[1:3]
test_df
##
x_dist = (ord(test_df.iloc[1]['X'])-96)-player_x
y_dist = int(test_df.iloc[1]['Y']) - player_y
distance = abs(x_dist)+abs(y_dist)





for index, row in myFile2.iterrows():
    global value
    value = row[resource]
    counter = 0
    if len(value)> 1:
        temp_row.append(row[resource])
        temp_grid = value
        temp_grid_lat = temp_grid[0]
        temp_grid_long = int(temp_grid[1:3])
        atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)
        counter ++1
    else:
        break





top = ['Grid']
#side needs to be adaptive with the number of values in the dataframe column
side = [1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53]
test_df = pd.DataFrame(temp_row, index=side, columns=top)





letter = test_df['Grid'].astype(str).str[0]
test_df['X'] = letter.str.lower()
test_df['Y'] = test_df['Grid'].astype(str).str[1:3]
test_df
####





##
x_dist = (ord(test_df.iloc[1]['X'])-96)-player_x
y_dist = int(test_df.iloc[1]['Y']) - player_y
distance = abs(x_dist)+abs(y_dist)
counter





x_dist = abs((ord(test_df.iloc[1]['X'])-64)-player_x)
if x_dist > 7:             # this accounts for east west wrap around ability with map
    x_dist = 15-x_dist
x_dist





y_dist = abs(int(test_df.iloc[1]['Y']) - player_y)
if y_dist > 7:             # this accounts for north south wrap around ability with map
    y_dist = 15-y_dist
y_dist




distance = x_dist+y_dist
distance



x_dist = abs((ord(test_df.iloc[1]['X'])-64)-player_x)
if x_dist > 7:             # this accounts for east west wrap around ability with map
    x_dist = 15-x_dist
y_dist = abs(int(test_df.iloc[1]['Y']) - player_y)
if y_dist > 7:             # this accounts for north south wrap around ability with map
    y_dist = 15-y_dist
distance = x_dist+y_dist





tryit = range(0,53)
tryit




atlas_map_df





def resource_update(resource):
    global atlas_map_df
    temp_row =[]
    for index, row in myFile2.iterrows():
        global value
        value = row[resource]
        if len(value)> 1:
            temp_row.append(row[resource])
            temp_grid = value
            temp_grid_lat = temp_grid[0]
            temp_grid_long = int(temp_grid[1:3])
            atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)
        else:
            break
    return





resource_update('Marble')





atlas_map_df





for word in need_list:
    temp_grid = myFile_tp[word:word] # temp_grid= myFile_tp['Agedwood':'Agedwood']
    temp_grid_list=temp_grid.values.tolist()
    temp_grid_lat = temp_grid[0]
    temp_grid_long = int(temp_grid[1:3])
    atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)





for col in need_list:
   myFile2[col] = myFile2[col].replace('', None)











temp_grid = myFile2['Agedwood']





#possible way
for word in need_list:
    temp_grid = myFile2['word']
    temp_grid_lat = temp_grid[0]
    temp_grid_long = int(temp_grid[1:3])
    atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)





temp_grid2= myFile_tp['Agedwood':'Agedwood']




temp_grid_list=temp_grid.values.tolist()




temp_grid2





go_to_list = []

for word in need_list:
    temp_grid = myFile_tp[word:word] # temp_grid= myFile_tp['Agedwood':'Agedwood']
    temp_grid_list=temp_grid.values.tolist()
    go_to_list.append(temp_grid_list)
 





go_to_list_wood = []

for word in need_list_wood:
    temp_grid = myFile_tp[word:word] # temp_grid= myFile_tp['Agedwood':'Agedwood']
    temp_grid_list=temp_grid.values.tolist()
    go_to_list_wood.append(temp_grid_list)
go_to_list_wood





#
#grid = [i for i in go_to_list_wood]
#grid_lat = grid[0]
#grid_long = grid[1:3]
#atlas_map_df.loc[grid_long,grid_lat] = int(1)





temp_grid





myFile_tp['DarkWood':'DarkWood']





#for grid in go_to_list:
#    if "" != grid:
#        temp_grid_lat = grid[0]
#        temp_grid_long = grid[1:3]
#        atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)





go_to_list





#Help from https://stackoverflow.com/questions/35758620/iterating-over-each-element-in-pandas-dataframe
temp_row =[]
for index, row in myFile2.iterrows():
    global value
    value = row['Agedwood']
    if len(value)> 1:
        temp_row.append(row['Agedwood'])
        temp_grid = value
        temp_grid_lat = temp_grid[0]
        temp_grid_long = int(temp_grid[1:3])
        atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)
    else:
        break
    
#    temp_grid = (row['Agedwood'])
#    temp_grid_lat = temp_grid[0]
#    temp_grid_long = int(temp_grid[1:3])
#    atlas_map_df.loc[temp_grid_long,temp_grid_lat] = int(1)





def temp_resource:
temp_row =[]
for index, row in myFile2.iterrows():
    value = row['Agedwood']
    if len(value)> 1:
        temp_row.append(row['Agedwood'])
    else:
        break





atlas_map_df





#inverting Y axis with <code> plt.gca().invert_yaxis() <code>





side = [1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,	33,	34,	35,	36,	37,	38,	39,	40,	41,	42,	43,	44,	45,	46,	47,	48,	49,	50,	51,	52,	53]
#side could be the 'length' variable below
test_df = pd.DataFrame(temp_row, index=side, columns=top)
letter = test_df['Grid'].astype(str).str[0]
test_df['X'] = letter.str.upper()
test_df['Y'] = test_df['Grid'].astype(str).str[1:3]
test_df





x_dist = (ord(test_df.iloc[1]['X'])-64)-player_x
y_dist = int(test_df.iloc[1]['Y']) - player_y
distance = abs(x_dist)+abs(y_dist)
distance






"""