class Solution:
    def climbStairs(self, n: int) -> int:
        # TODO
        if n < 2:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(   )) # Missing inout 