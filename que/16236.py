from sys import stdin
def sol():
    dic = {}
    size = int(stdin.readline()[:-1])
    vase = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        line = list(map(int,stdin.readline()[:-1].split()))
        for j in range(size):
            if( line[j] != 0):
                if(line[j] in dic.keys()):
                    dic[line[j]].append([i,j])
                else:
                    dic[line[j]] =  [[i,j]]
            vase[i][j] = line[j]
    while(True):
        answer = check(vase, fSize=2, dic)
        if( answer == False):
            return 0
        else:
            return answer
        
            
def check(arr, fSize, dic ):
    temp = fSize
    count = [0]
    while(temp > 0):
        if(temp in dic.keys()):
            for item in dic[temp]:
                i,j = item[0], item[1]
                return backTrack(arr, i, j ,fSize, time, dic, count)
                del dic[temp]
        temp -=1
    return False
def backTrack(arr, i,j, fSize, target, time, dic ,count):
    if(arr[i][j] == target):
        count[0] +=1 
        arr[i][j] = 0
        return time
    elif(i > 0 and arr[i-1][j]<=arr[i][j]):
        time += 1
        backTrack(arr, i-1, j, fSize, time)
    elif(j > 0 and arr[i][j-1] <= arr[i][j]):
        time += 1
        backTrack(arr, i, j-1, fSize, time)
    elif(i < fSize and arr[i+1][j] <= arr[i][j]):
        time += 1
        backTrack(arr, i+1, j, fSize, time)
    elif(j < fSize and arr[i][j+1] <= arr[i][j]):
        time +=1
        backTrack(arr, i, j+1, fSize, time)
    else: 
        return False  
if __name__ =='__main__':
    print(sol())