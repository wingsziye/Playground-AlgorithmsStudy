def selection(sequence):
    time = 1 #计算次数用
    nl = list( range( 0, len( sequence ) - 2 ) )
    for n in nl : #选择
        index = n + 1
        min = sequence[n]
        minindex = n;
        while index < len( sequence ) :
            if sequence[index] < min :
                min = sequence[index]
                minindex = index
            index = index + 1
            time = time +1
        temp = sequence[n]
        sequence[n] = min
        sequence[minindex] = temp
    print('计算次数:%s' % (time))

lists = [31, 41, 59, 26, 41, -10, 2, 4, 6, 1, 3]
print('origin:%s' % (lists))
selection(lists)
print('output:%s' % (lists))
