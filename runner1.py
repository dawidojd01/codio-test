__author__ = 'dawidojd01'
#To change this template use Tools | Templates.

Distance = 100
NameOfRunner = ""
SpeedOfRunner = 0
MStoMPH = 2.24
SpeedInMPH = 0
SpeedLimit = 20

NameOfRunner = input("Name Of Runner: ")
TimeTaken = float(input("Time Taken: "))

SpeedOfRunner = Distance / TimeTaken

SpeedInMPH = SpeedOfRunner * MStoMPH

print (NameOfRunner + " ran the 100M race in: 2" + str(round(SpeedInMPH)))