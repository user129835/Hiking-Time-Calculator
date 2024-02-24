import os

########################################
#  Hiking Distance To Time Calculator  #
########################################


# Note - This calculator does not include elevation, expects that hike is done on flat terrain

dist = float(input("\nEnter Distance (ex.: 6, 18.3): "))
print("* Average fast-paced speed for healthy adult is 6-8kmh\n* Average slow-paced speed for healthy adult is 3-5kmh")
# Implementation of speed is needed
speed = input("Enter speed (Rounded in kmh): ")

os.system('clear')

# Calculation of the distance to time in slow pace (person travels 1km in 0.5h)
calc1 = float(dist*0.477)
calc2 = (calc1/2)
# Calculation of the distance to time in fast pace (person travels 1km in 0.5h)
calc3 = float(dist*0.352)
calc4 = (calc3/2)

dist_length = len(str(dist)) + 5

print("###################")
print("#                 #")
print("#    User Info    #")
print("# Your Distance:  #")
print(f"# {dist:<16}#")
#print("# "+str(dist)+"km #")
print("# Your Speed:     #")
print(f"# {speed:<16}#")
#print("# "+str(speed)+"kmh #")
print("#                 #")
print("# --------------- #")
print("#                 #")
print("#   Hiking Time   #")
print("# Slow-Paced:     #")
print(f"# {calc2:<16.1f}#")
#print("# "+str(calc2)+"h #")
print("# Fast-Paced:     #")
print(f"# {calc4:<16.1f}#")
#print("# "+str(calc4)+"h #")
print("#                 #")
print("###################")




# Implementation for altitude coming soon...
# alt = 
