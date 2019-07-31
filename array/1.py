def rotate(arr, n ,d):
        temp1 = arr[n:d]
        temp2 = arr[0:n]
        print(temp1 + temp2)

#time complexity : o(n)
#auxiliary space : o(d) 

