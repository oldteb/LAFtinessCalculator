
class Member:

    def __init__(self, name, enrollTime):
        self.name = name
        self.enrollTime = enrollTime
        self.totalPayment = 0

    def getName(self):
        return self.name

    def getEnrollTime(self):
        return self.enrollTime

    def pay(self, payMount):
        self.totalPayment += payMount

    def getTotalPayment(self):
        return self.totalPayment
