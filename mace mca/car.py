class engine():
    engineType = 'V8'
    def common(self):
        print("In common engine")
    def getEngine(self):
        print("In engine class", self.engineType)
        return(self.engineType)

class wheels():
    wheelType = 'rainTyres'
    def common(self):
        print("In common wheels")

    def getWheels(self):
        print("In wheels class", self.wheelType)
        return(self.wheelType)


class transmission():
    transmissionType = 'helical'
    def common(self):
        print("In common transmission")

    def getTransmission(self):
        print("In transmission class", self.transmissionType)
        return(self.transmissionType)

class car(engine, transmission, wheels):
    def getCar(self):
        self.engineType = engine.getEngine(self)
        self.wheelType = wheels.getWheels(self)
        self.transmissionType = transmission.getTransmission(self)
        return(self.engineType, self.wheelType, self.transmissionType)

car1 = car()
print(car1.getCar())
car1.common()

engine.getEngine(car1)