from sys import stdin
def sol():
    row, col = map(int,stdin.readline()[:-1].split())
    answer = [['.' for x in range(col)] for y in range(row)]
    for i in range(row):
        temp = list(stdin.readline()[:-1])
        for j in range(col):
            answer[i][j]=change(temp[j])
    for i in range(col-1,-1,-1):
        for j in range(row):
            if(j!= row-1):
                print(answer[j][i], end='')
            else:
                print(answer[j][i])
def change(chr):
    if(chr == '-'):
        return '|'
    elif(chr =='|'):
        return '-'
    elif(chr =='/'):
        return '\\'
    elif(chr =='\\'):
        return '/'
    elif(chr =='^'):
        return '<'
    elif(chr =='<'):
        return 'v'
    elif(chr =='v'):
        return '>'
    elif(chr =='>'):
        return '^'
    else:
        return chr
if __name__ == '__main__':
    sol()