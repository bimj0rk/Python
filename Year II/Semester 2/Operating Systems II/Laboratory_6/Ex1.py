import random

class Factor(object):
    def __init__(self, aID, aName, aStatus, aTime):
        self.id = aID
        self.name = aName
        self.status = aStatus
        self.time = aTime
    
    def show(self):
        print("id: " + str(self.id) + ", name: " + str(self.name) +
              ", status: " + str(self.status) + ", time: " + str(self.time))

class Person(Factor):
    def __init__(self, aHabit, aLocation):
        self.disease = None
        self.habit = aHabit
        self.location = aLocation
    
    def move(self):
        return
    
    def getIn(self):
        return
    
    def getOut(self):
        return
    
    def use(self):
        return
    
class HomeAppliance(Factor):
    def __init__(self, aLocation, aEffectLevel):
        self.location = aLocation
        self.effectLevel = aEffectLevel

    def setStatus(self):
        return
    
class Environment(Factor):
    def __init__(self, aTemperature, aHumidity, aIllumination, aNoiseLevel):
        self.temperature = aTemperature
        self.humidity = aHumidity
        self.illumination = aIllumination
        self.noiseLevel = aNoiseLevel

    def getEnviromentalInfo(self):
        print("Temp: " + str(self.temperature) + ", humidity: " + str(self.humidity) + ", illumination: " 
              + str(self.illumination) + ", noise level: " + str(self.noiseLevel))

class Internal(Environment):
    def __init__(self, aSize):
        self.size = aSize
    
    def getEnvironmentFromApplianceEffect(self):
        return
    
class Weather(Environment):
    def __init__(self, aLevel):
        self.level = aLevel

    def setEffect(self):
        return

class VirtualSpace(object):
    def __init__(self, aSize, aLocation, aPersons, aAppliances, aEnvironment):
        self.factors = None
        self.size = aSize
        self.location = aLocation
        self.Persons = aPersons
        self.appliances = aAppliances
        self.environment = aEnvironment

    def show(self):
        print("Size: " + str(self.size) + ", location: " + str(self.location) + ", factors: " + str(self.factors))
        return
    
    def getEvent(self):
        return
    
class Reasoning(object):
    def __init__(self, aDBConnection, aRefSmartHome):
        self.dbConnection = aDBConnection
        self.refSmartHome = aRefSmartHome

    def getCases(self):
        return

    def doReasoning(self):
        return

    def caseMatching(self):
        return

    def getEnvironmentInfo(self):
        return self.refSmartHome.environment
    
class DBConnection(self):
    def __init__(self, aConnectionString):
        self.connectionString = aConnectionString

    def read(self):
        return
    
    def write(self):
        return
    
    def close(self):
        return