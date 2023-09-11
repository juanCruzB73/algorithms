import math
def binary_search(list,elemnto):
    low=0
    high=len(list)-1
    while low<=high:
        mid=math.floor((low+high)/2)
        guess=list[mid]
        if guess>elemnto:
            high=mid-1
        elif (guess<elemnto):
            low=mid+1
        else:
            return mid
    return None
list=[1,2,3,4]
print(binary_search(list,3))