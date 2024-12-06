'''
Given a string s, find the length of the longest substring without 
duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:
'''
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        l,r=0,1
        my_hash={}
        max_length=0
        if len(s)==1:
            max_length=1
            return max_length
        while (r<(len(s))):
            if(len(my_hash)==0):
                my_hash[s[l]]=s[l]
            print("l ",l,"r ",r,my_hash)
            if(s[r] in my_hash):
                print(r," " ,s[r], " in ",my_hash)
                l+=1
                r=l+1
                my_hash={}
                my_hash[s[l]]=s[l]
                if(len(my_hash)>max_length):
                    max_length=len(my_hash)
                continue
            if(s[r] not in my_hash):
                my_hash[s[r]]=s[r]
                if(len(my_hash)>max_length):
                    max_length=len(my_hash)
                r+=1

        return max_length
    def lengthOfLongestSubstring2(s: str) -> int:
        l=0
        my_hash=set()
        max_length=0

        if len(s)==1:
            max_length=1
            return max_length
        
        for r in range(len(s)):
            while(s[r] in my_hash):
                my_hash.remove(s[l])
                l+=1
            my_hash.add(s[r])
        
            max_length=max(max_length,r-l+1)

        return max_length 

s = "zxyzxyz"#3
s6="abcabcbb"
s2 = "xxxx"#1
s3="pwwkew"#3
s4=""#0
s5=" "
max_length=Solution.lengthOfLongestSubstring2(s3)
print(max_length)