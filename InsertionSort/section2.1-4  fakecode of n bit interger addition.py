def binaryAddtion(binaryA, binaryB):  # each digit is a number, either 0 or 1, high-significant digit first
    constrainlen(binaryA, binaryB)
    arrC = list()
    carry = 0  # 进位
    for i in range(len(binaryA) - 1, -1, -1):
        arrC.insert(binaryA[i] ^ binaryB[i] ^ carry, 0)  # step1 0+0=0 1+1=0 0+1=1 1+0=1 异或计算
        carry = (binaryA[i] + binaryB[i] + carry) // 2  # step2 "//"in python e.g. 3/2=1 2/2 =1 2/1=0
    arrC.insert(carry, 0)
    return arrC


def constrainlen(binaryA, binaryB):  # constrain binaryA.length==binaryB.length
    differ = len(binaryA) - len(binaryB)
    if differ > 0:
        for i in range(differ):
            binaryB.insert(0)
    else:
        for i in range(abs(differ)):
            binaryA.insert(0)


arrA = [1, 1, 0, 0, 1, 0, 1, 1, 0, 0]
arrB = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0]
arrA.reverse()
arrB.reverse()
binaryAddtion(arrA, arrB)
''' 运行结果构想
        //1 1 0 0 1 0 1 1 0 0 low<-high
        //1 0 0 0 0 0 1 1 0 0 low<-high
step1 0 //0 0 1 0 1 0 0 1 1 0 low<-high
st2-1 0 //2 2 1 0 1 0 2 3 1 0
st2-2 0 //1 1 0 0 0 0 1 1 0 0
'''
