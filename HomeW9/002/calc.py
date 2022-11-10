import re

def clclt(formul):
    while re.search(r'[\(\)]', formul) != None:
        formul = openHook(formul)
    nmb = re.findall(r'[0-9\.]+', formul)
    znk = re.findall(r'[/\*\-\+]', formul)
    i = 0
    while i < len(znk):
        if znk[i] == '*':
            nmb[i] = str(float(nmb[i]) * float(nmb.pop(i+1)))
            znk.pop(i)
        elif znk[i] == '/':
            nmb[i] = str(float(nmb[i]) / float(nmb.pop(i+1)))
            znk.pop(i)
        else:
            i = i + 1
    i = 0
        
    while i < len(znk):
        if znk[i] == '+':
            nmb[i] = str(float(nmb[i]) + float(nmb.pop(i+1)))
            znk.pop(i)
        elif znk[i] == '-':
            nmb[i] = str(float(nmb[i]) - float(nmb.pop(i+1)))
            znk.pop(i)
    
    return nmb[0]

def openHook (formul):
    infrl = re.findall('\([^\(\)]+\)', formul)
    outfrl = re.split('\([^\(\)]+\)', formul)
    res = outfrl[0]
    
    for i in range(len(infrl)):
        res = res + clclt(infrl[i][1:-1]) + outfrl[i+1]
    
    return res


