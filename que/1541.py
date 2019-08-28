from sys import stdin
def sol():
    sen = list(map(str,stdin.readline()[:-1].split('-')))
    for i in range(len(sen)):
        temp = 0
        tlist = list(map(str, sen[i].split('+')))
        for j in tlist:
            temp+=int(j)
            if(i==0):
                answer = temp
        if(i !=0):
            answer -= temp
    print(answer)

if __name__ =='__main__':
    sol()