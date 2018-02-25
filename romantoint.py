def value(k):
    if (k == 'I'):
        return 1
    if (k == 'V'):
        return 5
    if (k == 'X'):
        return 10
    if (k == 'L'):
        return 50
    if (k == 'C'):
        return 100
    if (k == 'D'):
        return 500
    if (k == 'M'):
        return 1000
    return -1
 
def romanToDecimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
        s1 = value(str[i])
 
        if (i+1 < len(str)):
            s2 = value(str[i+1])
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res
print("to convert roman number to integer number is:"),
print(romanToDecimal("IVX")) 
