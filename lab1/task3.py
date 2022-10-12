def bubbleSort(arr):
  lent = len(arr)
  swap = False # flag check

  for i in range(lent-1):
    for j in range(lent-i-1):
      if arr[j] > arr[j+1]:
        swap = True
        arr[j], arr[j+1] = arr[j+1], arr[j]
    # check if any swap happens
    if not swap:
      return



if __name__ == '__main__':
  f = open(r'C:\Users\sas\Desktop\New folder\python\lab1\input3.txt','r')
  op = open(r'C:\Users\sas\Desktop\New folder\python\lab1\output3.txt','w')

  f.readline()
  arr = f.readline().split(' ')
  arr = [int(a) for a in arr]

  bubbleSort(arr)

  for x in arr:
    print(f'{x} ',end=' ', file=op)