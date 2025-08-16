# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
setn= set(input().split())
b = int(input())
setb = set(input().split())
print(len(setn.union(setb)))

'''9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

13'''