class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        if(len(c)==2):
            return True
        x0,y0=c[0]
        x1,y1=c[1]
        for i in range(2,len(c)):
            x,y=c[i]
            if (y1-y0)*(x-x0)!=(y-y0)*(x1-x0):
                return False
        return True
            
        
