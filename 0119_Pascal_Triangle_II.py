class Solution:
    def getRow(self, rowIndex: int):     
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1, 1]
        
        dp = [[]] * (rowIndex + 1)
        dp[0] = [1]
        dp[1] = [1, 1]

        for i in range(2, rowIndex + 1):
            temp = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(dp[i - 1][j - 1] + dp[i - 1][j])

            dp[i] = temp

        return dp[-1]
