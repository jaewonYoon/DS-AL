def bubbleSort(alist):
    for i in range(len(alist)-1):
        for j in range(len(alist)-1-i):
            if(alist[j+1] < alist[j]):
                alist[j+1], alist[j] = alist[j], alist[j+1]

if __name__ == "__main__":
    li = [3,2,1,4]
    bubbleSort(li)
    print(li)
