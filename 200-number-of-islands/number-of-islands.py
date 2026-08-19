class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def fun(i, j):
            if (i < 0 or i >= len(grid) or
                j < 0 or j >= len(grid[0]) or
                grid[i][j] == "0"):
                return

            grid[i][j] = "0"

            fun(i + 1, j)
            fun(i - 1, j)
            fun(i, j + 1)
            fun(i, j - 1)

        c = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    c += 1
                    fun(i, j)

        return c