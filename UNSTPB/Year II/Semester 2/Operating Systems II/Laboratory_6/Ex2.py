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
        self.Person = aPersons
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
    
    def determineDisease(self):
        diseasesNames = ["Anthrax", "Botulism", "Brucellosis", "Chikungunya", "Coronavirus", "Dengue", 
                         "Ebola","Haemorrhagic fevers", "Hepatitis", "HIV"]
        env = self.getEnvironmentInfo()
        dangerFactor = 0
        seve = "none"

        if env.temperature > 42 or env.temperature < -20 and env.noiseLevel > 80:
            dangerFactor = random.randint(5, 10)
        elif env.temperature > 38 or env.temperature < -15 and env.noiseLevel > 70:
            dangerFactor = random.randint(4, 9)
        elif env.temperature > 35 or env.temperature < -10 and env.noiseLevel > 70:
            dangerFactor = random.randint(3, 7)
        elif env.temperature > 32 and env.noiseLevel > 60:
            dangerFactor = random.randint(1, 4)
        else:
            dangerFactor = random.randint(0, 1)

        if dangerFactor > 8:
            seve = "emergency"
        elif dangerFactor > 6:
            seve = "warning"
        elif dangerFactor > 3:
            seve = "normal"
        elif dangerFactor > 0:
            seve = "low"

        if seve == "none":
            name = "healthy"
        else:
            name = random.choice(diseasesNames)

        dis = Disease(seve, name)
        return dis
    
        
    def assignDiseases(self):
        pers = self.refSmartHome.aPersons
        for Person in pers:
        Person.disease = self.determineDisease()
    
class Disease(object):
    def __init__(self, aSeverity, aName):
        self.name = aName
        self.severity = aSeverity    
    
class DBConnection(self):
    def __init__(self, aConnectionString):
        self.connectionString = aConnectionString

    def read(self):
        return
    
    def write(self):
        return
    
    def close(self):
        return

def main():
    envTemperature = random.randint(20, 45)
    noiseLevel = random.randint(30, 80)
    env1 = Environment(envTemperature, 19, "good", noiseLevel)
    p1 = Person("eating", "Bucuresti")
    p2 = Person("breathing", "Bucuresti")
    p3 = Person("existing", "Bucuresti")
    p4 = Person("existing", "Bucuresti")
    p5 = Person("existing", "Bucuresti")
    p6 = Person("existing", "Bucuresti")
    p7 = Person("existing", "Bucuresti")
    p8 = Person("existing", "Bucuresti")
    p9 = Person("existing", "Bucuresti")
    p10 = Person("existing", "Bucuresti")

    homeapp = HomeAppliance("Bucuresti", 100)
    vectpers = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]



    vSpace = VirtualSpace(10, "Bucuresti", vectpers, homeapp, env1)
    DBCon = DBConnection("Connect1")

    reasoning1 = Reasoning(dbcon, vspace)

    reasoning1.assignDiseases()
    print("in Bucuresti " + " with the temperature " + str(envTemperature) + " degrees and the noise level " + str(noiseLevel) + " we have the following patients:")

    print("Person 1 has " + p1.disease.name + " with " + p1.disease.severity + " severity ")
    print("Person 2 has " + p2.disease.name + " with " + p2.disease.severity + " severity ")
    print("Person 3 has " + p3.disease.name + " with " + p3.disease.severity + " severity ")
    print("Person 4 has " + p4.disease.name + " with " + p4.disease.severity + " severity ")
    print("Person 5 has " + p5.disease.name + " with " + p5.disease.severity + " severity ")
    print("Person 6 has " + p6.disease.name + " with " + p6.disease.severity + " severity ")
    print("Person 7 has " + p7.disease.name + " with " + p7.disease.severity + " severity ")
    print("Person 8 has " + p8.disease.name + " with " + p8.disease.severity + " severity ")
    print("Person 9 has " + p9.disease.name + " with " + p9.disease.severity + " severity ")
    print("Person 10 has " + p10.disease.name + " with " + p10.disease.severity + " severity ")

if __name__ == "__main__":
    main()