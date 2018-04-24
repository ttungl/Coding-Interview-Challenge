# Top K Frequent Words 692
# ttungl@gmail.com
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        # sol 1:
        # runtime: 85ms
        freqs = {}
        counter = collections.Counter(words)
        for word, count in counter.items():
            if count not in freqs:
                freqs[count] = []
            freqs[count].append(word)
        res = []
        for i in range(len(words), 0, -1):
            if i in freqs:
                for w in freqs[i]:
                    res.append((w,i))
            if len(res)==k: break
        res.sort(cmp = lambda a, b: (b[1]-a[1]) 
                                    if a[1]!=b[1] 
                                    else (-1 
                                            if a[0] < b[0] 
                                            else 1)) 
        return [l[0] for l in res[:k]]
    
    
        # sol 2:
        # runtime: 56ms
        d = {} # dictionary to store occurrencies.
        for word in words:
            d[word] = d.get(word, 0) + 1
        res = sorted(d, key=lambda word: (-d[word], word))
        return res[:k]
    
    
        # sol 3:
        # runtime: 55ms
        d = {} # store words frequencies.
        for word in words:
            if word in d: d[word] += 1
            else: d[word] = 1
        
        uniWords = sorted(d.keys()) # sort of all returned keys in dictionary 
        res = sorted(uniWords, key=lambda x : -d[x]) # descending order using -d[x], so only care from 0-k in res.
        return res[:k]
        
        