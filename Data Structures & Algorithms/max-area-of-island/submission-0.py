class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        # same problem as number of islands, just returning area size now!
        # simple bfs
        # tricky part is working with 4 directions for the vertice children

        max_size = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(i,j,max_size):
            q = collections.deque()
            q.append((i,j))
            visited.add((i,j))

            cur_size = 0
            while q:
                # visit the vertice and add 1 to cur
                r, c = q.popleft()
                cur_size += 1
                max_size = max(max_size, cur_size)

                # add its children/neighbors
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for x_offset, y_offset in directions:
                    if ((x_offset + r) in range(rows) 
                    and (y_offset + c) in range(cols) 
                    and grid[x_offset + r][y_offset + c] == 1
                    and ((x_offset + r),(y_offset + c)) not in visited):
                        q.append((x_offset + r, y_offset + c))
                        visited.add((x_offset + r, y_offset + c))
            return max_size
                

        for i in range(rows):
            for j in range(cols):
                # if we find a unique island, do bfs on it (count the number of 1s on the bfs)
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_size = bfs(i,j,max_size)
    
        return max_size
        