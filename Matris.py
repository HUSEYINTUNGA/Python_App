size=int(input("Lütfen bir boyut değeri girin: "))

arr = [[0 for _ in range(size)] for _ in range(size)]

def Matris(size):
    for i in range(size):
        for j in range(size):
            for a in range(size):
                if i==a or j==a or i==size-(a+1) or j==size-(a+1):
                    arr[i][j]=a+1
                    break
            print("{:>4}".format(arr[i][j]) , end="")
        print()

Matris(size)
            