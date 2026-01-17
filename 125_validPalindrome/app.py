class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = ''.join([char for char in s if char.isalnum()])
        # list comprehension 'char for char in s' iterates through each character and only includes those that are alphanumeric
        # join then combines all obtained characters

        res = res.lower()

        end = len(res)
        if end == 0 or end == 1:
            # Return true if empty string or length of 1 is result
            return True

        x = 0
        end -= 1
        while x <= end:
            if res[x] != res[end]:
                return False
            x += 1
            end -= 1
        return True
