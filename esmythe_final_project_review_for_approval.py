##Created by gramadin during Python Scripting course at SDSU as final Project Started 10 Nov 2019
##For questions or feedback email esmythe1518@SDSU.edu, Subject ATLAS Resource tracker and path generator
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#Get the build quality
#Build Quality influences number of different resource sub-types required

quality = 1 # initilize quality
def quality_check():
    
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
        
## prompt user to enter BP requirments
BP_fiber = type(int)
BP_stone = int
BP_thatch = int
BP_wood = int

def BP_qty():
    
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
            f'Please try again, values must be an integer between and integer'
    

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

##Get user_quantity inputs
#press x for exiting loop early ?

#Get Types required & Quantity for each type
####between --- is not working
#---
#Dict_Wood ['Agedwood'] = int(input("How many Agedwood? "))
#**
#for i in Dict_Wood:
#    int(input(Dict_Wood.update(i)("How many " Dict_Wood[i]" ? ")))
#**   
#---
def user_inv():
# get user inventory
## Hard Way - need to get teh loop working
###Wood
    print("Wood")
    Dict_Wood ['Agedwood'] = int(input("How many Agedwood? "))
    Dict_Wood ['DarkWood'] = int(input("How many DarkWood? "))
    Dict_Wood ['Ironwood'] = int(input("How many Ironwood? "))
    Dict_Wood ['Lightwood'] = int(input("How many Lightwood? "))
    Dict_Wood ['Softwood'] = int(input("How many Softwood? "))
    Dict_Wood ['Strongwood'] = int(input("How many Strongwood? "))
    Dict_Wood ['Wetwood'] = int(input("How many Wetwood? "))
###Thatch
    print("Thatch")
    Dict_Thatch ['Bark'] = int(input("How many Bark? "))
    Dict_Thatch ['Fronds'] = int(input("How many Fronds? "))
    Dict_Thatch ['Reeds'] = int(input("How many Reeds? "))
    Dict_Thatch ['Roots'] = int(input("How many Roots? "))
    Dict_Thatch ['Rushes'] = int(input("How many Rushes? "))
    Dict_Thatch ['Twigs'] = int(input("How many Twigs? "))
###Stone
    print("Stone")
    Dict_Stone ['Coquina'] = int(input("How many Coquina? "))
    Dict_Stone ['Granite'] = int(input("How many Granite? "))
    Dict_Stone ['Limestone'] = int(input("How many Limestone? "))
    Dict_Stone ['Marble'] = int(input("How many Marble? "))
    Dict_Stone ['Sandstone'] = int(input("How many Sandstone? "))
    Dict_Stone ['Slate'] = int(input("How many Slate? "))
###Fiber
    print("Fiber")
    Dict_Fiber ['Bamboo'] = int(input("How many Bamboo? "))
    Dict_Fiber ['Cotton'] = int(input("How many Cotton? "))
    Dict_Fiber ['Hemp'] = int(input("How many Hemp? "))
    Dict_Fiber ['Jute'] = int(input("How many Jute? "))
    Dict_Fiber ['Seaweed'] = int(input("How many Seaweed? "))
    Dict_Fiber ['Silk'] = int(input("How many Silk? "))
    Dict_Fiber ['Straw'] = int(input("How many Straw? "))
    return
import pprint
f'You have the following inventory:'
pprint.pprint(Dict_Resources)
###Get differnece between inventory and needed from BP
#User_quantities - BP_values (if neg then need more of that resourse)
#loop through resources for values greater than 0 for {quality} number of times or end of dictonary keys. add 1 to counter for each key with enough units
#If get to end then quality - counter = number of resourses needed

## Pandas array with labels
##15x15 map representing the server grid in the Atlas Game
import numpy as np
import pandas as pd

atlas_map_bool_mask_init = np.zeros([15,15],dtype=int)
top = [x for x in 'ABCDEFGHIJKLMNO']
side = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
atlas_map_df = pd.DataFrame(atlas_map_bool_mask_init, index=side, columns=top)



##Make network x map/graph
#atlas_map = nx.Graph()
#map_tiles = [A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14,E15,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,F13,F14,F15,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,G11,G12,G13,G14,G15,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,H13,H14,H15,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,I11,I12,I13,I14,I15,J1,J2,J3,J4,J5,J6,J7,J8,J9,J10,J11,J12,J13,J14,J15,K1,K2,K3,K4,K5,K6,K7,K8,K9,K10,K11,K12,K13,K14,K15,L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12,L13,L14,L15,M1,M2,M3,M4,M5,M6,M7,M8,M9,M10,M11,M12,M13,M14,M15,N1,N2,N3,N4,N5,N6,N7,N8,N9,N10,N11,N12,N13,N14,N15,O1,O2,O3,O4,O5,O6,O7,O8,O9,O10,O11,O12,O13,O14,O15]
#atlas_map.add_nodes_from(map_tiles)
##get array location by first value is top, next value is side

#Make player location Black
#Make destinations Blue
#make end Red
##
###Edges wrap from O to A and 1 to 15
##        
#Networkx for path to map location, example from https://pypi.org/project/networkx/
#>>> G = nx.Graph()
#>>> G.add_edge('A', 'B', weight=4)
#>>> G.add_edge('B', 'D', weight=2)
#>>> G.add_edge('A', 'C', weight=3)
#>>> G.add_edge('C', 'D', weight=4)
#>>> nx.shortest_path(G, 'A', 'D', weight='weight')
#['A', 'B', 'D']







#node of A-O and 1-15
#use boolean Mask to remove the nodes not required for user based on user input or program calculations
