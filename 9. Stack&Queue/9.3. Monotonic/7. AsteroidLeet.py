class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                last = stack[-1]
                if last == -i:
                    stack.pop()
                    break
                elif last < -i:
                    stack.pop()
                    continue
                elif last > -i:
                    break
            else:
                stack.append(i)
        return stack

# Link: https://leetcode.com/problems/asteroid-collision/
