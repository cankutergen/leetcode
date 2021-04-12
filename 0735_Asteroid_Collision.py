class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        
        # astroid + ile stack'e at
        # değilse collision var mı
        # varsa durum ne
        while i < len(asteroids):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
            else:
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                
                if len(stack) <= 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
                elif stack[-1] == abs(asteroids[i]):
                    stack.pop()
            i += 1
                    
                
        return stack
