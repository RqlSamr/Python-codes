# Imagine that you develop a piece of software for an automatic weather station. 
# The device records the air temperature on an hourly basis and does it throughout the month. 
# This gives you a total of 24 × 31 = 744 values. Let's try to design a list capable of storing all these results.

# First, you have to decide which data type would be adequate for this application. 
# In this case, a float would be best, since this thermometer is able to measure the temperature with an accuracy of 0.1 C.
# Then you take an arbitrary decision that the rows will record the readings every hour on the hour (so the row will have 24 elements) 
# and each of the rows will be assigned to one day of the month (let's assume that each month has 31 days, so you need 31 rows).


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#
highest = -100.0
total = 0.0
hotDays = 0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)


for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")