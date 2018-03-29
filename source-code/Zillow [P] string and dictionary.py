## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

# Given a string, return the first character that doesn’t repeat elsewhere in the given string


str = hellohes

return o

# str = aa


d = {h:[0,5]
     e:[1,6]
     l:[2,3]
     o:[4]
     s:[7]
}
     
d = {a = [0, 1]
    
}     
     
def firstChar(str):
    res = ""
    tem = []
    d = collections.defaultdict(list)
    for i, c in enumerate(str):
        d[c] = d.get(c, []) + [i]
    
    for d in d.values():
        if len(d)==1:
            tem.append(d[0])
    if tem:
        minval = min(tem)
    else:
        return res 
    
    for k,v in d.items():
        if len(v)==1 and minval==v[0]:
            res = k 
    return res 
            