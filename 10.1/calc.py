
def getKef(formula):
    left = formula.split("=")[0]
    splpls = left.split("+")
    chlns = []
    for i in range(len(splpls)):
        splmns = splpls[i].split("-")
        if i == 0 and len(splmns) > 1:
            for j in range(1, len(splmns)):
                chlns.append("-" + splmns[j])
        else:
            chlns.append(splmns[0])
            if len(splmns) > 1:
                for j in range(1, len(splmns)):
                    chlns.append("-" + splmns[j])
    pwr = []
    for i in range(len(chlns)):
        if len(chlns[i].split("x^")) != 1:
            pwr.append(chlns[i].split("x^")[1])
        elif len(chlns[i].split("x")) != 1:
            pwr.append("1")
        elif len(chlns[i].split("x")) == 1:
            pwr.append("0")
    
    ielm = int(chlns[0].split("x^")[1])
    ipwr = 0
    kef = []
    while ielm > 0:
        if ipwr < len(pwr) and int(pwr[ipwr]) == ielm:
            kef.append(int(chlns[ipwr].split("x")[0]))
            ipwr += 1
        else:
            kef.append(0)
        ielm -= 1
    if pwr[-1] == "0":
        kef.append(int(chlns[-1]))
    else:
        kef.append(0)
        
    
    return kef


def calc (formulaOne, formulaTwo):
    kf1 = getKef(formulaOne)
    kf2 = getKef(formulaTwo)
    reskf = []
    if len(kf1) > len(kf2):
        for i in range(len(kf2)):
            reskf.append(kf1[-i-1] + kf2[-i-1])
        for i in range(len(kf2), len(kf1)):
            reskf.append(kf1[-i-1])
    elif len(kf1) < len(kf2):
        for i in range(len(kf1)):
            reskf.append(kf1[-i-1] + kf2[-i-1])
        for i in range(len(kf1), len(kf2)):
            reskf.append(kf2[-i-1])
    else:
        for i in range(len(kf1)):
            reskf.append(kf1[-i-1] + kf2[-i-1])

    res = ""
    k = len(reskf) - 1
    for i in range(k - 1):
        if reskf[k - i] != 0:
            if reskf[k - i] == 1:
                res = res + "x^" + str(k - i) + "+"
            else:
                res = res + str(reskf[k - i]) + "x^" + str(k - i) + "+"

    if reskf[1] != 0:
        if reskf[1] == 1:
            res = res + "x"
        else:
            res = res + str(reskf[1]) + "x+"

    if reskf[0] != 0:
        res = res + str(reskf[0])
    
    res = res + "=0"
    
    return res
