def insertion_sort(arr):
  for i in range(len(arr)-1):
    current = arr[i+1]
    j = i
    while j >= 0:
      if arr[j]["id"] < current["id"]:
        arr[j+1] = arr[j]
      else:
        break
      j-=1  
    arr[j+1] = current 


def printer(arr):
  for x in arr:
    print(f'{x["marks"]}',end=' ', file=otf)

if __name__ == "__main__":
  inf = open(r'I:\CSE221\cse-221\Lab2\input1.txt','r')
  otf = open(r'I:\CSE221\cse-221\Lab2\output1.txt','w')

  inf.readline()

  # readling line as array
  # converting each element from string to integer
  # moving them to another array
  marks_arr = [int(a) for a in inf.readline().split(' ')]
  id_arr = [int(a) for a in inf.readline().split(' ')]

  student_arr = [] # empty array for objects

  # adding elements from both array as objects
  for i in range(len(marks_arr)):
    student_arr.append({"marks":marks_arr[i], "id":id_arr[i]})

  insertion_sort(student_arr)
  printer(student_arr)



