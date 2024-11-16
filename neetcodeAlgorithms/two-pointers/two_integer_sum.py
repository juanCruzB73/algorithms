'''
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2],
such that they add up to a given target number target and index1 < index2.
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1)O(1) additional space.
'''

def twoSum(numbers: list[int], target: int) -> list[int]:
    #index1 + index = target
    #index1 < index2
    #idex != index2
    result=[]
    i,j = 0,len(numbers)-1
    while (i<j):
        if(numbers[i]+numbers[j]==target):
            result=[i+1,j+1]
            return result
        if((numbers[i]+numbers[j])>target):
            j-=1
        else:
            i+=1
    return result

numbers = [1,2,3,4]
target = 3
test=twoSum(numbers,target)
print(test)

