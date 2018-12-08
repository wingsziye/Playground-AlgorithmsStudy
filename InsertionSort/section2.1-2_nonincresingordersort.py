def insertion_sort_decrease(listA):
    nl = list(range(1, len(listA)))
    print('index: %s' % (nl))
    for j in nl:
        key = listA[j]
        # insert listA[j] into the sorted sequence listA[1..,j-1]
        i = j - 1
        while i >= 0 and listA[i] < key:#just change > into <, you'll get decreasing order
            listA[i + 1] = listA[i]
            i = i - 1
        listA[i + 1] = key
    print('output:%s' % (listA))


lists = [31, 41, 59, 26, 41, -10]
print('origin:%s' % (lists))
insertion_sort_decrease(lists)
