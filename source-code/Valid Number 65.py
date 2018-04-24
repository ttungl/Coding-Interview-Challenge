# 65. Valid Number
# ttungl@gmail.com

# Validate if a given string is numeric.

# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # sol 1:
        # runtime: 57ms
        try:
            float(s)
            return True
        except ValueError:
            return False


        # sol 2:
        # runtime: 52ms
        if not s: 
        	return False

        s = s.strip() # strip the heading and tailing spaces of the string
        i = 0

        res = signs = eE = dot = False

        while i < len(s):
            if s[i].isdigit():
                i+=1
                res = signs = True

            elif s[i]=='.' and not dot:
                i+=1
                dot = signs = True

            elif (s[i]=='e' or s[i]=='E') and (not eE) and res:
                i+=1
                res = signs = False
                dot = eE = True

            elif (s[i]=='+' or s[i]=='-') and not res and not signs:
                i+=1; signs = True

            else:
                return False
                
        return True if res else False
                
            
            
    
        
                
        
        
                
        
        
        
            
        


