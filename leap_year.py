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
testData = [1904, 1984, 2016, 1973]
testResults = [True, True, True, True]


for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")


		
