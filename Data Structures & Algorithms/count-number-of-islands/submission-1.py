class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        # super simple, coding the iterative bfs is just tricky since have to check up, down, left, and right
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(i,j):
            q = collections.deque()
            visited.add((i,j))
            q.append((i,j))

            while q:
                # visit the vertice
                r, c = q.popleft()

                # append its neighbors that are set to "1" and are within the grid and haven't been visited!
                directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

                # we are checkign all directions here, need to make sure we have offsets as well
                for x, y in directions:
                    if (x + r) in range(rows) and (y + c) in range(cols) and grid[x + r][y + c] == "1" and (x + r, y + c) not in visited:
                        q.append((x + r, y + c))
                        visited.add((x + r, y + c))


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1

        return islands