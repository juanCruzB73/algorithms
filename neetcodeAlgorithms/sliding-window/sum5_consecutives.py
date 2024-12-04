def sum5_consecutives(nums:list[int])->int:
    total=sum(nums[:5])
    max_total=total
    for i in range(len(nums)-5):
        total-=nums[i]
        total+=nums[5+i]
        if(total>max_total):
            max_total=total
    return max_total


lis=[ 5, 7, 1, 4, 3, 6, 2, 9, 2 ]
result=sum5_consecutives(lis)
print(result)
