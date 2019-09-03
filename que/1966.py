from sys import stdin
def sol():
    testcase = (int(stdin.readline()[:-1]))
    al = [] 
    for i in range(testcase):
        answer = 0
        arr1 = list(map(int,stdin.readline()[:-1].split()))
        find = arr1[1]
        arr2 = list(map(int,stdin.readline()[:-1].split()))
        al.append(que(find, arr2, answer)) 
    for item in al:
        print(item)
def que(find,arr,answer):
    for i in range(len(arr)):
        if(arr[i] > arr[0]):
            arr.append(arr[0])
            arr.pop(0)
            if(find == 0):
                return que(len(arr)-1,arr,answer)
            else:
                return que(find-1, arr, answer)
    arr.pop(0)
    if(find == 0):
        return (answer + 1)
    else:
        return que(find-1, arr, answer+1)
if __name__ == "__main__":
    sol()