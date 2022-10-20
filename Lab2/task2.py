def mergeSort(arr):
  n = len(arr)
  if n == 1:
    return arr
  mid = n // 2

  left_arr = []
  right_arr = []

  for i in range(mid):
    left_arr.append(arr[i])
  for i in range(mid, n):
    right_arr.append(arr[i])

  left_part = mergeSort(left_arr)
  righet_part = mergeSort(right_arr)
  
  return merge(left_part,righet_part)

def merge(left_arr, right_arr):
  arr = []
  i = j = 0
  while i < len(left_arr) and j < len(right_arr):
    if left_arr[i] < right_arr[j]:
      arr.append(left_arr[i])
      i += 1
    else:
      arr.append(right_arr[j])
      j += 1

  while i < len(left_arr):
    arr.append(left_arr[i])
    i += 1
  
  while j < len(right_arr):
    arr.append(right_arr[j])
    j += 1
  
  return arr
arr = [54, 13, 76, 43, 87, 62, 37, 14]
arr = mergeSort(arr)
print(arr)