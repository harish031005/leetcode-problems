class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == ')' or grid[rows - 1][cols - 1] == '(':
            return False
        if (rows + cols - 1) % 2 != 0:
            return False
        memo = {}
        def search_path(row, col, balance):
            if grid[row][col] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
            if row == rows - 1 and col == cols - 1:
                return balance == 0
            state = (row, col, balance)
            if state in memo:
                return memo[state]
            valid_path = False
            if row + 1 < rows:
                valid_path = search_path(row + 1, col, balance)
            if not valid_path and col + 1 < cols:
                valid_path = search_path(row, col + 1, balance)
            memo[state] = valid_path
            return valid_path
        return search_path(0, 0, 0)