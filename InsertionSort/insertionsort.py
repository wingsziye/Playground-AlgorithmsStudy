def insertion_sort(listA):
    nl = list(range(1, len(listA)))
    print('index %s'%(nl))
    for j in nl:
        key = listA[j]
        # insert listA[j] into the sorted sequence listA[1..,j-1]
        i = j - 1
        while i >= 0 and listA[i] > key:
            listA[i + 1] = listA[i]
            i = i - 1
        listA[i + 1] = key
    print('output:%s'%(listA))

def insertion_sort_后序插入(listA):
    nl = list(range(len(listA) - 2, -1, -1))
    print('index %s'%(nl))
    for j in nl:
        key = listA[j]
        # print('j=%s key=%s'%(j,key))
        # insert listA[j] into the sorted sequence listA[1..,j-1]
        i = j + 1
        while i < len(listA) and listA[i] < key:
            listA[i-1] = listA[i]
            i = i + 1
        listA[i-1] = key
    print('output:%s'%(listA))

lists = [5, 2, 4, 6, 1, 3]
insertion_sort(lists)
insertion_sort_后序插入(lists)
