from LAFitness import LAFitness
from Member import Member
from datetime import datetime


if __name__ == "__main__":

    # load from config file...

    # parameters
    monthlyFee = 25
    initFee = 25

    # main
    laFitness = LAFitness(monthlyFee, initFee)


    LDai= Member("Dai Lian", datetime(2016,12,15))
    LDai.pay(150)
    LDai.pay(150)

    KHuang = Member("Huang Kun", datetime(2017,5,13))
    KHuang.pay(75)

    JWang = Member("Wang Jinghao", datetime(2017,7,13))
    JWang.pay(150)

    laFitness.addMember(LDai)
    laFitness.addMember(KHuang)
    laFitness.addMember(JWang)

    laFitness.showAllStatics()
