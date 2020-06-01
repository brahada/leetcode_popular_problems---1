class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)<n-1:
            return -1
        elif n==1:
            return 1
        else:
            t=[0]*(n+1)
            for i_,j_ in trust:
                t[i_]-=1
                t[j_]+=1
            for i,score in enumerate(t):
                if score==n-1:
                    return i
            return -1
            
