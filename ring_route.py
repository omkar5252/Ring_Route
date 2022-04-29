('''
A City Bus is a Ring Route Bus which runs in circular fashion.That is, Bus once
starts at the Source Bus Stop, halts at each Bus Stop in its Route and at the
end it reaches the Source Bus Stop again.

If there are n  number of Stops and if the bus starts at Bus Stop 1, then after
nth Bus Stop, the next stop in the Route will be Bus Stop number 1 always.
If there are n stops, there will be n paths.One path connects two stops. 
Distances (in meters) for all paths in Ring Route is given in array Path[] 
as given below:

Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]

Fare is determined based on the distance covered from source to destination
stop as  Distance between Input Source and Destination Stops can be measured 
by looking at values in array Path[] and fare can be calculated as per following
criteria:

If d =1000 metres, then fare=5 INR
(When calculating fare for others, the calculated fare containing any fraction
 value should be ceiled. For example, for distance 900n when fare initially 
calculated is 4.5 which must be ceiled to 5)
Path is circular in function. Value at each index indicates distance till 
current stop from the previous one. And each index position can be mapped with 
values at same index in BusStops [] array, which is a string array holding 
abbreviation of names for all stops as-
“THANERAILWAYSTN” = ”TH”, “GAONDEVI” = “GA”, “ICEFACTROY” = “IC”, 
“HARINIWASCIRCLE” = “HA”, “TEENHATHNAKA” = “TE”, “LUISWADI” = “LU”, 
“NITINCOMPANYJUNCTION” = “NI”, “CADBURRYJUNCTION” = “CA”

Given, n=8, where n is number of total BusStops.
BusStops = [ “TH”, ”GA”, ”IC”, ”HA”, ”TE”, ”LU”, ”NI”,”CA” ]

Write a code with function getFare(String Source, String Destination) which 
take Input as source and destination stops(in the format containing first two 
characters of the Name of the Bus Stop) and calculate and return travel fare.

Example 1:
Input Values
ca
Ca

Output Values
INVALID OUTPUT

''')


import math
def getfare(source,destination):
    Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    BusStops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI","CA"]

    start = BusStops.index(source)
    stop = BusStops.index(destination)

    start += 1
    stop += 1

    fare = 0
    dist = 0

    if (start == stop):
        return ("Invalid Input")
    
    elif (start < stop):
        for i in range(start,stop):
            dist += Path[i]
    
    elif (start > stop):
        for i in range(start+1,len(Path)):
            start = 0
        dist += Path[start]
    print("Distance:",dist)

    fare = (dist/1000)*5
    return math.ceil(fare)

source = input("Enter a source:")
destination = input("Enter a destination:")
result = getfare(source,destination)
print("Final Fare:",result)

