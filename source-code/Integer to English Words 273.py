# 273. Integer to English Words
# ttungl@gmail.com
# Convert a non-negative integer to its english words 
# representation. Given input is guaranteed to be less 
# than 2^31 - 1.

# For example,
# 123 -> "One Hundred Twenty Three"
# 12345 -> "Twelve Thousand Three Hundred Forty Five"
# 1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"


class Solution(object):
    
    def __init__(self):
        ### init_1
        # self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen",\
        #                    "Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        # self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        # self.thousands = ["","Thousand","Million","Billion"]
        ### init_2
        self.lessThan20 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        self.tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        self.thousands = 'Thousand Million Billion'.split()
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        # sol 1:
        # use init_1
        # runtime: 52ms
        if not num:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if not (num % 1000 == 0):
                res = self.wordsProcess(num % 1000) + self.thousands[i] + " " + res
            num /= 1000
        return res.strip()
    def wordsProcess(self, num):
        if not num:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num/10] + " " + self.wordsProcess(num % 10)
        else:
            return self.lessThan20[num/100] + " Hundred " + self.wordsProcess(num % 100)
    
        # sol 2:
        # use init_2
        # runtime: 43ms
        def words(n):
            if n < 20:
                return self.lessThan20[n-1:n]
            if n < 100:
                return [self.tens[n/10-2]] + words(n%10)
            if n < 1000:
                return [self.lessThan20[n/100-1]] + ['Hundred'] + words(n%100)
            for p, w in enumerate(self.thousands, 1):
                if n < 1000**(p+1):
                    return words(n/1000**p) + [w] + words(n%1000**p)
        ##        
        return ' '.join(words(num)) or "Zero"
        
        # sol 3:
        # use init_2
        # runtime: 39ms
        return ' '.join(self.wordsProcess(num)) or "Zero"
    
    def wordsProcess(self, n):
        if n < 20:
            return self.lessThan20[n-1:n]
        
        elif n < 100:
            return [self.tens[n/10 - 2]] + self.wordsProcess(n%10)
        
        elif n < 1000:
            return [self.lessThan20[n/100 - 1]] + ['Hundred'] + self.wordsProcess(n%100)
         
        for i, v in enumerate(self.thousands, 1):
            if n < 1000**(i + 1):
                return self.wordsProcess(n/1000**i) + [v] + self.wordsProcess(n%1000**i)
    
        
        
    
    
        
        
        
    
    
        
        
        
        
        
        





