# PROBLEM STATEMENT - Surrounded Regions
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

def solve1(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        if m <= 1:
            return
        n = len(board[0]) 
        flag = [[-1 for i in range(n)] for j in range(m)]

        def bfs(i, j):
            if i - 1 > 0 and board[i - 1][j] == 'O' and flag[i - 1][j] == -1:
                flag[i - 1][j] = 1
                bfs(i - 1, j)

            if i + 1 < m and board[i + 1][j] == 'O' and flag[i + 1][j] == -1:
                flag[i + 1][j] = 1
                bfs(i + 1, j)

            if j - 1 > 0 and board[i][j - 1] == 'O' and flag[i][j - 1] == -1:
                flag[i][j - 1] = 1
                bfs(i, j - 1)

            if j + 1 < n and board[i][j + 1] == 'O' and flag[i][j + 1] == -1:
                flag[i][j + 1] = 1
                bfs(i, j + 1)

            return 

        for k in (0, m - 1):
            for l in range(n):
                if board[k][l] == 'O' and flag[k][l] == -1:
                    flag[k][l] = 1
                    bfs(k, l)

        for l in (0, n - 1):
            for k in range(m):
                if board[k][l] == 'O' and flag[k][l] == -1:
                    flag[k][l] = 1
                    bfs(k, l)

        for k in range(m):
            for l in range(n):
                if board[k][l] == 'O' and flag[k][l] == -1:
                    board[k][l] = 'X'

        return