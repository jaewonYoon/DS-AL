from sys import stdin
def sol():
    num = int(stdin.readline()[:-1])
    dic = {}
    start_num  = []
    answer = 0
    dp = {}
    for i in range(num):
        arr = list(map(int,stdin.readline()[:-1].split()))
        if(dic.get(arr[0]) is None or dic[arr[0]] > arr[1]):
            dic[arr[0]] = arr[1]
        start_num.append(arr[0])
    arr_start = list(dic.keys()) 
    arr_start.sort(reverse=True)
    for i in range(len(arr_start)):
        temp = tra(arr_start[i],dic,arr_start,dp)
        if answer < temp:
            answer = temp 
    print(answer)
def tra(start,dic, arr_start,dp):
    if(dp.get(start)):
        return dp.get(start)
    else:sdfsd
        answer = 0
        if dic[start] < arr_start[0]:
            while(dic[start] not in arr_start):
                dic[start] +=1 
            answer =  1 + tra(dic[start],dic,arr_start,dp)
        else :
            answer = 1
        dp[start] = answer
        return answer
if __name__ == "__main__":
    sol()