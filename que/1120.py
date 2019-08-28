from sys import stdin
def sol():
    sen = list(map(str,stdin.readline()[:-1].split()))
    length = len(sen[1]) - len(sen[0])
    answer = 50 
    for i in range(length+1):
        temp = 0
        for j in range(len(sen[0])):
            if(sen[0][j] != sen[1][j+i]):
                temp += 1
        if(temp < answer):
            answer = temp
    return answer
if __name__ == "__main__":
    print(sol())

        
        