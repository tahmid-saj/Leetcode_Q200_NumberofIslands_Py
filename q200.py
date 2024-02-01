class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    self.bfs(grid, i, j)
        
        return res
    
    def dfs(self, grid, i, j):
        if grid[i][j] == "0": return
        grid[i][j] = "0"

        if i > 0: self.dfs(grid, i - 1, j)
        if i < len(grid) - 1: self.dfs(grid, i + 1, j)
        if j > 0: self.dfs(grid, i, j - 1)
        if j < len(grid[0]) - 1: self.dfs(grid, i, j + 1)
    
    def bfs(self, grid, i, j):
        queue = deque([(i, j)])
        while queue:
            i, j = queue.popleft()
            if grid[i][j] == "0": continue
            grid[i][j] = "0"

            if i > 0: queue.append((i - 1, j))
            if i < len(grid) - 1: queue.append((i + 1, j))
            if j > 0: queue.append((i, j - 1))
            if j < len(grid[0]) - 1: queue.append((i, j + 1))
