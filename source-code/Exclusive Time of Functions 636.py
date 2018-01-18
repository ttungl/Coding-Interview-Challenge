# Exclusive Time of Functions 636


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # sol 1:
        # runtime: 105ms
        stack, res = [], [0]*n
        prev = 0
        for log in logs:
            fid, typ, time = log.split(':')
            fid, time = int(fid), int(time)
            if typ == 'start':
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(fid)
                prev = time
            else:
                res[stack.pop()] += time - prev + 1
                prev = time + 1
        return res
    
        # sol 2:
        # runtime: 132ms
        # ["0:start:0",
        #  "1:start:2",
        #  "1:end:5",
        #  "0:end:6"]
        stack, res = [], [0]*n
        for log in logs:                                # each log; [0:s:0]; [1s2], [1e5], [0e6]
            fid, typ, time = log.split(":")
            fid, time = int(fid), int(time)             # (fid=1, time=5) (0,6)
            if typ == 'start': 
                stack.append(time)                      # stack [0, 2]
            else:                                       # 'end'
                timediff = time - stack.pop() + 1       # diff = 4 = 5-[2]+1; f=3=6-4+1 
                res[fid] += timediff                    # res[1]=4 =0+4; res[0]=3=0+3; 
                stack = [ti + timediff for ti in stack] # stack = [4]; [];
        return res
        
        
                    
                    
                