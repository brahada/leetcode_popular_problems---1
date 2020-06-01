class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(list)
        
        for x, y in trust:
            graph[x].append(y)
            indegree[y].append(x)
        candidate = None
        
        #The town judge will have indegree of n-1 and outdegree of 0
        for k, v in indegree.items():
            if len(v) == N-1 and len(graph[k]) == 0:
                return k
        return -1 
