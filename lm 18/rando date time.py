import random
import time
def GetRandomDate(startDate, endDate):  
    print("printing random date between",startDate, "and" ,endDate)
    randomGenerator = random.random()
    dateFormat= '%m/%d/%Y'
    starttime = time.mktime(time.strptime(startDate,dateFormat))
    endtime = time.mktime(time.strptime(endDate,dateFormat))
    randomtime = starttime + randomGenerator * (endtime-starttime)
    randomdate = time.strftime(dateFormat,time.localtime(randomtime))
    return randomdate
print("Random Date= ",GetRandomDate("1/1/2016","12/12/2029"))