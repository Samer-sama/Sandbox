import unittest
import climbing_stairs

class TestClimbingStairs(unittest.TestCase):

    def test_climbStairs(self):
        self.assertEqual(climbing_stairs.Solution().climbStairs(1), 1)
        self.assertEqual(climbing_stairs.Solution().climbStairs(2), 2)
        self.assertEqual(climbing_stairs.Solution().climbStairs(3), 3)
        self.assertEqual(climbing_stairs.Solution().climbStairs(4), 5)
        self.assertEqual(climbing_stairs.Solution().climbStairs(5), 8)
        self.assertEqual(climbing_stairs.Solution().climbStairs(6), 13)
        self.assertEqual(climbing_stairs.Solution().climbStairs(7), 21)
        self.assertEqual(climbing_stairs.Solution().climbStairs(8), 34)
        self.assertEqual(climbing_stairs.Solution().climbStairs(9), 55)
        self.assertEqual(climbing_stairs.Solution().climbStairs(10), 89)
        self.assertEqual(climbing_stairs.Solution().climbStairs(11), 144)
        self.assertEqual(climbing_stairs.Solution().climbStairs(12), 233)
        self.assertEqual(climbing_stairs.Solution().climbStairs(13), 377)
        self.assertEqual(climbing_stairs.Solution().climbStairs(14), 610)
        self.assertEqual(climbing_stairs.Solution().climbStairs(15), 987)
        self.assertEqual(climbing_stairs.Solution().climbStairs(16), 1597)
        self.assertEqual(climbing_stairs.Solution().climbStairs(17), 2584)
        self.assertEqual(climbing_stairs.Solution().climbStairs(18), 4181)
        self.assertEqual(climbing_stairs.Solution().climbStairs(19), 6765)
        self.assertEqual(climbing_stairs.Solution().climbStairs(20), 10946)
        self.assertEqual(climbing_stairs.Solution().climbStairs(21), 17711)
        self.assertEqual(climbing_stairs.Solution().climbStairs(22), 28657)
        self.assertEqual(climbing_stairs.Solution().climbStairs(23), 46368)
        self.assertEqual(climbing_stairs.Solution().climbStairs(24), 75025)
        self.assertEqual(climbing_stairs.Solution().climbStairs(25), 121393)
        self.assertEqual(climbing_stairs.Solution().climbStairs(26), 196418)
        self.assertEqual(climbing_stairs.Solution().climbStairs(27), 317811)
        self.assertEqual(climbing_stairs.Solution().climbStairs(28), 514229)
        self.assertEqual(climbing_stairs.Solution().climbStairs(29), 832040)
        self.assertEqual(climbing_stairs.Solution().climbStairs(30), 1346269)
        self.assertEqual(climbing_stairs.Solution().climbStairs(31), 2178309)
        self.assertEqual(climbing_stairs.Solution().climbStairs(32), 3524578)
        self.assertEqual(climbing_stairs.Solution().climbStairs(33), 5702887)
        self.assertEqual(climbing_stairs.Solution().climbStairs(34), 9227465)
        self.assertEqual(climbing_stairs.Solution().climbStairs(35), 14930352)
        # WARNING: This will take too long
        """ 
        self.assertEqual(climbing_stairs.Solution().climbStairs(36), 24157817)
        self.assertEqual(climbing_stairs.Solution().climbStairs(37), 39088169)
        self.assertEqual(climbing_stairs.Solution().climbStairs(38), 63245986)
        self.assertEqual(climbing_stairs.Solution().climbStairs(39), 102334155)
        self.assertEqual(climbing_stairs.Solution().climbStairs(40), 165580141)
        self.assertEqual(climbing_stairs.Solution().climbStairs(41), 267914296)
        self.assertEqual(climbing_stairs.Solution().climbStairs(42), 433494437)
        self.assertEqual(climbing_stairs.Solution().climbStairs(43), 701408733)
        self.assertEqual(climbing_stairs.Solution().climbStairs(44), 1134903170)
        self.assertEqual(climbing_stairs.Solution().climbStairs(45), 1836311903) 
        """

if __name__ == "__main__":
    unittest.main()