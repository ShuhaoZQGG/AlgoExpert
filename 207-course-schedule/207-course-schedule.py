class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adjacency_list[crs].append(pre)
            
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            
            if adjacency_list[crs] == []:
                return True
            
            visited.add(crs)
            for pre in adjacency_list[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adjacency_list[crs] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True