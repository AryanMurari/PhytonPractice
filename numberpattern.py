#PRINT THE BELOW MENTIONED PATTERN FOR ANY "N" VALUE. WHERE "N" INDICATES NO.OF ROWS.

#1    5
 #2  4
 #  3

n=int(input())
for i in range(1,n//2 + 2):
    for j in range(1,n+1):
        if j==i or j==n-i+1:
            print(j,end="")
        else:
            print(" ",end="")
    print()
