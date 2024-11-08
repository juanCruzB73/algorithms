def longestConsecutive(nums: list[int]) -> int:
        my_hash=set(nums)
        max=0
        for num in nums:
            length=0
            current=num
            while(current in my_hash):
                length+=1
                if(length>max):
                     max=length
                current+=1
        return max
        

nums=[2,20,4,10,3,4,5]

print(longestConsecutive(nums))