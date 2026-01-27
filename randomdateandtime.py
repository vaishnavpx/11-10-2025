import random
import time

def getRandomDate(startDate, endDate):
    print("printing random date between ", startDate, "and ", endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%Y'

    startTime=time.mktime(time.strptime(startDate, dateFormat))
    endTime=time.mktime(time.strptime(endDate, dateFormat))

    randomTime=startTime+randomGenerator*(startTime-endTime)
    RandomDate=time.strftime(dateFormat, time.localtime(randomTime))
    return RandomDate

print("random date= ", getRandomDate("1/1/2026", "12/12/2018"))