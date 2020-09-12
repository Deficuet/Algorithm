Chrs = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMYKNPAwcF'
NumList = []
for i in range(0, 58):
    NumList.append(i)
ChrNumDic = dict(zip(Chrs, NumList))
EncIndexList = [11, 10, 3, 8, 4, 6, 2, 9, 5, 7]
DecIndexList = [6, 2, 4, 8, 5, 9, 3, 7, 1, 0]
def dec(BVNum):
    BVNum = list(BVNum)
    if ''.join(BVNum[:2]) == 'BV':
        BVNum = BVNum[2:]
    a = 0
    for j in range(0, 10):
        a += ChrNumDic[BVNum[j]] * 58 ** DecIndexList[j]
    return (a - 100618342136696320) ^ 177451812
def enc(AVNum):
    BVStr = list('BV__________')
    a = (177451812 ^ AVNum) + 100618342136696320
    for k in range(0, 10):
        BVStr[EncIndexList[k]] = Chrs[a // 58 ** k % 58]
    return ''.join(BVStr)
print(dec('BVaaaaaaaaaa'))