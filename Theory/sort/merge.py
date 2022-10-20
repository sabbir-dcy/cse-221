def merge_sort(arr, l ,r):
  if len(arr) > 1:
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    merge_sort(left_arr, l, mid)
    merge_sort(right_arr, mid + 1, r)
    merge(arr, left_arr, right_arr)

def merge(arr, L, R):
  i = j = k = 0
  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
    else:
        arr[k] = R[j]
        j += 1
    k += 1

  # Checking if any element was left
  while i < len(L):
    arr[k] = L[i]
    i += 1
    k += 1

  while j < len(R):
    arr[k] = R[j]
    j += 1
    k += 1

arr = [10, 15, 16, 5, 2, 9, 11, 5, 2, 4, 7]
merge_sort(arr, 0, len(arr))
print(arr)

