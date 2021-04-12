class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = self.reverse(x)
        return reversed == x
    
    def reverse(self, x):
        negative = False
        if x < 0:
            x *= -1
            negative = True

        number = str(x)

        num = 0
        for i in range(len(number)):
            num += (10 ** i) * int(number[i])

        if num > 2**31 - 1:
            return 0

        if negative:
            num *= -1

        return num
