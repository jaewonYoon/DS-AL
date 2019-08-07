def selection_sort(li):
    for i in range(len(li)-1):
        min_idx=i
        for j in range(i+1,len(li)):
            if li[min_idx] > li[j]: 
                min_idx = j
        if min_idx != i:
            li[i], li[min_idx] = li[min_idx], li[i]
    return li
    
if __name__ == "__main__": 
    for i in range(10): 
        print(i)