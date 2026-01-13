class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """

        count = 10
        # Need to check while count is greater than 0 and number of stones is greater than 0
        # starts from n = 19
        while count > 0:
            # stop if count exceeds n
            if n < count:
                # If current count is even that means it stopped on even and Alice loses and it's FALSE
                # If current count is odd that means it stopped on odd and Alice wins and it's TRUE
                return count % 2 == 1
            # Decrement total number of stones
            n -= count
            count -= 1
        # count has reached 0 so Alice cannot make any moves
        return False
