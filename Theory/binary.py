def binary_search(arr, l, r, k):
  if l >= r:
    return None
  mid = (l + r) // 2
  if k == arr[mid]:
    return mid
  elif k < arr[mid]:
    return binary_search(arr, l, mid, k)
  else:
    return binary_search(arr, mid+1, r, k)

arr = [10, 20, 30, 40, 50, 60]
print(binary_search(arr, 0, len(arr), 50))
