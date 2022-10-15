class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP = [amount+1]*(amount+1)
        DP[0]=0
        
        for a in range(1,amount+1):
            for c in coins:
                if a-c >= 0:
                    DP[a] = min(DP[a],1+DP[a-c])
                    
        return DP[amount] if DP[amount] != amount+1 else -1
