def insertion_sort_decrease(listA):
    time = 1 #计算次数用
    nl = list(range(1, len(listA)))
    print('index: %s' % (nl))
    for j in nl:
        key = listA[j]
        # insert listA[j] into the sorted sequence listA[1..,j-1]
        i = j - 1
        while i >= 0 and listA[i] < key:#just change > into <, you'll get decreasing order
            listA[i + 1] = listA[i]
            i = i - 1
            time = time + 1
        listA[i + 1] = key
    print('output:%s' % (listA))
    print('计算次数:%s' % (time))


lists = [31, 41, 59, 26, 41, -10, 2, 4, 6, 1, 3]
print('origin:%s' % (lists))
insertion_sort_decrease(lists)
