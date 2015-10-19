__author__ = 'kdougla01'
#To change this template use Tools | Templates.

Distance = 100
#UnitOfDistance = "Meters"
NameOfRunner = ""
SpeedOfRunner = 0
#UnitOfSpeed = "MPH"
MStoMPH = 2.24
SpeedInMPH = 0
SpeedLimit = 20

NameOfRunner = input("Name of Runner: ")
TimeTaken = float(input("Time Taken: "))

SpeedOfRunner = Distance / TimeTaken

SpeedInMPH = SpeedOfRunner * MStoMPH

print (NameOfRunner + " ran the 100M race in: " + str(round(SpeedInMPH,2)))