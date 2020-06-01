class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)[2:]
        n,ans=len(binary),0
        for i in range(0,n):
            if binary[i]=="0":
                ans+=2**(n-1-i)
        return ans
        
