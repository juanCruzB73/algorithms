"""
MAKE A FUNCTION THAT WILL RETURN TRUE IF THERE IS AN ANAMGRAM
BETWEEN TWO VARIABLES.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hashS,hashT={},{}#hasmaps
        for i in range(len(s)):
            hashS[s[i]]=1+hashS.get(s[i],0)#gives  default value
            hashT[t[i]]=1+hashT.get(t[i],0)#gives  default value
        for j in hashS:
            if(hashS[j]!=hashT.get(j)):
                return False
        return True
dic1="anagram"
dic2="naramga"
result=None
print(Solution.isAnagram(result,dic1,dic2))