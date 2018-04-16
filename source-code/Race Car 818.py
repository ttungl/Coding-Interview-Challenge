# 818. Race Car

# Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

# Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

# When you get an instruction "A", your car does the following: position += speed, speed *= 2.

# When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

# For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

# Now for some target position, say the length of the shortest sequence of instructions to get there.

# Example 1:
# Input: 
# target = 3
# Output: 2
# Explanation: 
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
# Example 2:
# Input: 
# target = 6
# Output: 5
# Explanation: 
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
 

# Note:

# 1 <= target <= 10000.

class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        # sol 1:
        # BFS
        # use queues to store results and visited to keep track of visited pairs.
        # runtime: 2973ms
        if target == 0:
            return 0
            
        queue = [(0, 1)] # (p,s)
        visited, cnt = set((0, 1)), 0

        while queue:
            newQueue = []
            cnt += 1

            for pos, speed in queue:
                p1, s1 = pos + speed, speed * 2
                newQueue.append((p1,s1))

                if p1 == target: return cnt
                
                p2, s2 = pos, -1 if s1 > 0 else 1
                if (p2,s2) not in visited:
                    visited.add((p2,s2))
                    newQueue.append((p2,s2))

            queue = newQueue

        return -1
                
        
        
        
                
