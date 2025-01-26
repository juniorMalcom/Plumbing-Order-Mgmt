# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:48:43 2025

@author: Nick
"""
#sgp supply order guide

#building specs (USER INPUT VARIABLE VALUES) ft
building_lenght = 100
building_width = 30
building_height = 45
#rooms bed/bath (?bd?ba)
bd1ba1 = 0
bd2ba2 = (8*3)
bd3ba3 = (4*3)
bd3ba2 = 0
bd4ba4 = 0
bd4ba3 = 0
handicaps_bathrooms = 3
#exclude handicapped showers from showers
showers = 4
#FOR TUB VALVES ONLY 
offset_right = 0
offset_left = 0
straight_valve = 0
shower_valve = 0
sides = 0


#building calculations
building_volume = (building_lenght * building_width * building_height)
building_rooms = (bd1ba1+bd2ba2+bd3ba3+bd3ba2+bd4ba4+bd4ba3)
bathrooms = ((bd1ba1)+(bd2ba2*2)+(bd3ba3*3)+(bd3ba2*2)+(bd4ba4*4)+(bd4ba3*3))
kitchens = (bd1ba1+bd2ba2+bd3ba3+bd3ba2+bd4ba4+bd4ba3)
washer_driers = (bd1ba1+bd2ba2+bd3ba3+bd3ba2+bd4ba4+bd4ba3)
water_heaters = (bd1ba1+bd2ba2+bd3ba3+bd3ba2+bd4ba4+bd4ba3)
total_showers = (handicaps_bathrooms + showers)
tub_valves = (offset_right + offset_left + straight_valve + shower_valve)


#MATERIALS NEEDED FOR TUB VALES
print ("Materials needed for tub valves:)
print ('brass adapters : ' + str((tub_valves * sides) - ((offset_right + offset_left + straight_valve) * 1)))
print ('copper adapter: ' + str(offset_right + offset_left + straight_valve))
print ('copper elbows: ' + str(((offset_right + offset_left) * 2) + straight_valve))
print ('1/2 crimp rings: ' + str(shower_valve))
print ('1/2 caps: ' + str(shower_valve))
print ('1/2 pex tube: ' + str(shower_valve) + 'inches')
print ('blue copper pipe: ' + str(((tub_valves - total_showers) * 4) + 'inches')
print ('red copper pipe: ' + str(((((offset_right + offset_left) * 2) + (straight_valve))) * 4 ))
       
if tub_valves >= 300:
 print ('pipe dope: 2')
else:
 print ('pipe dope: 1')

if (offset_right + offset_left + straight_valve) >= 200:
  print ('flux: 2')
else:
  print ('flux: 1')

if (tub_valves * sides) >=  1000
 print ('teflon tape: 15')
elif (tub_valves * sides) >750:
 print ('teflon tape: 10'       
elif (tub_valves * sides) >500:
 print ('teflon tape: 7')    
elif (tub_valves * sides) < 500:
 print ('teflon tape: 5')

if (offset_right + offset_left + straight_valve) >= 200:
 print ('fire gas: 2')
 print ('solder: 2')
else:
 print ('fire gas: 1')
 print ('solder: 1')
       


                                



# MATERIALS NEEDED FINAL FORMULAS
#Rough-In
fire_caulk=((bd1ba1*0.5)+(bd2ba2*0.75)+(bd3ba3*1)+(bd3ba2*0.85)+(bd4ba4*1.3)+(bd4ba3*1.15))
print('fire caulk: ' + str(fire_caulk))
nail_plates=((bd1ba1*3)+(bd2ba2*5)+(bd3ba3*8)+(bd3ba2*7)+(bd4ba4*10)+(bd4ba3*9))
stud_guards=((bd1ba1*5)+(bd2ba2*7)+(bd3ba3*10)+(bd3ba2*9)+(bd4ba4*12)+(bd4ba3*11))
print('nail plates: ' + str(nail_plates) + ' or ' + str(nail_plates/25) + ' boxes')
print('stud guards: ' + str(stud_guards) + ' or ' + str(stud_guards/50) + ' boxes')
tubs = (bathrooms - showers - handicaps_bathrooms)
print ('tubs: ' + str(tubs))
print ('showers: ' + str(showers))
print ('handicap showers: ' + str(handicaps_bathrooms))



#Finishings 
print ("toliets: " + str(bathrooms) )
print ('Bathroom Sinks: ' + str(bathrooms))
print ('tub valves: ' + str(bathrooms))
print ('shower heads: ' + str(bathrooms))
print ('tub drains: ' + str(bathrooms))
