import re


def parsPolinom(s):  # разбор полинома
    s = s.replace('-', '+-')
    print(s)
    match = re.split('\+|=', s)
    num = dict()
    for i in match:
        # выбираем коэффициенты
        k = re.search(r'^-?\d*', i)
        K = k[0] if k else '1'
        d = re.search(r'(x\^)\d*', i)  # выбираем степени
        if d:
            D = int(re.search(r'\d+', d[0])[0])
        else:
            d = re.search(r'x', i)
            if d:
                D = 1
            else:
                D = 0
        if D in num:
            num[D] = num[D]+int(K)
        else:
            num[D] = int(K)
    return (num)


def sumPolinom(a, b):  # сложение полиномов
    sum = dict()
    keys = list(a.keys())
    keys.extend(b.keys())
    maxDegree = max(keys)
    for i in range(maxDegree+1):
        if (i in b) and (i in a):
            sum[i] = a[i]+b[i]
        elif i in a:
            sum[i] = a[i]
        elif i in b:
            sum[i] = b[i]
    result = ""
    flag = True
    y = sorted(sum, reverse=True)
    for i in sorted(sum, reverse=True):
        plus = '+'
        if flag or sum[i] < 0:
            plus = ''
            flag = False
        degree = ''
        if i > 1:
            degree = f"*x^{i}"
        elif i == 1:
            degree = f"*x"
        else:
            degree = f""
        result = result + f"{plus}{sum[i]}{degree}"
    return result+"=0"
