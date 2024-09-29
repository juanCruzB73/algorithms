'''
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.
'''

class Solution:
    def groupAnagrams(self,strs: list[str])->list[list[str]]:
            my_hashes=[]
            for word in range(len(strs)):
                my_hash={}
                for letter in range(len(strs[word])):
                    my_hash[strs[word][letter]]=1+my_hash.get(strs[word][letter],0)
                my_keys=list(my_hash.keys())
                my_keys.sort()
                sorted_hash=str({i: my_hash[i] for i in my_keys})
                for i in my_hashes:
                    if(sorted_hash in i):
                        i.append(strs[word])
                    else:
                        my_hashes.append([strs[word]])
                return my_hashes        
strs = ["act","pots","tops","cat","stop","hat"]
result=None
result=Solution.groupAnagrams(result,strs)
print(result)