# 735. Asteroid Collision

# compute array after collision.

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # use stack
        # time: O(n) space O(n)
        # runtime: 65ms
        # --
        if not asteroids: 
            return asteroids

        stack = [] # store positive asteroids.
        for ix in asteroids:

            if not stack or ix > 0: 
                stack.append(ix)

            elif ix < 0: # pop stack
                while stack and stack[-1] > 0:
                    if stack[-1] == -ix: # top = cur: break
                        stack.pop()
                        break

                    elif stack[-1] < -ix: # top < cur: cont.
                        stack.pop()
                        continue
                        
                    elif stack[-1] > -ix: # top > cur: break
                        break
                else:
                    stack.append(ix)
        return stack
        
        
        
        
        
        