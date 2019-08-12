def selection_sort(li):
    for i in range(len(li)-1):
        min_idx = i
        for j in range(i+1, len(li)):
            if(li[min_idx] > li[j]):
                min_idx = j
        if(i!=min_idx):
            li[i], li[min_idx] = li[min_idx], li[i]
    return li
if __name__ == "__main__":
    li = [2,5,6,1,3,8,4,3,9,6,10,11,12]
    print(selection_sort(li))
