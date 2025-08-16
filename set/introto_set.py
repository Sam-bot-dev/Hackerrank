def average(arr):
  array = set(arr)
  total = sum(array)
  avg  = total / len(array)
  return avg 

''' input would be first number of elements in array then the array elements like 10 
161 161 161 161 161 161 161 161'''

if __name__ == '__main__':
  n = int(input())
  arr = list(map(int, input().split()))
  result = average(arr)
  print(result)