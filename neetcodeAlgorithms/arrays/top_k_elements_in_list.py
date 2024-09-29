class Solution:
    #OPTION 1
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_hash={}
        result=[]
        for num in nums:
            if(num in my_hash):
                my_hash[num]=1+my_hash[num]
            else:
                my_hash[num]=1
        sorted_items = sorted(my_hash.items(), key=lambda item: item[1], reverse=True)
        print(sorted_items)
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
    #OPTION 2
    class Solution:
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            my_hash={}
            freq=[[]for i in range(len(nums)+1)]
            result=[]

            for num in nums:
                my_hash[num]=1+my_hash.get(num,0)

            for key,value in my_hash.items():
                freq[value].append(key)
            print(freq)
            for i in range(len(freq)-1,0,-1):
                for j in freq[i]:
                    result.append(j)
                    if(len(result)==k):
                        return result
nums = [1,2,2,3,3,3], k = 2