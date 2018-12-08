def findv(sequence, v):
    nl = list(range(0, len(sequence) - 1))
    for index in nl:
        if sequence[index] == v:
            return '%s' % index
    return 'NIL'


lists = [31, 41, 59, 26, 41, -10, 2, 4, 6, 1, 3]
num = input('please enter special number: ')
result = findv(lists, int(num))
print('result=%s' % result)
