# 269. Alien Dictionary 
# ttungl@gmail.com

# Referenne:
# https://discuss.leetcode.com/topic/22476/16-18-lines-python-30-lines-c

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # sol 1: 
        less = []
        for pair in zip(words, words[1:]):
            # print(pair)
            for a, b in zip(*pair):
                # print(a, b)
                if a != b:
                    less += a + b,
                    break
        chars = set(''.join(words))
        order = []
        while less:
            print(zip(*less)[1])
            free = chars - set(zip(*less)[1]) # retwf-fetr=w; retwf-twre=f;  
            if not free:
                return ''
            order += free
            less = filter(free.isdisjoint, less)
            chars -= free
        return ''.join(order + list(chars))
    
        # sol 2
        # stores predecessor and successor of chars. Use defaultdict(set).
        # BFS for each predecessor, traverse on successor, append to res. 
        # runtime: 64ms
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        free = chars - set(pre)
        order = ''
        while free:
            char = free.pop()
            order += char
            for b in suc[char]:
                pre[b].discard(char)
                if not pre[b]:
                    free.add(b)
        return order * (set(order) == chars)

        
        
## Test cases
# if __name__ == "__main__":
# 	words_1 = ["wrt", "wrf", "er", "ett", "rftt"]
# 	expected_order_1 = "wertf"

# 	words_2 = ["z", "x"]
# 	expected_order_2 = "zx"

# 	words_3 = ["z", "x", "z"]
# 	expected_order_3 = ""

# 	words_4 = ["a", "b", "c", "a"]
# 	expected_order_4 = ""

# 	assert(expected_order_1 == AlienOrder().alienOrder(words_1))
# 	assert(expected_order_2 == AlienOrder().alienOrder(words_2))

