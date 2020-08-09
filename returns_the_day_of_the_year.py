# Your task is to write and test a function which takes three arguments 
# (a year, a month, and a day of the month) 
# and returns the corresponding day of the year, 
# or returns None if any of the arguments is invalid.

def isYearLeap(year):
    if year%4!=0 and year%400!=0:
        return False
    elif year%100!=0:
         return True
    else:
        return True
#
# put your code here
#
def daysInMonth(year, month):
    print("Numero de mes: ", month)
   
    months=[31,28,31,30,31,30, 31, 31,30,31,30,31]      
    if isYearLeap(year):
        if month==2:
            return int(29)
        else:
            month= month-1            
            return months[month]
    else:
        month= month-1        
        return months[month]
  

testYears = [1900, 2000, 2016, 1987]
testYResults = [True, True, True, True]
testMonths = [2, 2, 1, 11]
testMResults = [28, 29, 31, 30]

for i in range(len(testYears)):
	yr = testYears[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testYResults[i]:
		print("OK")
	else:
		print("Failed")

for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testMResults[i]:
		print("OK")
	else:
		print("Failed")
