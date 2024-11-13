'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
'''

def is_alphanumeric(char):
        return ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9')
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r =0,len(s)-1
        condition=True
        while (l<r):
            print(l,r)
            if(not is_alphanumeric(s[l])):
                l+=1
                continue
            if(not is_alphanumeric(s[r])):
                r-=1
                continue
            print(s[l],s[r])
            if(s[l].lower()!=s[r].lower()):
                condition = False
                return condition
            else:
                l+=1
                r-=1
        return True
        