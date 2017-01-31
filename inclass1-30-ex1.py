#List of cities and N/W coordinates
#Sublist structure: [city_name, degreesLat, N/S
#                               degressLong, E/W]


cities=[['Philadelphia',39,'N',75,'W'],
        ['Boston',42,'N',71,'W'],
        ['New York City',40,'N',74,'W']];

def find_most_north(x):
    if len(x) == 0:
        raise Exception("No cities found")
    else:
        #assume first city most north
        maxNorth = x[0][1]
        maxNorthIndex = 0;
        for i in range(1,len(x)):
            if(x[i][1] > maxNorth):
                #I found a new max
                maxNorth = x[i][1];
                maxNorthIndex = i;
        return x[maxNorthIndex][0];

print(find_most_north([]))
print(find_most_north(cities));

