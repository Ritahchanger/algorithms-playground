class Solution:
    def lengthOfLongestSubstring(s):        
        charSet=set()
        left=0
        res=0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                l+=1
            charSet.add(s[right])
            res=max(res,right-left+1)
        return res
 
listed=["a","b","c","a","b","f","g","a","b"]
result=lengthOfLongestSubstring(listed)
print(result)           
            
            