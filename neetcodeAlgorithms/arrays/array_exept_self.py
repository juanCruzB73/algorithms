#MY answer
def productExceptSelf(nums):
        hash_pre=[]
        hash_pos=[]
        result=[]
        aux=0
        for index in range(len(nums)-1,-1,-1):
            if(len(hash_pos)==0):
                hash_pos.append(1)
            else:
                hash_pos.append(nums[index+1]*hash_pos[aux])
                aux+=1
        aux=0
        for index in range(len(nums)):
            if(len(hash_pre)==0):
                hash_pre.append(1)
            else:
                hash_pre.append(nums[index-1]*hash_pre[aux])
                aux+=1
            result.append(hash_pre[index]*hash_pos[((len(nums)-1)-index)])
        return result

#neetcode answer
def productExceptSelf2(nums):
    result=[1]*len(nums)
    perfix=1
    for index in range(len(nums)):
        result[index]*=perfix
        perfix*=nums[index]
    postfix=1
    for index in range(len(nums)-1,-1,-1):
        result[index]*=postfix
        postfix*=nums[index]
    return result
          

nums=[1,2,3,4,5]
print(productExceptSelf(nums))
print(productExceptSelf2(nums))