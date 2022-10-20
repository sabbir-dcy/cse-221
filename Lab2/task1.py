def insertion_sort(arr,l): 
  for i in range(l-1): 
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
  inf = open(r'/content/sample_data/input1.txt','r') #input file
  otf = open(r'/content/sample_data/output1.txt','w') #output file

  # first line denotes len of the array
  l = int(inf.readline())

  # readling line as array
  # converting each element from string to integer
  # moving them to another array
  marks_arr = [int(a) for a in inf.readline().split(' ')]
  id_arr = [int(a) for a in inf.readline().split(' ')]

  student_arr = [] # empty array for objects

  # adding elements from both array as objects
  for i in range(l):
    student_arr.append({"marks":marks_arr[i], "id":id_arr[i]})

  insertion_sort(student_arr,l)
  printer(student_arr)



