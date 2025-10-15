import random
import time
def getRandomDate(s,e):
    print("RNADOM DATE BETWEEN",s,"AND",e)
    randomGenerator=random.Random()
    dateformat="%m/%d/%Y"
    st=time.mktime(time.strptime(s,dateformat))
    end=time.mktime(time.strptime(e,dateformat))
    randomTime = st + randomGenerator * (end - st)
    RandomDate=time.strftime(dateformat,time.localtime(randomTime))
    return rd

print(getRandomDate("01/01/2025","01/01/2026"))


#Random Date and Time
import random
import time

def getRandomDate(startDate, endDate):

    print("Printing random date between", startDate, "and", endDate)

    randomGenerator = random.random()

    dateFormat = '%m/%d/%Y'

#mktime() will convert date into above format; strptime() converts string to object

    Sdate = time.mktime(time.strptime(startDate, dateFormat))

    Edate = time.mktime(time.strptime(endDate, dateFormat))

#below calculate random date betn start to end

    randomTime = Sdate + randomGenerator * (Edate - Sdate)

#below to covert into local date format

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate

print("Random Date = ", getRandomDate("01/01/2025", "12/01/2025")) #mm/dd/yy