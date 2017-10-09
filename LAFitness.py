from datetime import datetime


class LAFitness:

    def __init__(self, membershipFee, initFee):
        self.members = []
        self.membershipFee = membershipFee
        self.initFee = initFee


    def addMember(self, newMember):
        self.members.append(newMember)


    def loadFromConfig(self):
        pass


    def showAllStatics(self):
        for member in self.members:
            self.showMemberStatistics(member)


    def showMemberStatistics(self, member):
        startDate = member.getEnrollTime()
        today = datetime.now()

        cycles = self.cycleCalculator(startDate, today)
        balance = (cycles + 1) * self.membershipFee
        balance += self.initFee
        balance -= member.getTotalPayment()

        print(member.getName() + ": $" + str(balance))


    def cycleCalculator(self, startDate, endDate):
        cycle = 0
        while(startDate <= endDate):
            if startDate.month == 12:
                startDate = startDate.replace(year=(startDate.year+1), month=1)
            else:
                startDate = startDate.replace(month=(startDate.month + 1))
            cycle += 1
        return cycle
