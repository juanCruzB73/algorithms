'''
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
'''
#OPTION 1 FUCKING GAY
class Solution:
    def groupAnagrams(self,strs: list[str])->list[list[str]]:
        my_hashes={}
        my_keys=[]
        for word in range(len(strs)):
            my_hash={}
            for letter in range(len(strs[word])):
                 my_hash[strs[word][letter]]=1+my_hash.get(strs[word][letter],0)
            my_key=list(my_hash.keys())
            my_key.sort()
            sorted_hash=str({i: my_hash[i] for i in my_key})
            if(len(my_keys)<1):
                my_keys.append(sorted_hash)
                my_hashes[sorted_hash]=[strs[word]]
            else:
                if(sorted_hash in my_keys):
                    print("wababaadd")
                    my_hashes[sorted_hash].append(strs[word])
                else:
                    my_keys.append(sorted_hash)
                    my_hashes[sorted_hash]=[strs[word]]
        result=list(my_hashes.values())
        return result


    #OPTION 2 
    def groupAnagrams2(self,strs: list[str])->list[list[str]]:
        my_hashes={}
        for word in strs:
            my_key=''.join(sorted(word))
            if(my_key in my_hashes):
                my_hashes[my_key].append(word)
            else:
                my_hashes[my_key]=[word]
        result=list(my_hashes.values())
        return result
strs = ["act","pots","tops","cat","stop","hat"]
result=None
result=Solution.groupAnagrams2(result,strs)
print(result)
