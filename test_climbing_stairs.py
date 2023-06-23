import unittest
import climbing_stairs

class TestClimbingStairs(unittest.TestCase):

    def test_climbStairs(self):
        self.assertEqual(climbing_stairs.Solution().climbStairs(3), 3)
        self.assertEqual(climbing_stairs.Solution().climbStairs(2), 2)

if __name__ == "__main__":
    unittest.main()