def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s
    
print(list_sum([5, 4, 3]))

def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))