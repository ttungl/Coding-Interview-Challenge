
# Complete the function below.
def checkPangram(s):
    s = s.lower()
    tem = []
    for i in s:
        tem.append(ord(i))
    for i in range(ord('a'), ord('z')+1):
        if i not in tem:
            return False
    return True

def isPangram(strings):
    res = ""
    for s in strings:
        state = checkPangram(s)
        if state:
            res += '1'
        else:
            res += '0'
    return res
        
                
            
