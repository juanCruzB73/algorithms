'''
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
'''

def threeSum(nums: list[int]) -> list[list[int]]:
    p1,p2=0,1
    sorted_numbers=sorted(nums)
    resutl=[]
    for i in range(len(sorted_numbers)):
        if(i>0 and sorted_numbers[i] == sorted_numbers[i-1]):
            continue
        j , k = i+1 , len(sorted_numbers)-1
        while(j<k):
            if(sorted_numbers[i]+sorted_numbers[j]+sorted_numbers[k]<0):
                j+=1
                continue
            if(sorted_numbers[i]+sorted_numbers[j]+sorted_numbers[k]>0):
                k-=1
                continue
            if([sorted_numbers[i],sorted_numbers[j],sorted_numbers[k]] in resutl):
                j+=1
                k-=1
                continue
            resutl.append([sorted_numbers[i],sorted_numbers[j],sorted_numbers[k]])
            j+=1
            k-=1
    return resutl

nums = [-1,0,1,2,-1,-4]
test=threeSum(nums)
print(test)